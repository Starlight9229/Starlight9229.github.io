<?php
require "savedMessagesConnect.php";

$id = $_GET['id'];
echo $id;

$query = "DELETE FROM `messages` WHERE `id` = '$id'";
if ($result = mysqli_query($link, $query)) {
    header("https://starlight9229.github.io/CAL0022/non-verb/");
    echo $query;
} else {
    echo "bad";
}
