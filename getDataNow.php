<?php

  require('getData.php');
  
  echo json_encode(Temperature::getData(urlencode($_GET['sensor']), "Now"));

?>

