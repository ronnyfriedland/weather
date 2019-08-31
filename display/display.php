<?
$ch = curl_init();

curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, false); // TODO: fixme
curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false); // TODO: fixme

curl_setopt($ch, CURLOPT_URL, "https://" . $_SERVER['SERVER_NAME'] . ":" . $_SERVER['SERVER_PORT'] . "/intranet/weather/api/checkhumidity.py?sensor1=buero&sensor2=aussen");
$response = curl_exec($ch);

$data = json_decode($response, true);

$lueftung_ok = $data['ok'];

curl_close($ch);
?>

<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.5.0/css/all.css" integrity="sha384-B4dIYHKNBt8Bc12p+WXckhzcICo0wtJAoU8YZTY5qE0Id1GSseTk6S+L3BlXeVIU" crossorigin="anonymous">
    <title>Weather Buero</title>
    <style type="text/css">
        body {
            background-color: #505050;
        }
    </style>
  </head>
  <body>

    <div class="container rounded">
      <div class="row ml-1">
        <div class="col text-light p-3">
          Buero
        </div>
        <div class="col text-light p-3">
          Aussen
        </div>
      </div>
      <div class="row ml-1">
        <div class="col text-light p-3">
          Temperatur:
          <span class="display-4 strong"><? echo number_format($data['buero']['temperature'], 1); ?> &deg;C</span>
        </div>
        <div class="col text-light p-3">
          Temperatur:
          <span class="display-4 strong"><? echo number_format($data['aussen']['temperature'], 1); ?> &deg;C</span>
        </div>
      </div>
      <div class="row ml-1">
        <div class="col text-warning p-3">
          Luftfeuchte:
          <span class="display-4 strong"><? echo number_format($data['buero']['humidity'], 1); ?> &#37;</span>
        </div>
        <div class="col text-warning p-3">
          Luftfeuchte:
          <span class="display-4 strong"><? echo number_format($data['aussen']['humidity'], 1); ?> &#37;</span>
        </div>
      </div>
      <div class="row rounded justify-content-center align-self-center">
        <div class="col" style="font-size:10em;">
          <div class="text-center p-3 <? if($lueftung_ok) echo("bg-success"); else echo("bg-danger"); ?>"><i class="fas <? if($lueftung_ok) echo("fa-check-circle"); else echo("fa-ban"); ?>"></i></div>
        </div>
      </div>
    </div>

  </body>
</html>
