google.charts.load("current", {packages:["corechart"]});
    google.charts.setOnLoadCallback(drawChart);
    function drawChart() {
      var data = google.visualization.arrayToDataTable([
        ["Year", "Penetration Rate", { role: "style" } ],
        ["2012", 1.8, "color: blue"],
        ["2013", 3.7, "color: blue"],
        ["2014", 7.3, "color: blue"],
        ["2015", 14, "color: blue"],
        ["2016", 18.5, "color: blue"],
        ["2017", 26.5, "color: blue"],
        ["2018", 36.9, "color: blue"],
        ["2019", 46.5, "color: blue"],
        ["2020", 55.5, "color: blue"],
        ["2025", 65.5, "color: blue"],
        ["2030", 75.5, "color: blue"],
      ]);

      var view = new google.visualization.DataView(data);
      view.setColumns([0, 1,
                       { calc: "stringify",
                         sourceColumn: 1,
                         type: "string",
                         role: "annotation" },
                       2]);

      var options = {
        title: "LED Penetration By Year",
        fontFace: 'Roboto',
        fontSize: 13,
        bar: {groupWidth: "80%"},
        legend: { position: "none" },
        bars: 'veritcal', // Required to position the bars
        chartArea: {left: 50, top: 40, width: '100%'},
        hAxis: {title: 'Percentage Rate (%)', viewMode: 'percent', viewWindow: {min: 0, max: 80}, gridlines: {count: 3}, textStyle: {fontFace: 'Roboto', fontSize: 13, color: '#666', bold: true}},
        vAxis: {title: 'Year', textStyle: {fontFace: 'Roboto', fontSize: 13, color: '#666', bold: true}},
      };
      var chart = new google.visualization.BarChart(document.getElementById("led-bar-chart"));
      chart.draw(view, options);
  }