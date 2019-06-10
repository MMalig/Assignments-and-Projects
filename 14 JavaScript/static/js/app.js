// from data.js
var tableData = data;

// Statements to declare variables
var columns = ["datetime", "city", "state", "country", "shape", "durationMinutes", "comments"]
var dateSelect = d3.select("#datetime");
var tbody = d3.select("tbody");
var filterButton = d3.select("#filter-btn");

var populate = (inputData) => {inputData.forEach(record => {
    var row = tbody.append("tr");
    columns.forEach(column => row.append("td").text(record[column])
    )
  });
}

//Populate table with tableData
populate(tableData);

// Filter by datetime input field value
filterButton.on("click", () => {d3.event.preventDefault();
  var inputDate = dateSelect.property("value").trim();
  var filterDate = tableData.filter(tableData => tableData.datetime === inputDate);
  console.log(filterDate)

  // Populate table with filtered tableData
  tbody.html("");

  let response = {
    filterDate
  }

  if (response.filterDate.length !== 0) {
    populate(filterDate);
  }
    else {
      tbody.append("tr").append("td").text("Selected date is not available"); 
    }
})
