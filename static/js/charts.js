//create the drop down selection tool for 
function init() {
  // Grab a reference to the dropdown select element
  var selector = d3.select("#selDataset");
  
  // Use the list of column names to populate the select options
  d3.json("sample.json").then((data) => {
    var date = data.dates;
  
    date.forEach((date) => {
      selector
        .append("option")
        .text(date)
        .property("value", date);
    });
  
    // Use the first date from the list to build the initial plots
    var firstDate = date[0];
    buildCharts(firstDate);
    buildMetadata(firstDate);
  }); 
}
 
// Initialize the dashboard
init();
  
function optionChanged(newDate) {
  // Fetch new data each time a new date is selected
  buildMetadata(newDate);
  buildCharts(newDate);
    
}


// Demographics Panel 
function buildMetadata(date) {
  d3.json("sample.json").then((data) => {
    var metadata = data.gender;
    // Filter the data for the object with the desired date
    var resultArray = metadata.filter(sampleObj => sampleObj.DATE == date);
    var result = resultArray[0];
    // Use d3 to select the panel with id of `#sample-metadata`
    var PANEL = d3.select("#sample-metadata");

    // Use `.html("") to clear any existing metadata
    PANEL.html("");

    // Use `Object.entries` to add each key and value pair to the panel
    // Hint: Inside the loop, you will need to use d3 to append new
    // tags for each key-value in the metadata.
    Object.entries(result).forEach(([key, value]) => {
      PANEL.append("h6").text(`${key.toUpperCase()}: ${value}`);
    });

  });
}

// create the buildChart for data display
function buildCharts(date) {
  //Use d3.json to load and retrieve the gender.json file 
  d3.json("sample.json").then((data) => {
    //Create a variable that holds the samples array. 
    var dates = data.dates
    var unemployed = data.gender;
    //Create a variable that filters the dates for the object with the desired date.
    var resultUnEmployed = unemployed.filter(sampleObj => sampleObj.DATE == date);
    //console.log(resultUnEmployed)
    //Create a variable that filters the dates array for the object with the desired date.
    var sampleDate = data.dates.filter(sampleObj => sampleObj.dates == date);
    //console.log(sampleDate);
    //Create a variable that holds the first date in the array.
    var result = resultUnEmployed[0].DATE;
    console.log(result)
    //Create a variable that holds the first date in the gender array.
    var number = sampleDate[0];

    //Create variables that hold the men and women unemployment rates.
    var men = data.Rate_Men;
    
    var women = data.Rate_Women;

    //Create the men and women trace for the line graph. 
//     //var menTrace = [{
//     //  type: 'scatter',
//     //  x: number,
//     //  y: men,
// //mode: 'lines',
//     //  line: {
//         dash: 'dashdot',
//         width: 4
//       }
//     }];

//     var womenTrace = [{
//       type: 'scatter',
//       x: number,
//       y: women,
//       mode: 'lines',
//       line: {
//         dash: 'solid',
//         width: 4
//       }
//     }];

    // var trace = [menTrace, womenTrace]

    // // 9. Create the layout for the bar chart. 
    // var lineLayout = {
    //   title: "Unemployment By Gender",
    //   hovermode: 'closest',
    //   xaxis: result,
    //   yaxis: {
    //     range: [0, 10]
    //   }
    // };
    // //Use Plotly to plot the data with the layout. 
    // Plotly.newPlot("line", trace, lineLayout);

    var menRate = {
      x: number,
      y: men,
    };
    var womenRate = {
      x: number,
      y: women,
    };
    var data = [menRate, womenRate];
    var layout = {
      title: "Unemployment by Gender",
      xaxis: dates,
      yaxis: [0,1,2,3,4,5,6]
    };
    Plotly.newPlot('line', data, layout);
  
  });
}

