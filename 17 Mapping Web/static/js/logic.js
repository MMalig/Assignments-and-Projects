// Store API link
var link = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson"

function markerSize(mag) {
  return mag * 20000;
}

function markerColor(mag) {
  if (mag <= 1) {
      return "#8bff00";
  } else if (mag <= 2) {
      return "#cbff00";
  } else if (mag <= 3) {
      return "#fff300";
  } else if (mag <= 4) {
      return "#ffb300";
  } else if (mag <= 5) {
      return "#ff7300";
  } else {
      return "#ff3300";
  };
}

// Execute request to the query URL
d3.json(link, function(data) {
  createFeatures(data.features);
});

function createFeatures(earthquakeData) {

  var earthquakes = L.geoJSON(earthquakeData, {
  // Run fucntion for each feature in the array
  // Define popup for each data point
 onEachFeature : function (feature, layer) {

    layer.bindPopup("<h2>" + feature.properties.place +
      "</h2><h3> Magnitude: " + feature.properties.mag + "</h3>" + "<hr><h5>" + new Date(feature.properties.time) + "</h5>")
    },     pointToLayer: function (feature, latlng) {
      return new L.circle(latlng,
        {radius: markerSize(feature.properties.mag),
        fillColor: markerColor(feature.properties.mag),
        fillOpacity: 0.6,
        stroke: "true",
        color: "black",
    })
  }
  });
    


  // Send earthquakes layer to the createMap function
  createMap(earthquakes);
}

function createMap(earthquakes) {

  // Define lightmap layer for background
  var lightmap = L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/light-v9/tiles/256/{z}/{x}/{y}?access_token={accessToken}", {
    attribution: "Map data &copy; <a href=\"http://openstreetmap.org\">OpenStreetMap</a> contributors, <a href=\"http://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"http://mapbox.com\">Mapbox</a>",
    maxZoom: 18,
    id: "mapbox.light",
    accessToken: API_KEY
  });

  // Create a baseMaps object to hold the lightmap layer
  var baseMaps = {
    "Light Map": lightmap
  };

  // Create an overlayMaps object to hold the earthquakes layer
  var overlayMaps = {
    "Earthquakes": earthquakes
  };

  // Create the map object with options
  var map = L.map("map", {
    center: [38.57853542647338,-97.580078125],
    zoom: 5,
    layers: [lightmap, earthquakes]
  });

  // Create a layer control, pass in the baseMaps and overlayMaps. Add the layer control to the map
  L.control.layers(baseMaps, overlayMaps, {
    collapsed: false
  }).addTo(map);

  var legend = L.control({position: 'bottomright'});

  legend.onAdd = function () {
  
      var div = L.DomUtil.create('div', 'info legend'),
          magnitudes = [0, 1, 2, 3, 4, 5];
  
      for (var i = 0; i < magnitudes.length; i++) {
          div.innerHTML +=
              '<i style="background:' + markerColor(magnitudes[i] + 1) + '"></i> ' + 
      + magnitudes[i] + (magnitudes[i + 1] ? ' - ' + magnitudes[i + 1] + '<br>' : ' + ');
      }
  
      return div;
  };
  
  legend.addTo(map);

}