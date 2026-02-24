"""ranking.csv の読み書き・カウント更新を行うモジュール。"""

import csv
import logging
import os

logger = logging.getLogger(__name__)

def _to_pascal_case(s: str) -> str:
    """文字列をパスカルケース（各単語の先頭を大文字）に変換する。

    例: "cool one" -> "Cool One", "japanese apple" -> "Japanese Apple"
    """
    if not s or not s.strip():
        return ""
    return " ".join(word.capitalize() for word in s.strip().split())


def _get_filepath(filename: str, base_dir: str) -> str:
    """base_dir を基準にしたファイルパスを返す。"""
    return os.path.join(base_dir, filename)


def load_ranking(base_dir: str, filename: str = "ranking.csv") -> list[tuple[str, int]]:
    """ranking.csv を読み、カウントの降順で (NAME, COUNT) のリストを返す。

    ファイルが存在しないか空の場合は空リストを返す。
    """
    filepath = _get_filepath(filename, base_dir)
    if not os.path.exists(filepath):
        logger.warning(f"ファイルが存在しません: {filepath}")
        return []

    rows = []
    with open(filepath, "r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = row.get("NAME", "").strip()
            try:
                count = int(row.get("COUNT", 0))
            except ValueError:
                count = 0
            if name:
                rows.append((name, count))

    rows.sort(key=lambda x: x[1], reverse=True)
    return rows


def increment_and_save(
    base_dir: str, restaurant_name: str, filename: str = "ranking.csv"
) -> None:
    """指定レストラン名のカウントを1増やし、ranking.csv に保存する。

    既存になければ COUNT=1 で追加する。
    レストラン名はパスカルケースに正規化して保存する。
    """
    restaurant_name = _to_pascal_case(restaurant_name)
    if not restaurant_name:
        return

    filepath = _get_filepath(filename, base_dir)
    rows = load_ranking(base_dir, filename)
    name_to_count = {name: count for name, count in rows}

    name_to_count[restaurant_name] = name_to_count.get(restaurant_name, 0) + 1
    new_rows = sorted(name_to_count.items(), key=lambda x: x[1], reverse=True)

    os.makedirs(base_dir, exist_ok=True)
    with open(filepath, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["NAME", "COUNT"])
        for name, count in new_rows:
            writer.writerow([name, count])
    logger.info({
        "action": "save",
        "status": "success",
    })
