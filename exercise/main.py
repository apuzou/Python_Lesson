"""Roboter アプリのエントリポイント。ターミナルで python main.py で実行する。"""

import os

from roboter.controller.conversation import run_session


def _base_dir() -> str:
    """main.py があるディレクトリを返す。"""
    return os.path.dirname(os.path.abspath(__file__))


def main() -> None:
    """exit が入力されるまで会話を繰り返す。"""
    base = _base_dir()
    while True:
        if run_session(base) == "exit":
            break


if __name__ == "__main__":
    main()
