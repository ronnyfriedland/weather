<?php

  require('getData.php');
  
  echo json_encode(Temperature::getData("buero", "Now"));

?>

