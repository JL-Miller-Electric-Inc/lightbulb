      google.charts.load('current', {'packages':['corechart']});
      google.charts.setOnLoadCallback(drawChart);

      function drawChart() {

        var data = google.visualization.arrayToDataTable([
          ['Manfacturer', 'Market Share'],
          ['Tesla', 56.2],
          ['Ford',   6.7],
          ['Merceds-Benz',  3.9],
          ['Rivian', 3.8],
          ['Hyundai',5.0],
          ['Chevrolet',	5.8],
          ['Kia',      2.3],
          ['BMW', 1.8],
          ['Volkswagen',  3.5],
          ['Cadillac',0.8],
          ['Nissan', 1.9],
          ['Audi',	2.0],
          ['Volvo', 1.1],
          ['Porsche', 0.7],
          ['Toyota', 0.9],
          ['GMC', 0.3],
          ['Lucid', 0.5],
          ['Lexus', 0.5],
          ['Subaru',0.8],
          ['Genesis', 0.6],
         ['Polestar', 0.6], 
        ]);

        var options = {
          title: 'Year 2023 - EV Market Share Analysis',
          chartArea: {left:20, top:30, width:'100%'},
          fontFace: 'Arial',
          legend: {position: 'right', align: 'end', maxLines: 3, textStyle: {fontSize: 12}},
          titleTextStyle: { color: '#2e2e2e', fontSize: 12, bold: true },
          sliceVisibilityThreshold: .03
        };

        var chart = new google.visualization.PieChart(document.getElementById('piechart'));

        chart.draw(data, options);
      }