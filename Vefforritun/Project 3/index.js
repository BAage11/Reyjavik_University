
var express = require('express');
var app = express();
var fs = require("fs");
var port = process.env.PORT || 3000;
app.use(express.json());
var nextID = 5;
var nextObsID = 5;

/*  1. Read all stations.
    Returns an array of all stations. For each station, only the description 
    and the id is included in the response. */
app.get('/api/v1/stations', function (req, res) {
    const ret_var = []
    for (let i=0; i < stations.length; i++) {
        ret_var.push(String(stations[i].id) + " " + stations[i].description); 
    };
    return res.status(200).json(ret_var);
});


/* 2. Read an individual station. 
    Returns all attributes of a speciﬁed station. */
app.get('/api/v1/stations/:id', function (req, res) {
    const station = stations.find(item => item.id === parseInt(req.params.id));

    if (!station) {
        return res.status(404).json("The station with ID " + String(req.params.id) + " was not found.");
    };

    return res.status(200).json(station);
});


/* 3. Create a new station. 
    The endpoint expects all attributes apart from the id in the request body. The id shall be auto-generated. The request, if successful, shall return the new station (all attributes, including id). */
app.post('/api/v1/stations', function (req, res) {
    if (!req.body.description) {
        return res.status(400).json("Description input is missing.");
    };

    if (!req.body.lat || !parseFloat(req.body.lat) || req.body.lat < -90 || req.body.lat > 90) {
        return res.status(400).json("Latitude must be a NUMBER between -90 and 90.");
    };

    if (!req.body.lon || !parseFloat(req.body.lon) || req.body.lon < -180 || req.body.lon > 180) {
        return res.status(400).json("Longitude must be a NUMBER between -180 and 180.");
    };

    if (!req.body.observations) {
        return res.status(400).json("Observation input is missing.");
    };
    
    const station = {
        id: nextID,
        description: req.body.description,
        lat: req.body.lat,
        lon: req.body.lon,
        observations: req.body.observations
    };

    if (req.body.observations != undefined) {
        nextObsID++;
    };
    nextID++;
    stations.push(station);
    return res.status(201).json(station);
});


/* 4. Delete a station. 
    Deletes an existing station. The request also deletes all observations for the given station. The request, if successful, returns all attributes of the deleted station (including all observations in the observations attribute). */
app.delete('/api/v1/stations/:id', function (req, res) {
    const station = stations.find(item => item.id === parseInt(req.params.id));

    if (!station) {
        return res.status(404).json('The station with ID ' + String(req.params.id) + ' was not found.');
    };

    const index = stations.indexOf(station);
    stations.splice(index, 1);

    console.log(station);
    console.log(deletedObsv);

    return res.status(200).json(station);
});



/* 5. Update a station.
    (Completely) Updates an existing station. The updated data is expected in the request body (excluding the id). The request, if successful, returns all updated attributes of the station. */
app.put('/api/v1/stations/:id', function (req, res) {
    const station = stations.find(item => item.id === parseInt(req.params.id));

    if (!station) {
        return res.status(404).json('The station ID ' + String(req.params.id) + ' was not found.');
    };

    station.description = req.body.description
    station.lat = req.body.lat
    station.lon = req.body.lon
    station.observations = req.body.observations

    if (!station.description) {
        return res.status(400).json("Description input is missing."); 
    };

    if (!station.lat || !parseFloat(station.lat) || station.lat < -90 || station.lat > 90) {
        return res.status(400).json("Latitude must be a NUMBER between -90 and 90.");
    };

    if (!station.lon || !parseFloat(station.lon) || station.lon < -180 || station.lon > 180) {
        return res.status(400).json("Longitude must be a NUMBER between -180 and 180.");
    };

    if (!station.observations) {
        return res.status(400).json("Observation input is missing.");
    };

    return res.status(200).json(station);
});


/* 6. Delete all stations.
    Deletes all existing stations. The request also deletes all observations for all existing stations. The request, if successful, returns all deleted stations (all attributes), as well as their observations (as a part of the observations attribute). */
app.delete('/api/v1/stations', function (req, res) {
    var returnArray = stations.slice();
    stations = [];
    res.status(200).json(returnArray);
});


////////////////////////////////////////////////////////////////////////////////////


/* 1. Read all observations for a station. 
    Returns an array of all observations (with all attributes) for a speciﬁed station. */
app.get('/api/v1/stations/:id/observations', function (req, res) {
    const station = stations.find(item => item.id === parseInt(req.params.id));
    const ret_var = [];

    if (!station) {
        return res.status(404).json('The station with ID '+ String(req.params.id) + ' was not found.');
    }; 

    for (let i=0; i< observations.length; i++) {
        if (observations[i].id == station.observations[0]) {
            ret_var.push(observations[i]);
        };
    };

    return res.status(200).json(ret_var);
});


/* 2. Read an individual observation. 
    Returns all attributes of a speciﬁed observation (for a station). */
