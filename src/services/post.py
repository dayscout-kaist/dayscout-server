from src.schemas import Post


def search_post_by_food_id(food_id: int) -> Post:
    return Post(
        id=1, content="test", food_id=1, user_id=1, created_at="2021-09-16 00:00:00"
    )
