"""ターミナルへの表示・入力を行うビューモジュール。"""

from functools import wraps
from termcolor import colored


def green(f):
    """関数が返す文字列を緑色で表示する。"""

    @wraps(f)
    def wrapper(*args, **kwargs):
        text = f(*args, **kwargs)
        if text is not None:
            print(colored(text, "green"))
    return wrapper


def with_separator(f):
    """表示の前後を緑の区切り線（===）で挟む。"""

    @wraps(f)
    def wrapper(*args, **kwargs):
        sep = colored("=" * 50, "green")
        print(sep)
        f(*args, **kwargs)
        print(sep)
    return wrapper


@with_separator
@green
def show_message_block(text: str) -> str:
    """区切り線で挟んでメッセージを緑色で表示する。"""
    return text


def read_input() -> str:
    """ユーザー入力を1行読み、前後の空白を除いて返す。"""
    return input().strip()
