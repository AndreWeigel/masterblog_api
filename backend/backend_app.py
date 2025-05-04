from flask import Flask, jsonify, request
from flask_cors import CORS


from backend.services.post_service import PostService
from backend.extensions import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
db.init_app(app)

with app.app_context():
    db.create_all()

CORS(app)  # This will enable CORS for all routes

POSTS = [
    {"id": 1, "title": "First post", "content": "This is the first post."},
    {"id": 2, "title": "Second post", "content": "This is the second post."},
]

@app.before_request
def log_request_info():
    print(f"Method: {request.method}, Path: {request.path}")


@app.route('/api/posts', methods=['GET'])
def get_posts():
    blog = PostService()
    return blog.get_all_posts()


@app.route('/api/posts', methods=['POST'])
def add_post():
    blog = PostService()

    data = request.get_json()

    required_fields = ['title', 'content']
    missing_fields = [field for field in required_fields if field not in data]

    if missing_fields:
        return jsonify({'error': f'Missing fields:{", ".join(missing_fields)}'}), 400

    new_post = {
        "title": data['title'],
        "content": data['content']
    }
    blog.create_post(new_post)
    return jsonify(new_post), 201

@app.route('/api/posts/<int:id>', methods=['DELETE'])
def delete_post(id):
    post = next((post for post in POSTS if post['id'] == id), None)
    if post:
        POSTS.remove(post)
        return jsonify({'message': f'Post with id {id} deleted successfully'}), 200
    else:
        return jsonify({'error': f'Post with id {id} not found'}), 404



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5002, debug=True)
