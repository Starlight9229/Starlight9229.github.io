<?php
require "savedMessagesConnect.php";
$error = "";

if (isset($_POST['messages'])) {
    $message = $_POST['messages'];
    echo  $message;
    $valid = true;
    if(!$message){
        $error = "Please write a message";
        $valid = false;
    }
    if(strlen($message) > 150){
        $error = "Message must be no more than 100 characters long";
        $valid = false;
    }
    if($valid){
    $message_clean = mysqli_real_escape_string($link, $message);
    $query = "INSERT INTO `messages`(`message`) VALUES ('$message_clean')";
    if($result = mysqli_query($link, $query)) {
        $error = "Success!";
    }else{
        $error = "Failure";
    }
}
}
?>
<html>

<head>
    <title>Starlight's non-verbal writing page</title>
    <link rel="stylesheet" href="http://citadel.ghs.vic.edu.au/CAL0022/non-verb/bootstrap-non-verb.css">
    <link rel="stylesheet" href="http://citadel.ghs.vic.edu.au/CAL0022/non-verb/style-non-verb.css">
</head>

<body>

    <form method="POST">
        <div class="indent">
            <label for="writtentext" class="form-label mt-4">Write here:</label>
            <div class="input-group mb-3">
                <input type="text" class="form-control darkbluelight-dark-gradient-bg-only" id="writtentext" value="" name="messages" required maxlength="100"></input>
                <button type="submit" class="btn btn-custom-save" id="button-addon2">Save Message</button>
            </div>
        </div>

    </form>
    <?php echo $error; ?>
</body>
</html>