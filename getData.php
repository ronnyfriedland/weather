<?php

/**
 * Access temperature values
 */
class Temperature {

  /**
   * Retrieve temperature values
   *
   * @param string $sensor  defines the name of the sensor
   * @param string $period  defines the period of data to be retrieved
   */
  function getData($sensor, $period) {

    $ch = curl_init();

    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, false); // TODO: fixme
    curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false); // TODO: fixme

    if(strpos($period,"Week")!==false) { //last week
        $fromdate = date('Y-m-d H:i:s', strtotime('-7 days'));
        $todate = date('Y-m-d H:i:s', strtotime('+1 day'));

        curl_setopt($ch, CURLOPT_URL, "https://" . $_SERVER['SERVER_NAME'] . ":" . $_SERVER['SERVER_PORT'] . "/intranet/weather/api/find.py?sensor=". $sensor . "&from=" . $fromdate . "&to=" . $todate);
    } else if(strpos($period,"Month")!==false) { //last month
        $fromdate = date('Y-m-d H:i:s', strtotime('-30 days'));
        $todate = date('Y-m-d H:i:s', strtotime('+1 day'));

        curl_setopt($ch, CURLOPT_URL, "https://" . $_SERVER['SERVER_NAME'] . ":" . $_SERVER['SERVER_PORT'] . "/intranet/weather/api/find.py?sensor=". $sensor . "&from=" . $fromdate . "&to=" . $todate);
    } else if(strpos($period,"Today")!==false) { //current day
        $fromdate = date('Y-m-d H:i:s', strtotime('-1 day'));
        $todate = date('Y-m-d H:i:s');

        curl_setopt($ch, CURLOPT_URL, "https://" . $_SERVER['SERVER_NAME'] . ":" . $_SERVER['SERVER_PORT'] . "/intranet/weather/api/find.py?sensor=". $sensor . "&from=" . $fromdate . "&to=" . $todate);
    } else { // current / last value
        curl_setopt($ch, CURLOPT_URL, "https://" . $_SERVER['SERVER_NAME'] . ":" . $_SERVER['SERVER_PORT'] . "/intranet/weather/api/findrecent.py?sensor=". $sensor);
    }

    $response = curl_exec($ch);
    return json_decode($response, true);

  }
}
?>

