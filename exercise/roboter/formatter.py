"""レストラン名をパスカルケースに変換するユーティリティ。"""


def to_pascal_case(s: str) -> str:
    """文字列をパスカルケース（各単語の先頭を大文字）に変換する。

    例: "cool one" -> "Cool One", "japanese apple" -> "Japanese Apple"
    """
    if not s or not s.strip():
        return ""
    return " ".join(word.capitalize() for word in s.strip().split())
