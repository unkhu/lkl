<?php
$conn=mysqli_connect("localhost","root","");
if(!$conn)
{
    die("connection unsussefull".mysqli_error($conn));

}else{
    echo" connection was sussefull<br>";
}
$sql = "CREATE DATABASE IF NOT EXISTS dh";
$result = mysqli_query($conn, $sql);
if ($result) { 
    echo "<br>Database created successfully";
} else {
    echo "Database not created: " . mysqli_error($conn);
}

// Create connection
$conn = mysqli_connect("localhost", "root", "", "dh");

if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}

// Create table if not exists
$tableSql = "CREATE TABLE IF NOT EXISTS students (
    student_id INT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    course VARCHAR(50) NOT NULL
)";
mysqli_query($conn, $tableSql);

// INSERT
if (isset($_POST['insert'])) {
    $student_id = $_POST['student_id'];
    $name = $_POST['name'];
    $course = $_POST['course'];

    $sql = "INSERT INTO students (student_id, name, course)
            VALUES ('$student_id', '$name', '$course')";

    if (mysqli_query($conn, $sql)) {
        echo "✅ Record inserted successfully<br>";
    } else {
        echo "❌ Error inserting record: " . mysqli_error($conn);
    }
}

// UPDATE


// DELETE
if (isset($_POST['delete'])) {
    $student_id = $_POST['student_id'];
    $sql = "DELETE FROM students WHERE student_id='$student_id'";
    if (mysqli_query($conn, $sql)) {
        echo "<script>alert('Record deleted successfully');</script>";
    } else {
        echo "<script>alert('Error deleting record: " . mysqli_error($conn) . "');</script>";
    }
}

// FETCH

?>

<!DOCTYPE html>
<html>
<head>
    <title>Student Management</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        form {
            border: 4px double #007bff;
            padding: 15px;
            border-radius: 5px;
            margin-bottom: 20px;
            background-color:rgb(60, 236, 236);
        }
       

    </style>
</head>
<body>
<div class="container mt-4">
    <h2>Insert Student</h2>
    <form method="post">
        <input type="text" name="student_id" class="form-control mb-2" placeholder="Student ID" required>
        <input type="text" name="name" class="form-control mb-2" placeholder="Name" required>
        <input type="text" name="course" class="form-control mb-2" placeholder="Course" required>
        <input type="submit" name="insert" class="btn btn-success" value="Insert">
    </form>


    <h2>Delete Student</h2>
    <form method="post">
        <input type="text" name="student_id" class="form-control mb-2" placeholder="Student ID to Delete" required>
        <input type="submit" name="delete" class="btn btn-danger" value="Delete">
    </form>

</div>
</body>
</html>
