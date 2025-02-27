<?php

$servername = "localhost";
$username = "CAL0022";
$password = "CAL0022";
$database = "CAL0022";
//create connection
$link  = new mysqli($servername, $username, $password, $database);

//check connection
if ($link->connect_error) {
    die("connection failed: " . $link->connect_error);
} else {
}
