<?php
// Check if the form is submitted
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Retrieve the form data
    $rating = $_POST['rating'];
    $comments = $_POST['comments'];

    // Store the feedback in a database (example using MySQL)
    $servername = 'localhost';
    $username = 'your_username';
    $password = 'your_password';
    $dbname = 'feedback_db';

    // Create a database connection
    $conn = new mysqli($servername, $username, $password, $dbname);

    // Check the connection
    if ($conn->connect_error) {
        die('Connection failed: ' . $conn->connect_error);
    }

    // Insert the feedback into the database
    $sql = "INSERT INTO feedback (rating, comments) VALUES ('$rating', '$comments')";

    if ($conn->query($sql) === TRUE) {
        echo 'Feedback submitted successfully!';
    } else {
        echo 'Error: ' . $sql . '<br>' . $conn->error;
    }

    // Close the database connection
    $conn->close();
}
?>