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
    success, result = blog.get_all_posts()
    if success:
        return jsonify(result), 200
    else:
        return jsonify({'error': result}), 400


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
    success, result = blog.create_post(new_post)
    if success:
        POSTS.append(new_post)
        return jsonify(result), 201
    else:
        return jsonify({'error': result}), 400


@app.route('/api/posts/<int:id>', methods=['DELETE'])
def delete_post(id):
    blog = PostService()
    success, result = blog.delete_post(id)
    if success:
        return jsonify({'message': result}), 200
    else:
        return jsonify({'error': result}), 404

@app.route('/api/posts/<int:id>', methods=['PUT'])
def update_post(id):
    blog = PostService()
    data = request.get_json()
    success, result = blog.update_post(id, data)
    if success:
        return jsonify(result), 200
    else:
        return jsonify({'error': result}), 404

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5002, debug=True)
