<?php

  require('getData.php');

  $result = array();
  array_push($result, array('day','temperature','humidity'));
  $data = Temperature::getData("buero", "Today");
  foreach ($data as $value) {
    array_push($result, array(date("H:i", strtotime($value['measuredate'])), $value['temperature'], $value['humidity']));
  }

  echo json_encode($result);

?>

