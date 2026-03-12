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
    coordinates: [-93.243197, 44.965065],
    name: 'Lot D'
  },
  {
    coordinates: [-93.241709, 44.964796],
    name: 'Unknown Lot'
  },
  {
    coordinates: [-93.237113, 44.965077],
    name: 'Lot L'
  },
  // ... more locations
];

map.addControl(new mapboxgl.NavigationControl());

// Functions should be in asynchronous func or it may not be called
map.on('load', () => {
    locations.forEach(location => {
        new mapboxgl.Marker()
          .setLngLat(location.coordinates)
          .setPopup(new mapboxgl.Popup().setHTML(`<h3>${location.name}</h3>`))
          .addTo(map);
    });
});