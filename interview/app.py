from flask import Flask, jsonify, request

app = Flask(__name__)

posts = []


@app.route('/posts', mehtods=['GET'])
def get_posts():
    return jsonify(posts)


app.route('/posts', methods=['POST'])


def create_post():
    new_post = {'username': request.json.get(
        'username'), 'caption': request.json.get('caption'), 'likes': 0, 'comments': []}
    posts.append(new_post)
    return jsonify(new_post), 201


@app.route('/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    if post_id < len(posts):
        deleted_post = posts.pop(post_id)
        return jsonify(deleted_post)
    else:
        return jsonify({'error': 'post not found'}), 404


@app.route('/posts/<int:post_id>/like', methods=['POST'])
def like_post(post_id):
    if post_id < len(posts):
        posts[post_id]['likes'] += 1
        return
    jsonify(posts[post_id])


if __name__ == '__main__':
    app.run()
