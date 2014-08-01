<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>EOLRepair</title>
<link href="style.css" rel="stylesheet" type="text/css" />
</head>
<body>
<img src="logo.png" id="logo" width="400" height="138" />
<div id="menubar">
  <ul>
    <a href="index.html">Home</a>
  </ul>
  <ul>
    <a href="repair.php">Repair Request</a>
  </ul>
  <ul>
    <a href="what.html">What we do</a>
  </ul>
  <ul>
    <a href="about.html">About us</a>
  </ul>
</div>
<div id="wrapper_main">
  <h2>Repair Request</h2>
  <?php
	//This won't work until the php.ini is updated with smtp and source emails
	if ($_GET['status'] || $_POST['name']) {
		$response = mail($_POST['email'],"Repair request from ".$_POST['email']);
		?>
  <p id="status">Repair request has been submitted! Thank you!<br />
    (This won't work until the php.ini is updated with smtp and source emails)<br />
    In the meantime, <a href="requests_sent.txt" target="_blank">click here to see entries</a></p>
  <?php
		$f=fopen("requests_sent.txt","a+");
		fwrite($f,$_POST['name']." sent a message from ".$_POST['email']." saying:\n".$_POST['body']."\n\n\	n");
	}
?>
  <p>Here you can give us information about your problem and the related hardware. We'll do our best to get back to you within the next business day (typically 24 hours). If you have problems, or would prefer to contact us via phone, feel free to call us at [eolrepair_phone_number] during our business hours (9am-5pm M-F). </p>
  <div id="repair_form">
    <form action="repair.php" method="post">
      <p>Name:
        <input name="name" type="text" size="50" />
      </p>
      <p>Email:
        <input name="email" type="text" size="50" />
      </p>
      <p>Tell us about your problem. Be sure to include details like the product numbers and server type.<br />
        <textarea name="body" cols="75" rows="10"></textarea>
      </p>
      <input name="submit" type="submit" />
      <br />
    </form>
  </div>
</div>
<div id="footer"> Copyright © 2014 eolrepair.com.<br />
  All rights reserved. </div>
</body>
</html>
