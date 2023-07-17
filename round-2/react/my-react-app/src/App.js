import React, { useState } from 'react';

const App = () => {
  const [posts, setPosts] = useState([]);
  const [newPost, setNewPost] = useState({ username: '', caption: '', likes: 0, comments: [] });

  const handleInputChange = (event) => {
    setNewPost({ ...newPost, [event.target.name]: event.target.value });
  };

  const handlePostSubmit = (event) => {
    event.preventDefault();
    const updatedPosts = [...posts, newPost];
    setPosts(updatedPosts);
    setNewPost({ username: '', caption: '', likes: 0, comments: [] });
  };

  const handleDeletePost = (index) => {
    const updatedPosts = [...posts];
    updatedPosts.splice(index, 1);
    setPosts(updatedPosts);
  };

  const handleLikePost = (index) => {
    const updatedPosts = [...posts];
    updatedPosts[index].likes += 1;
    setPosts(updatedPosts);
  };

  const handleCommentSubmit = (index, comment) => {
    const updatedPosts = [...posts];
    updatedPosts[index].comments.push(comment);
    setPosts(updatedPosts);
  };

  return (
    <div>
      <h1>Instagram</h1>
      <h2>Create Post</h2>
      <form onSubmit={handlePostSubmit}>
        <input
          type="text"
          name="username"
          placeholder="Username"
          value={newPost.username}
          onChange={handleInputChange}
        />
        <input
          type="text"
          name="caption"
          placeholder="Caption"
          value={newPost.caption}
          onChange={handleInputChange}
        />
        <button type="submit">Create Post</button>
      </form>
      <h2>Posts</h2>
      {posts.map((post, index) => (
        <div key={index}>
          <h3>{post.username}</h3>
          <p>{post.caption}</p>
          <p>Likes: {post.likes}</p>
          <button onClick={() => handleDeletePost(index)}>Delete</button>
          <button onClick={() => handleLikePost(index)}>Like</button>
          <h4>Comments</h4>
          <ul>
            {post.comments.map((comment, commentIndex) => (
              <li key={commentIndex}>{comment}</li>
            ))}
          </ul>
          <form
            onSubmit={(event) => {
              event.preventDefault();
              const comment = event.target.elements.comment.value;
              handleCommentSubmit(index, comment);
              event.target.reset();
            }}
          >
            <input type="text" name="comment" placeholder="Add a comment" />
            <button type="submit">Submit</button>
          </form>
        </div>
      ))}
    </div>
  );
};

export default App;
