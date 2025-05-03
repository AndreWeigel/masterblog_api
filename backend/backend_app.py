from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
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
    return jsonify(POSTS)


@app.route('/api/posts', methods=['POST'])
def add_post():
    data = request.get_json()

    required_fields = ['title', 'content']
    missing_fields = [field for field in required_fields if field not in data]

    if missing_fields:
        return jsonify({'error': f'Missing fields:{", ".join(missing_fields)}'}), 400

    new_post = {
        "id": POSTS[-1]['id'] + 1 if POSTS else 1,
        "title": data['title'],
        "content": data['content']
    }
    POSTS.append(new_post)
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
