<?php
$username = $_POST["username"];
$password = $_POST["password"];
$email = $_POST["email"];
$user = $_POST["user"];
$country = $_POST["country"];

if (!empty($username) || !empty($password) || !empty($email) || !empty($user) || !empty($country))
{
    #Create a localhost db on your system and if needed, change the values 
    $host = "localhost";
    $dbUsername = "root";
    $dbPassword = "";
    $dbName = "test";

    $connection = mysqli_connect($host,$dbUsername,$dbPassword,$dbName);

    if (mysqli_connect_error())
    {
        die("Connection Error(".mysqli_connect_errno().")".mysqli_connect_error());
    }
    else
    {
        $SELECT = "SELECT email FROM register WHERE email = ? LIMIT 1";
        $INSERT = "INSERT INTO register (username,password,email,user,country) VALUES (?,?,?,?,?)";

        $statement = $connection->prepare($SELECT);
        $statement->bind_param("s",$email);
        $statement->execute();
        $statement->bind_result($email);
        $statement->store_result();
        $rownum = $statement->num_rows;

        if ($rownum == 0)
        {
            $statement->close();

            $statement = $connection->prepare($INSERT);
            $statement->bind_param("sssss",$username,$password,$email,$user,$country);
            $statement->execute();
            echo ("New record inserted successfully");
        }
        else
        {
            echo("This email already exists");
        }
        $statement->close();
        $connection->close();
    }
}
else
{
    echo("All fields are OK");
    die();
}
?>