<?php
    $email = $_POST['email'];
    $full_name = $_POST['full_name'];
    $address = $_POST['address'];

    print("Register success for $email at $full_name in $address");

    $servername = "localhost";
    $username = "PEET";
    $password = "10042541";

    // Create connection
    $conn = new mysqli($servername, $username, $password);

    // Check connection
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }
    echo "Connected successfully";
?>