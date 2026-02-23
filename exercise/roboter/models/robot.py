"""ロボットの振る舞い（会話フローなど）を扱うモジュール。"""

import os
from typing import Literal

from roboter.models import ranking

from roboter.views.console import show_message_block

RANKING_FILENAME = "ranking.csv"


class RestaurantRobot:
    """レストラン推薦の会話を行うロボット。"""

    def __init__(self, base_dir: str) -> None:
        self._base_dir = base_dir

    def _templates_dir(self) -> str:
        """roboter パッケージ内の templates ディレクトリのパスを返す。"""
        this_dir = os.path.dirname(os.path.abspath(__file__))
        package_dir = os.path.dirname(this_dir)
        return os.path.join(package_dir, "templates")

    def _load_template(self, name: str) -> str:
        """テンプレートファイルを読み込み、内容を返す。"""
        path = os.path.join(self._templates_dir(), name)
        with open(path, "r", encoding="utf-8") as f:
            return f.read().strip()

    def _show_template(self, template_name: str, **kwargs: str) -> None:
        """テンプレートを読み込み、フォーマットして表示する。"""
        content = self._load_template(template_name)
        if kwargs:
            content = content.format(**kwargs)
        show_message_block(content)

    def _save_restaurant(self, restaurant_name: str) -> None:
        """レストランをランキングに追加・更新して保存する。"""
        ranking.increment_and_save(
            self._base_dir, restaurant_name, RANKING_FILENAME
        )

    def _is_exit(self, s: str) -> bool:
        """入力が終了コマンドかどうかを返す。"""
        return s.strip().lower() == "exit"

    def hello(self) -> str:
        """挨拶して名前を聞く。ユーザー名を返す。'exit' のときは 'exit' を返す。"""
        self._show_template("hello.txt")
        name = self._view.read_input()
        return "exit" if self._is_exit(name) else name

    def recommend_restaurant(self, user_name: str) -> Literal["liked", "ask_favorite"]:
        """ランキングからおすすめを聞く。

        Returns:
            'liked': Yes と答えたので保存し締め済み
            'ask_favorite': すべて No またはその他なので好きなレストランを聞く段階へ
        """
        ranking_list = ranking.load_ranking(self._base_dir, RANKING_FILENAME)
        if not ranking_list:
            return "ask_favorite"

        for restaurant_name, _ in ranking_list:
            self._show_template(
                "like_restaurant.txt", restaurant_name=restaurant_name
            )

            answer = self._view.read_input().strip().lower()
            if answer == "yes":
                self._save_restaurant(restaurant_name)
                self.thank_you(user_name)
                return "liked"

        return "ask_favorite"

    def ask_user_favorite(self, user_name: str) -> None:
        """好きなレストランを聞き、保存する。"""
        self._show_template("which_restaurant.txt", user_name=user_name)

        restaurant = self._view.read_input()
        self._save_restaurant(restaurant)

    def thank_you(self, user_name: str) -> None:
        """締めの挨拶を表示する。"""
        self._show_template("good_by.txt", user_name=user_name)
