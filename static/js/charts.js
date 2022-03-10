//create the drop down selection tool for 

function init() {
  // Grab a reference to the dropdown select element
  var selector = d3.select("#selDataset");
  
  // Use the list of column names to populate the select options
  d3.json("gender.json").then((data) => {
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
  d3.json("gender.json").then((data) => {
    var gender = data.gender;
    // Filter the data for the object with the desired date
    var resultArray = gender.filter(sampleObj => sampleObj.DATE == dates);
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
