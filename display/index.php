<?
$ch = curl_init();

curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false); // TODO: fixme

curl_setopt($ch, CURLOPT_URL, "https://" . $_SERVER['SERVER_NAME'] . ":" . $_SERVER['SERVER_PORT'] . "/intranet/weather/api/findrecent.py?sensor=buero");
$response_buero = curl_exec($ch);
$data_buero = json_decode($response_buero, true);

$abs_feuchte_buero = (((0.000002*pow($data_buero['temperature'],4))+(0.0002*pow($data_buero['temperature'],3))+(0.0095*pow($data_buero['temperature'],2))+(0.337*$data_buero['temperature'])+4.9034)*$data_buero['humidity'])/100;

curl_setopt($ch, CURLOPT_URL, "https://" . $_SERVER['SERVER_NAME'] . ":" . $_SERVER['SERVER_PORT'] . "/intranet/weather/api/findrecent.py?sensor=aussen");
$response_aussen = curl_exec($ch);
$data_aussen = json_decode($response_aussen, true);

$abs_feuchte_aussen = (((0.000002*pow($data_aussen['temperature'],4))+(0.0002*pow($data_aussen['temperature'],3))+(0.0095*pow($data_aussen['temperature'],2))+(0.337*$data_aussen['temperature'])+4.9034)*$data_aussen['humidity'])/100;

curl_close($ch);
?>

<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link rel="stylesheet" href="assets/css/bootstrap.min.css" />
    <title>Weather Buero</title>
    <style type="text/css">
        body {
            background-color: #e0ebeb;
        }
        .btn-circle {
          width: 30px;
          height: 30px;
          text-align: center;
          padding: 6px 0;
          font-size: 12px;
          line-height: 1.428571429;
          border-radius: 15px;
        }
        .btn-circle.btn-xl {
          width: 70px;
          height: 70px;
          padding: 10px 16px;
          font-size: 24px;
          line-height: 1.33;
          border-radius: 35px;
        }
    </style>
  </head>
  <body>

    <div class="container-fluid">
        <table style="width: 100%;font-family: sans-serif" border="0">
        <tbody>
        <tr>
        <td>
        <p style="font-size: 36px; color: #ff8566; text-align: center"><? echo number_format($data_buero['temperature'], 1); ?> &deg;C</p>
        <p style="font-size: 34px; color: #99ccff; text-align: center"><? echo number_format($data_buero['humidity'], 1); ?> &#37;</p>
        </td>
        <td>
        <p style="font-size: 36px; color: #ff8566; text-align: center"><? echo number_format($data_aussen['temperature'], 1); ?> &deg;C</p>
        <p style="font-size: 34px; color: #99ccff; text-align: center"><? echo number_format($data_aussen['humidity'], 1); ?> &#37;</p>
        </td>
        </tr>
        <tr>
        <td colspan="2" line-height="50px" style="text-align: center">
            L&uuml;ftung ok ?
            <button type="button" class="btn btn-<? if($abs_feuchte_aussen < $abs_feuchte_buero) echo("success"); else echo("danger"); ?> btn-circle btn-xl"></button>
        </td>
        </tr>
        </tbody>
        </table>
        <p>&nbsp;</p>
      </div>

  </body>
</html>
