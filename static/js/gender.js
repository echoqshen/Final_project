Plotly.d3.csv('Resources/gender.csv', function(err, rows){
    function unpack(rows, key) {
        return rows.map(function(row) {return row[key]; });
    }
  
    var trace1 = {
        type: "scatter",
        mode: "lines",
        name: "Men",
        x: unpack(rows, 'DATE'),
        y: unpack(rows, 'Rate_Men'),
        line: {
        color: '#FF8700',
        width: 3,
        shape: "spline"
        }
    }
  
    var trace2 = {
        type: "scatter",
        mode: "lines",
        name: "Women",
        x: unpack(rows, 'DATE'),
        y: unpack(rows, 'Rate_Women'),
        line: {
        color: '#81827F',
        width: 3,
        shape: "spline"
        }
    }
  
    var data = [trace1, trace2];
  
    var layout = {
        title: "Unemployment by Gender",
        xaxis: {
            title: 'Year'
        },
        yaxis: {
            title: 'Percentage'
        }

    };
  
  
    Plotly.newPlot('gender', data, layout);
  
})
  