""" Example illustrating using pyno to provide a shallow wrapper over chart.js using a custom """

from pyno import HTML as H, browser_preview
import json


class Chart(H):
    """ Custom element which creates the canvas and script required to generate the chart.js chart"""
    def __init__(self, plotstruct, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.plotstruct = plotstruct

    def construct(self, *args, **kwargs):
        return H.div(H.canvas(id='myChart', width=400, height=400), 
                H.script(f'''new Chart(document.getElementById("myChart").getContext('2d'), {json.dumps(self.plotstruct)});'''),
                     style="width:400px;height:400px;")


plotstruct = {'type': 'bar',
              'data': {
                  'labels': ["Red", "Blue", "Yellow", "Green", "Purple", "Orange"],
                  'datasets': [{
                      'label': '# of Votes',
                      'data': [12, 19, 3, 5, 2, 3],
                      'backgroundColor': [
                          'rgba(255, 99, 132, 0.2)',
                          'rgba(54, 162, 235, 0.2)',
                          'rgba(255, 206, 86, 0.2)',
                          'rgba(75, 192, 192, 0.2)',
                          'rgba(153, 102, 255, 0.2)',
                          'rgba(255, 159, 64, 0.2)'
            ], 'borderColor': [
                          'rgba(255,99,132,1)',
                          'rgba(54, 162, 235, 1)',
                          'rgba(255, 206, 86, 1)',
                          'rgba(75, 192, 192, 1)',
                          'rgba(153, 102, 255, 1)',
                          'rgba(255, 159, 64, 1)'
            ],
                      'borderWidth': 1
                  }]
              },
              'options': dict(scales={'yAxes': [{'ticks:': {'beginAtZero': True}}]})
              }

browser_preview(
    H.html(
        H.head(
            H.script(src="resources/node_modules/chart.js/dist/Chart.min.js"),
            H.style('div {font-weight:bold;font-size:22;}')),
        H.body(H.div('Hello there! :)'), H.Chart(plotstruct))
    )
)
