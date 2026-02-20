"""会話の流れを制御するコントローラ。"""

from roboter.models import robot
from roboter.views import console


def run_session(base_dir: str) -> str | None:
    """1回の会話セッションを実行する。

    Args:
        base_dir: ranking.csv を置くディレクトリ（通常は main.py があるディレクトリ）。

    Returns:
        "exit" のとき "exit" を返す。通常終了時は None。
    """
    restaurant_robot = robot.RestaurantRobot(view=console, base_dir=base_dir)

    name = restaurant_robot.hello()
    if name == "exit":
        return "exit"

    result = restaurant_robot.recommend_restaurant(name)
    if result == "liked":
        return None

    restaurant_robot.ask_user_favorite(name)
    restaurant_robot.thank_you(name)
    return None
