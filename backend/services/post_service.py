from backend.models.post import Post
from backend.extensions import db


class PostService:
    @staticmethod
    def create_post(data):
        try:
            post = Post(
                title=data['title'],
                content=data['content']
            )
            db.session.add(post)
            db.session.commit()
            return True, post.to_dict()
        except Exception as e:
            db.session.rollback()
            return False, str(e)

    @staticmethod
    def get_all_posts():
        try:
            posts = [post.to_dict() for post in Post.query.all()]
            return True, posts
        except Exception as e:
            return False, str(e)

    @staticmethod
    def get_post_by_id(post_id):
        try:
            post = Post.query.filter_by(id=post_id).first()
            return True, post.to_dict()
        except Exception as e:
            return False, str(e)

    @staticmethod
    def delete_post(post_id):
        try:
            post = Post.query.filter_by(id=post_id).first()
            if not post:
                return False, "Post not found"
            db.session.delete(post)
            db.session.commit()
            return True, "Post deleted"
        except Exception as e:
            db.session.rollback()
            return False, str(e)

    @staticmethod
    def update_post(post_id, data):
        try:
            post = Post.query.filter_by(id=post_id).first()
            if not post:
                return False, "Post not found"
            post.title = data['title']
            post.content = data['content']
            db.session.commit()
            return True, post.to_dict()
        except Exception as e:
            db.session.rollback()
            return False, str(e)
