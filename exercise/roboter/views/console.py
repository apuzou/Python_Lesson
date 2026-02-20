"""ターミナルへの表示・入力を行うビューモジュール。"""

from termcolor import colored


def show_message(text: str) -> None:
    """Roboter のメッセージを緑色で表示する。"""
    print(colored(text, "green"))


def show_separator() -> None:
    """区切り線を緑色で表示する。"""
    print(colored("=" * 50, "green"))


def show_message_block(text: str) -> None:
    """区切り線で挟んでメッセージを緑色で表示する。"""
    show_separator()
    show_message(text)
    show_separator()


def read_input() -> str:
    """ユーザー入力を1行読み、前後の空白を除いて返す。"""
    return input().strip()
