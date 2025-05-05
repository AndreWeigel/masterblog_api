from backend.models.post import Post
from backend.extensions import db
from sqlalchemy import asc, desc



class PostService:
    """Service class for Post model."""
    @staticmethod
    def create_post(data):
        """Create a new post."""
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
    def get_all_posts(sort_by='id', order='desc'):
        """Get all posts."""
        try:
            # Determine order direction
            column = getattr(Post, sort_by)
            ordering = desc(column) if order == 'desc' else asc(column)

            posts = [post.to_dict() for post in Post.query.order_by(ordering).all()]
            return True, posts
        except Exception as e:
            return False, str(e)

    @staticmethod
    def get_post_by_id(post_id):
        """Get a post by ID."""
        try:
            post = Post.query.filter_by(id=post_id).first()
            return True, post.to_dict()
        except Exception as e:
            return False, str(e)

    @staticmethod
    def search_posts( **kwargs):
        """Search for posts based on title and content."""
        try:
            title_query = kwargs.get('title', '').strip()
            content_query = kwargs.get('content', '').strip()

            query = Post.query
            if title_query:
                query = query.filter(Post.title.ilike(f'%{title_query}%'))
            if content_query:
                query = query.filter(Post.content.ilike(f'%{content_query}%'))

            posts = [post.to_dict() for post in query]
            return True, posts
        except Exception as e:
            return False, str(e)

    @staticmethod
    def delete_post(post_id):
        """Delete a post by ID."""
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
        """Update a post by ID."""
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
