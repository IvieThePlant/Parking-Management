mapboxgl.accessToken = 'pk.eyJ1IjoiYm9iYnJvIiwiYSI6ImNtbW1sdWJrbTJjOTQycW9rbmt3bnlheDcifQ.C2hSvGbFdfvicyO69r0GmA'

// Global map object
const map = new mapboxgl.Map({
    container: 'map',
    style: 'mapbox://styles/mapbox/standard', // Use the standard style for the map
    projection: 'globe', // display the map as a globe
    zoom: 17, // initial zoom level, 0 is the world view, higher values zoom in
    center: [-93.24076, 44.967375] // center the map on this longitude and latitude
});

// Easiest to add market objects via this data array
// https://docs.mapbox.com/mapbox-gl-js/guides/add-your-data/markers/
const locations = [
  {
    coordinates: [-93.242878, 44.964812],
    name: 'Lot A',
    spotsTaken: 10,
    totalSpots: 30
  },
  {
    coordinates: [-93.241709, 44.964796],
    name: 'Lot B',
    spotsTaken: 8,
    totalSpots: 20
  },
  {
    coordinates: [-93.243197, 44.965065],
    name: 'Lot D',
    spotsTaken: 23,
    totalSpots: 30

  },
  {
    coordinates: [-93.242081, 44.965318],
    name: 'Lot E',
    spotsTaken: 5,
    totalSpots: 20
  },
  {
    coordinates: [-93.242024, 44.967266],
    name: 'Lot G',
    spotsTaken: 18,
    totalSpots: 30,
  },
  {
    coordinates: [-93.239643, 44.966379],
    name: 'Lot J',
    spotsTaken: 20,
    totalSpots: 30
  },
  {
    coordinates: [-93.238787,44.966341],
    name: 'Lot K',
    spotsTaken: 12,
    totalSpots: 20
  },
  {
    coordinates: [-93.237113, 44.965077],
    name: 'Lot L',
    spotsTaken: 15,
    totalSpots: 60
  },
  // ... more locations
];

map.addControl(new mapboxgl.NavigationControl());

// Functions should be in asynchronous func or it may not be called
map.on('load', () => {
    locations.forEach(location => {
        new mapboxgl.Marker({color: setColorBasedOnSpots(location.spotsTaken, location.totalSpots)})
          .setLngLat(location.coordinates)
          .setPopup(new mapboxgl.Popup().setHTML(`<h3>${location.name}</h3>
            <h3>${location.spotsTaken}/${location.totalSpots} spots taken</h3>
            <button type="button" id="myButton">Park Here</button>`))
          .addTo(map);
    });
});

function setColorBasedOnSpots(spotsTaken, totalSpots) {
    const ratio = spotsTaken / totalSpots;
    if (ratio < 0.5) {
        return "#00FF00"; // Green
    } else if (ratio < 0.8) {
        return "#FFFF00"; // Yellow
    } else {
        return "#FF0000"; // Red
    }
}
