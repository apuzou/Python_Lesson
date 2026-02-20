"""Roboter アプリのエントリポイント。ターミナルで python main.py で実行する。"""

import os
from termcolor import colored

from roboter import conversation, csv_manager, formatter

RANKING_FILENAME = "ranking.csv"


def _base_dir() -> str:
    """main.py があるディレクトリを返す。"""
    return os.path.dirname(os.path.abspath(__file__))


def _print_robot(msg: str) -> None:
    """Roboter のメッセージを緑色で表示する。"""
    print(colored(msg, "green"))


def _separator() -> None:
    """区切り線を緑色で表示する。"""
    print(colored("=" * 50, "green"))


def run_session() -> str | None:
    """1回の会話セッションを実行する。

    Returns:
        "exit" のとき "exit" を返す。通常終了時は None。
    """
    _separator()
    _print_robot(conversation.greet_and_ask_name())
    _separator()

    name = input().strip()
    if name.lower() == "exit":
        return "exit"

    base = _base_dir()
    ranking = csv_manager.load_ranking(base, RANKING_FILENAME)

    if ranking:
        for restaurant_name, _ in ranking:
            _separator()
            _print_robot(conversation.ask_like_restaurant(restaurant_name))
            _separator()

            answer = input().strip().lower()
            if answer == "exit":
                return "exit"
            if answer == "yes":
                csv_manager.increment_and_save(base, restaurant_name, RANKING_FILENAME)
                _separator()
                _print_robot(conversation.closing(name))
                _separator()
                return None
            # No の場合は次のレストランへ

    # ランキングが空 or すべて No → 好きなレストランを聞く
    _separator()
    _print_robot(conversation.ask_favorite_restaurant(name))
    _separator()

    restaurant = input().strip()
    if restaurant.lower() == "exit":
        return "exit"

    restaurant = formatter.to_pascal_case(restaurant)
    if restaurant:
        csv_manager.increment_and_save(base, restaurant, RANKING_FILENAME)

    _separator()
    _print_robot(conversation.closing(name))
    _separator()
    return None


def main() -> None:
    """exit が入力されるまで会話を繰り返す。"""
    while True:
        result = run_session()
        if result == "exit":
            break


if __name__ == "__main__":
    main()
