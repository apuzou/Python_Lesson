"""Roboter の会話メッセージを返すモジュール。"""


def greet_and_ask_name() -> str:
    """挨拶と名前の質問メッセージを返す。"""
    return "こんにちは！私はRobokoです。あなたの名前は何ですか？"


def ask_like_restaurant(restaurant_name: str) -> str:
    """おすすめレストランについて好きかどうか聞くメッセージを返す。"""
    return f"私のオススメのレストランは、{restaurant_name}です。このレストランは好きですか？ [Yes/No]"


def ask_favorite_restaurant(user_name: str) -> str:
    """好きなレストランを聞くメッセージを返す。"""
    return f"{user_name}さん。どこのレストランが好きですか？"


def closing(user_name: str) -> str:
    """締めの挨拶メッセージを返す。"""
    return f"{user_name}さん。ありがとうございました。良い一日を！さようなら。"
