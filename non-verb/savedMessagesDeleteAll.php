<?php
require "savedMessagesConnect.php";

$id = $_GET['id'];
echo $id;

$query = "DELETE FROM `messages`";
if ($result = mysqli_query($link, $query)) {
    header("Location:http://citadel.ghs.vic.edu.au/CAL0022/non-verb/");
    echo $query;
} else {
    echo "bad";
}
