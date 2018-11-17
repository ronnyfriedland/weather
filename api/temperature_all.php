<html>
  <head>
    <title>Raspberry Weather</title>
    <script language="javascript" type="text/javascript" src="/intranet/js/jquery.min.js"></script></script>
    <script type="text/javascript" src="/intranet/js/google-jsapi.js"></script>
    <script type="text/javascript">
      $.noConflict();
      google.load("visualization", "1", {packages: ["corechart"]});
      
      function doStats() {
        var statisticsOverview = {
          init: function() {
            this.drawWeatherTodayChart();
            this.drawWeatherWeekChart();
            this.drawWeatherMonthChart();
          },
          drawWeatherTodayChart: function() {
            var jsonData = $.ajax({
              url: "/intranet/weather/getDataToday.php",
              dataType: "json",
              async: false
            }).responseText;
      
            var obj = JSON.parse(jsonData);
      
            var options = {
              width: 800, height: 300,
              title: 'Today',
              legend : 'top',
              series: {0: {targetAxisIndex:0},
               1:{targetAxisIndex:1}
              },
              colors: ['#db3011', '#0128d8']
            };
            var id = 'chart_div_today';
            this.drawLineChart(obj, options, id);
          },
          drawWeatherWeekChart: function() {
            var jsonData = $.ajax({
              url: "/intranet/weather/getDataWeek.php",
              dataType: "json",
              async: false
            }).responseText;
      
            var obj = JSON.parse(jsonData);
      
             var options = {
               width: 800, height: 300,
               title: 'Last Week',
               legend : 'top',
               series: {0: {targetAxisIndex:0},
                1:{targetAxisIndex:1}
               },
               colors: ['#db3011', '#0128d8']
             };
             var id = 'chart_div_week';
             this.drawLineChart(obj, options, id);
          },
          drawWeatherMonthChart: function() {
            var jsonData = $.ajax({
              url: "/intranet/weather/getDataMonth.php",
              dataType: "json",
              async: false
            }).responseText;
      
            var obj = JSON.parse(jsonData);
      
            var options = {
              width: 800, height: 300,
              title: 'Last Month',
              legend : 'top',
              series: {0: {targetAxisIndex:0},
               1:{targetAxisIndex:1}
              },
              colors: ['#db3011', '#0128d8']
            };
            var id = 'chart_div_month';
            this.drawLineChart(obj, options, id);
          },
          drawLineChart: function(data, options, id) {
            var chartData = google.visualization.arrayToDataTable(data);
      
            var chart = new google.visualization.LineChart(document.getElementById(id));
            chart.draw(chartData, options);
          }
        };
        statisticsOverview.init();
      }
      google.setOnLoadCallback(doStats);
    </script>
  </head>
  <body>
    <center>
      <div id="chart_div_today"></div><br/><br/>
      <div id="chart_div_week"></div><br/><br/>
      <div id="chart_div_month"></div><br/><br/>
    </center>
  </body>
</html>