app.get('/api/v1/stations/:Stationid/observations/:id', function (req, res) {
    const station = stations.find(item => item.id === parseInt(req.params.Stationid));
    const observation = observations.find(item => item.id === parseInt(req.params.id));

    if (!station) {
        return res.status(404).json('The station with ID ' + String(req.params.Stationid) + ' was not found.');
    }; 

    if (!observation) {
        return res.status(404).json('The observation with ID ' + String(req.params.id) + ' was not found.')
    };

    for (i=0; observations.length; i++) {
        if (observations[i].id == station.observations[0]) {
            if (observations[i].id == observation.id) {
                return res.status(200).json(observations[i]);
            };
        };
    };

    return res.status(404).json('Observation ID ' + String(req.params.id) + ' for station ID ' + String(req.params.Stationid) + ' does not exist.');
});


/* 3. Create a new observation. 
    Creates a new observation for a speciﬁed station. The endpoint expects all attributes apart from the id and the date in the request body. The id (unique, non-negative number)and the date (current date) shall be auto-generated. The request, if successful, shall return the new observation (all attributes, including id and date). */
app.post('/api/v1/stations/:id/observations', function (req, res) {
    if (!parseFloat(req.body.temp) || !parseFloat(req.body.windSpeed)) {
        return res.status(400).json("Temperature and WindSpeed must be an integer or a floating NUMBER.")
    };

    if (req.body.prec < 0 && parseFloat(req.body.prec)) {
        return res.status(400).json("Precipitation must be a positive floating number.")
    };

    if (req.body.hum < 0 || req.body.hum > 100) {
        return res.status(400).json("Humidity shall always be between 0 and 100.")
    };

    let observation = {
         id: nextObsID,
         date: Number(new Date()),
         temp: req.body.temp,
         windSpeed: req.body.windSpeed,
         windDir: req.body.windDir,
         prec: req.body.prec,
         hum: req.body.hum
    };

    nextObsID++;
    observations.push(observation);
    return res.status(201).json(observation);
   
});


/* 4. Delete an observation.
    Deletes an existing observation for a speciﬁed station. The request, if successful, returns all attributes of the deleted observation. */
app.delete('/api/v1/stations/:Stationid/observations/:Observationid', function (req, res) {
    const station = stations.find(item => item.id === parseInt(req.params.Stationid));
    const observation = observations.find(item => item.id === parseInt(req.params.Observationid));
    
    if (!station) {
        return res.status(404).json("The station with ID " + String(req.params.Stationid) + " was not found.");
    };

    if (!observation) {
        return res.status(404).json("The observation with ID " + String(req.params.Observationid) + " does not exist.");
    };

    for (let i=0; i<stations.length; i++) {
        if (stations[i].id === station.id) {
            for (let j=0; j<stations[i].observations.length; j++) {
                if (stations[i].observations[j] === Number(req.params.Observationid)) {
                    stations[i].observations.splice(j,1);
                    for (let k=0; k<observations.length; k++) {
                        if (observations[k].id === Number(req.params.Observationid)) {
                            return res.status(200).json(observations.splice(k,1));
                        };
                    };
                };
            };
        };
    };
    return res.status(404).json("The station with ID " + String(req.params.Stationid) + " does not have the observation with ID" + String(req.params.Observationid) + ".")
});


/* 5. Delete all observations for a station.
    Deletes all existing observations for a speciﬁed station. The request, if successful, returns all deleted observations (all attributes).*/
app.delete('/api/v1/stations/:id/observations', function (req, res) {
    const station = stations.find(item => item.id === parseInt(req.params.id));
    const del_obsv = [];

    if (!station) {
        return res.status(404).json("The station with ID" + String(req.params.id) + "was not found.");
    };

    for (let i=0; observations.length; i++) {
        if (observations.id === station.observations[0]) {
            del_obsv.push(observations[i]);
            observations.splice(i, 1);
        };
    };
    
    if (del_obsv != []) {
        return res.status(200).json(del_obsv);
    } else {
        return res.status(404).json("The station with ID" + String(req.params.Stationid) + "does not have any observations.");
    };
});


app.use('*', (req, res) => {
    res.status(405).send('Operation not supported.');
});


app.listen(port, function () {
   console.log('Listening on port', port, '...')
});


var stations = [
    {id: 1, description: "Reykjavik", lat: 64.1353, lon: -21.8952, observations: [2]},
    {id: 2, description: "Akureyri", lat: 65.6839, lon: -18.1105, observations: [1]},
    {id: 3, description: "Egilsstaðir", lat: 65.2669, lon: -14.3948, observations: [4]},
    {id: 4, description: "Höfn", lat: 64.256, lon: -15.2076, observations: [3]}
];


var observations = [
    {id: 1, date: 1551885104266, temp: -2.7, windSpeed: 2.0, windDir: "e", prec: 0.0, hum: 82.0},
    {id: 2, date: 1551885137409, temp: 0.6, windSpeed: 5.0, windDir: "n", prec: 0.0, hum: 50.0},
    {id: 3, date: 1551885134244, temp: -2.6, windSpeed: 7.4, windDir: "n", prec: 0.0, hum: 55.0},
    {id: 4, date: 2622341813241, temp: 2.2, windSpeed: 0.4, windDir: "w", prec: 0.0, hum: 75.0},
]; 

