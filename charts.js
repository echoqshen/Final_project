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