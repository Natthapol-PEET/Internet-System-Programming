<?php
include 'dbconnect.php';
$email = $_POST['email'];
$fullname = $_POST['fullname'];
$address = $_POST['address'];

$sqlcheck = "SELECT * FROM  registered_users WHERE email = '$email'";
$result = mysqli_query($conn, $sqlcheck) or die(mysqli_error($conn));
$num = mysqli_num_rows($result);
if ($num !== 0) {
    echo "<script>";
    echo "alert('อีเมลนี้ได้ลงทะเบียนแล้ว!!');";
    echo "window.location='greeting.php';";
    echo "</script>";

} else {
    $sql = "INSERT INTO registered_users(email,fullname,address) VALUES('$email','$fullname','$address')";
    $result = mysqli_query($conn, $sql) or die("Error in query: $sql" . mysqli_error($conn));

    if ($result) {
        echo "<script type='text/javascript'>";
        echo "alert ('ลงทะเบียนสำเร็จ');";
        echo "window.location='greeting.php';";
        echo "</script>";
    } else {
        echo "<script type='text/javascript'>";
        echo "alert ('ลงทะเบียนไม่สำเร็จ!');";
        echo "window.location='index.html';";
        echo "</script>";
    }
}
mysqli_close($conn);
?>