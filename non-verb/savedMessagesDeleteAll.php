<?php
require "savedMessagesConnect.php";

$id = $_GET['id'];
echo $id;

$query = "DELETE FROM `messages`";
if ($result = mysqli_query($link, $query)) {
    header("Location:https://starlight9229.github.io/non-verb/");
    echo $query;
} else {
    echo "bad";
}
