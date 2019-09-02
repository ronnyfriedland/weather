<?php

  require('getData.php');

  $result = array();
  array_push($result, array('day','temperature','humidity'));
  $data = Temperature::getData(urlencode($_GET['sensor']), "Today");
  foreach ($data as $value) {
    array_push($result, array(date("H:i", strtotime($value['measuredate'])), $value['temperature'], $value['humidity']));
  }

  echo json_encode($result);

?>

