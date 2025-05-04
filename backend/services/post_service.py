from backend.models.post import Post
from backend.extensions import db


class PostService:
    @staticmethod
    def create_post(data) -> Post:
        post = Post(
            title=data['title'],
            content=data['content']
        )
        db.session.add(post)
        db.session.commit()
        return post

    @staticmethod
    def get_all_posts():
        return [post.to_dict() for post in Post.query.all()]



