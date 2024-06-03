google.charts.load('current', {packages:["orgchart"]});
google.charts.setOnLoadCallback(drawChart);

function drawChart() {
  var data = new google.visualization.DataTable();
  data.addColumn('string', 'Name');
  data.addColumn('string', 'Manager');
  data.addColumn('string', 'ToolTip');

  // For each orgchart box, provide the name, manager, and tooltip to show.
  data.addRows([
    [{'v':'Keith', 'f':'Keith<div style="color:red; font-style:italic">President</div>'},
     '', 'The President'],
    [{'v':'Dorothy', 'f':'Dorothy<div style="color:red; font-style:italic">CFO</div>'},
     'Keith', 'The Chief Financial Officer'],
     [{'v':'Jason', 'f':'Jason<div style="color:red; font-style:italic">CTO</div>'},
     'Keith', 'The Chief Technical Officer'],
    ['Josh', 'Dorothy', ''],
    ['Jon', 'Keith', ''],
    ['Gerry', 'Keith', ''],
  ]);

  // Create the chart.
  var chart = new google.visualization.OrgChart(document.getElementById('orgchart'));
  // Draw the chart, setting the allowHtml option to true for the tooltips.
  chart.draw(data, {'allowHtml':true,'size': 'large'});
}