<?php
require "savedMessagesConnect.php";
$error = "";

if (isset($_POST['messages'])) {
    $message = $_POST['messages'];
    $valid = true;
    if (!$message) {
        $error = "Please write a message";
        $valid = false;
    }
    if (strlen($message) > 152) {
        $error = "Message must be no more than 100 characters long";
        $valid = false;
    }
    if ($valid) {
        $message_clean = mysqli_real_escape_string($link, $message);
        $query = "INSERT INTO `messages`(`message`) VALUES ('$message_clean')";
        if ($result = mysqli_query($link, $query)) {
            $error = "Success!";
        } else {
            $error = "Failure";
        }
    }
}
$showTitles = "";
$query = "SELECT * FROM `messages` ORDER BY `id` DESC";
if ($result = mysqli_query($link, $query)) {
    while ($row = $result->fetch_assoc()) {
        $showTitles = $showTitles . "<tr><td>" . $row['message'] . "</td><td><a href = 'savedMessagesDelete.php?id=" . $row['id'] . "'>delete</a></td></tr>";
    }
}


$showTitles = "<table style='background-image: linear-gradient(-90deg, rgb(23, 78, 106), rgb(69, 176, 222)); margin-left: 10px; margin-right: 10px; border-radius: 20px; color: rgb(71, 31, 66); width:97%; min-height:100px; margin-bottom:20px;' cellPadding=10px><thead><th></th><th></th></thead></tbody>" . $showTitles . "</tbody></table>";


?>
<html>

<head>
    <title>Starlight's non-verbal writing page</title>
    <script src="../assets/scripts/bootstrap.bundle.js"></script>
    <link rel="stylesheet" href="../assets/stylesheets/bootstrap-non-verb.css">
    <link rel="stylesheet" href="../assets/stylesheets/style-non-verb.css">
</head>

<body>
    <div w3-include-html="../assets/addons/navbar.html"></div>

    <form method="POST" autocomplete="off">
        <div class="indent">
            <label for="writtentext" class="form-label mt-4">Write here:</label>
            <div class="input-group mb-3">
                <input type="text" class="form-control darkbluelight-dark-gradient-bg-only" id="writtentext" value=""
                    name="messages" required maxlength="152" autofocus></input>
                <button type="submit" class="btn btn-custom-save" id="button-addon2">Save Message</button>
            </div>
            <a href="https://starlight9229.github.io/non-verb/savedMessagesDeleteAll.php"><button type="button"
                    class="btn btn-custom-clear">Clear All Messages</button></a>
        </div>

    </form>

    <div class="cyanlight-dark-gradient">
        <?php echo $showTitles ?>
    </div>
    <script>
    includeHTML();

    function includeHTML() {
        var z, i, elmnt, file, xhttp;
        /* Loop through a collection of all HTML elements: */
        z = document.getElementsByTagName("*");
        for (i = 0; i < z.length; i++) {
            elmnt = z[i];
            /*search for elements with a certain atrribute:*/
            file = elmnt.getAttribute("w3-include-html");
            if (file) {
                /* Make an HTTP request using the attribute value as the file name: */
                xhttp = new XMLHttpRequest();
                xhttp.onreadystatechange = function() {
                    if (this.readyState == 4) {
                        if (this.status == 200) {
                            elmnt.innerHTML = this.responseText;
                        }
                        if (this.status == 404) {
                            elmnt.innerHTML = "Page not found.";
                        }
                        /* Remove the attribute, and call this function once more: */
                        elmnt.removeAttribute("w3-include-html");
                        includeHTML();
                    }
                }
                xhttp.open("GET", file, true);
                xhttp.send();
                /* Exit the function: */
                return;
            }
        }
    }
    </script>
</body>

</html>