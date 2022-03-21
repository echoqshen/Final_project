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

// create a graph for the education csv
Plotly.d3.csv('Resources/education.csv', function(err, rows){
    function unpack(rows, key) {
        return rows.map(function(row) {return row[key]; });
    }
  
    var trace1 = {
        type: "scatter",
        mode: "lines",
        name: "High School",
        x: unpack(rows, 'DATE'),
        y: unpack(rows, 'Rate_High_School'),
        line: {
        color: 'blue',
        width: 3,
        shape: "spline"
        }
    }
  
    var trace2 = {
        type: "scatter",
        mode: "lines",
        name: "Bachelors",
        x: unpack(rows, 'DATE'),
        y: unpack(rows, 'Rate_Bachelors'),
        line: {
        color: 'red',
        width: 3,
        shape: "spline"
        }
    }

    var trace3 = {
        type: "scatter",
        mode: "lines",
        name: "Masters",
        x: unpack(rows, 'DATE'),
        y: unpack(rows, 'Rate_Masters'),
        line: {
        color: 'yellow',
        width: 3,
        shape: "spline"
        }
    }

    var trace4 = {
        type: "scatter",
        mode: "lines",
        name: "Doctorate",
        x: unpack(rows, 'DATE'),
        y: unpack(rows, 'Rate_Doctoral'),
        line: {
        color: 'green',
        width: 3,
        shape: "spline"
        }
    }
  
    var data = [trace1, trace2, trace3, trace4];
  
    var layout = {
        title: "Unemployment by Education",
        xaxis: {
            title: 'Year'
        },
        yaxis: {
            title: 'Percentage'
        }

    };
  
  
    Plotly.newPlot('education', data, layout);
  
})


//create a graph for race csv
Plotly.d3.csv('Resources/race.csv', function(err, rows){
    function unpack(rows, key) {
        return rows.map(function(row) {return row[key]; });
    }
  
    var trace1 = {
        type: "scatter",
        mode: "lines",
        name: "Asian",
        x: unpack(rows, 'DATE'),
        y: unpack(rows, 'Rate_Asian'),
        line: {
        color: 'blue',
        width: 3,
        shape: "spline"
        }
    }
  
    var trace2 = {
        type: "scatter",
        mode: "lines",
        name: "Black",
        x: unpack(rows, 'DATE'),
        y: unpack(rows, 'Rate_Black'),
        line: {
        color: 'red',
        width: 3,
        shape: "spline"
        }
    }

    var trace3 = {
        type: "scatter",
        mode: "lines",
        name: "White",
        x: unpack(rows, 'DATE'),
        y: unpack(rows, 'Rate_White'),
        line: {
        color: 'yellow',
        width: 3,
        shape: "spline"
        }
    }

    var trace4 = {
        type: "scatter",
        mode: "lines",
        name: "Latino",
        x: unpack(rows, 'DATE'),
        y: unpack(rows, 'Rate_Latino'),
        line: {
        color: 'green',
        width: 3,
        shape: "spline"
        }
    }
  
    var data = [trace1, trace2, trace3, trace4];
  
    var layout = {
        title: "Unemployment by Race",
        xaxis: {
            title: 'Year'
        },
        yaxis: {
            title: 'Percentage'
        }

    };
  
  
    Plotly.newPlot('race', data, layout);
  
})

//create a graph for the national unemployment rate
Plotly.d3.csv('Resources/overall_monthly.csv', function(err, rows){
    function unpack(rows, key) {
        return rows.map(function(row) {return row[key]; });
    }
  
    var trace1 = {
        type: "scatter",
        mode: "lines",
        name: "National",
        x: unpack(rows, 'DATE'),
        y: unpack(rows, 'Rate_Overall'),
        line: {
        color: 'green',
        width: 3,
        shape: "spline"
        }
    }
  
    var data = [trace1];
  
    var layout = {
        title: "National Overall Unemployment",
        xaxis: {
            title: 'Year'
        },
        yaxis: {
            title: 'Percentage'
        }

    };
  
  
    Plotly.newPlot('national', data, layout);
  
})