//These four imports are required for setup
let mongoose = require("mongoose");
let Station = require('../models/station');
let Observation = require('../models/observation');
let server = require('../app');

//These are the actual modules we use
let chai = require('chai');
let chaiHttp = require('chai-http');
chai.use(chaiHttp);

describe('Endpoint tests', () => {
    //###########################
    //These variables contain the ids of the existing station/observation
    //That way, you can use them in your tests (e.g., to get all observations for a station)
    //###########################
    let stationId = '';
    let observationId = '';

    //###########################
    //The beforeEach function makes sure that before each test, 
    //there is exactly one station and one observation (for the existing station).
    //The ids of both are stored in stationId and observationId
    //###########################
    beforeEach((done) => {
        let station = new Station({ description: "Reykjavik", lat: 64.1275, lon: 21.9028 });
        let observation = new Observation({ stationId: station._id, temp: 2.0, windSpeed: 30.5, windDir: "ne", hum: 20.5, prec: 0.0 });

        Station.deleteMany({}, (err) => {
            Observation.deleteMany({}, (err) => {
                station.save((err, stat) => {
                    observation.save((err, obs) => {
                        stationId = stat._id;
                        observationId = obs._id;
                        done();
                    });
                });
            });
        });
    });

    //###########################
    //Write your tests below here
    //###########################

    //  1. GET/api/v1/stations
    it("1. GET /stations request", function(done) {
        chai.request('http://localhost:3000')
        .get('/api/v1/stations')
        .end((err, res) => {
            chai.expect(res).to.have.status(200);
            chai.expect(res).to.be.json;

            chai.expect(res.body).is.a('array');    
            chai.expect(res.body.length).to.be.equal(1);
            chai.expect(Object.keys(res.body[0]).length).to.be.equal(2);
                        
            chai.expect(res.body[0]).to.have.property('_id');
            chai.expect(res.body[0]).to.have.property('description');
            
            chai.expect(res.body[0]._id).to.be.a('string');
            chai.expect(res.body[0].description).to.be.a('string').eql('Reykjavik');

            done(); 
        });
    });

    
    //  2. GET/api/v1/stations/:id
    it("2. GET /stations with ID request", function(done) {
        chai.request('http://localhost:3000')
        .get('/api/v1/stations/' + stationId)
        .end((err, res) => {
            chai.expect(res).to.have.status(200);
            chai.expect(res).to.be.json;
            chai.expect(res.body).is.a('object');  
            chai.expect(Object.keys(res.body).length).to.be.equal(5);

            chai.expect(res.body).to.have.property('_id').to.be.a('string');
            chai.expect(res.body).to.have.property('description').to.be.a('string').eql('Reykjavik');
            chai.expect(res.body).to.have.property('lon').to.be.a('number').eql(21.9028);
            chai.expect(res.body).to.have.property('lat').to.be.a('number').eql(64.1275);
            chai.expect(res.body).to.have.property('observations').to.be.a('array');

            done(); 
        });
    });


    //  3. POST/api/v1/stations
    it("3. POST / Should make a POST request with a new station", function(done) {
        let newStation = {'description': 'Selfoss', 'lat': 63.9363, 'lon': -21.0028};

        chai.request('http://localhost:3000')
        .post('/api/v1/stations')
        .set('content-type', 'application/json')
        .send(newStation)
        .end((err, res) => {
            chai.expect(res).to.have.status(201);
            chai.expect(res).to.be.json;
            chai.expect(res.body).to.be.a('object');
            chai.expect(Object.keys(res.body).length).to.be.equal(4);

            chai.expect(res.body).to.have.property('_id');
            chai.expect(res.body).to.have.property('description');
            chai.expect(res.body).to.have.property('lat');
            chai.expect(res.body).to.have.property('lon');
            
            chai.expect(res.body.description).to.be.a('string').eql('Selfoss');
            chai.expect(res.body.lat).to.be.a('number').eql(63.9363);
            chai.expect(res.body.lon).to.be.a('number').eql(-21.0028);

            done();
        });
    });


    //  4. GET/api/v1/stations/:stationId/observations 
    it("4. GET /observations of a given stations ID request", function(done) {
        chai.request('http://localhost:3000')
        .get('/api/v1/stations/' + stationId + '/observations')
        .end((err, res) => {
            chai.expect(res).to.have.status(200);
            chai.expect(res).to.be.json;
            chai.expect(res.body).to.be.a('array');

            chai.expect(res.body.length).to.be.equal(1);
            chai.expect(Object.keys(res.body).length).to.be.equal(1);
            
            chai.expect(res.body[0]).to.have.property('_id');
            chai.expect(res.body[0]).to.have.property('temp');
            chai.expect(res.body[0]).to.have.property('windSpeed');
            chai.expect(res.body[0]).to.have.property('windDir');
            chai.expect(res.body[0]).to.have.property('hum');
            chai.expect(res.body[0]).to.have.property('prec');
            
            chai.expect(res.body[0]._id).to.be.a('string');
            chai.expect(res.body[0].temp).to.be.a('number').eql(2);
            chai.expect(res.body[0].windSpeed).to.be.a('number').eql(30.5);
            chai.expect(res.body[0].windDir).to.be.a('string').eql('ne');
            chai.expect(res.body[0].hum).to.be.a('number').eql(20.5);
            chai.expect(res.body[0].prec).to.be.a('number').eql(0);

            done(); 
        });
    });
    
    //  5. GET/api/v1/stations/:stationId/observations/:obsId 
    it("5. GET /retrieve a given observations (with ID) of a given stations request", function(done) {
        chai.request('http://localhost:3000')
        .get('/api/v1/stations/' + stationId + '/observations/' + observationId)
        .end((err, res) => {
            chai.expect(res).to.have.status(200);
            chai.expect(res).to.be.json;
            chai.expect(res.body).to.be.a('object');
            chai.expect(Object.keys(res.body).length).to.be.equal(6);

            chai.expect(res.body).to.have.property('_id').to.be.a('string');
            chai.expect(res.body).to.have.property('temp').to.be.a('number').eql(2);
            chai.expect(res.body).to.have.property('windSpeed').to.be.a('number').eql(30.5);
            chai.expect(res.body).to.have.property('windDir').to.be.a('string').eql('ne');
            chai.expect(res.body).to.have.property('hum').to.be.a('number').eql(20.5);
            chai.expect(res.body).to.have.property('prec').to.be.a('number').eql(0);

            done();
        });
    });


    //  6. POST/api/v1/stations/:stationId/observations
    it("6a. POST / Should make a POST request with a new observation to a specific station ID", function(done) {
        let newObservation = {"temp": 5, "windSpeed": 15.9, "windDir": "w", "hum": 10.1, "prec": 0}
        
        chai.request('http://localhost:3000')
        .post('/api/v1/stations/' + stationId + '/observations/')
        .set('content-type', 'application/json')
        .send(newObservation)
        .end((err, res) => {
            chai.expect(res).to.have.status(201);
            chai.expect(res).to.be.json;
            chai.expect(res.body).to.be.a('object');

            chai.expect(Object.keys(res.body).length).to.be.equal(6);

            chai.expect(res.body).to.have.property('_id');
            chai.expect(res.body).to.have.property('temp');
            chai.expect(res.body).to.have.property('windSpeed');
            chai.expect(res.body).to.have.property('windDir');
            chai.expect(res.body).to.have.property('hum');
            chai.expect(res.body).to.have.property('prec');

            chai.expect(res.body._id).to.be.a('string');
            chai.expect(res.body.temp).to.be.a('number').eql(5);
            chai.expect(res.body.windSpeed).to.be.a('number').eql(15.9);
            chai.expect(res.body.windDir).to.be.a('string').eql('w');
            chai.expect(res.body.hum).to.be.a('number').eql(10.1);
            chai.expect(res.body.prec).to.be.a('number').eql(0);

            done();
        });
    });

    it("6b. POST / failure case: body attribute missing, resulting in a 400 error", function(done) {
        let newObservation = {"temp": 6, "windSpeed": 1.2, "hum": 5.4, "prec": 0}
        
        chai.request('http://localhost:3000')
        .post('/api/v1/stations/' + stationId + '/observations/')
        .set('content-type', 'application/json')
        .send(newObservation)
        .end((err, res) => {
            chai.expect(res).to.have.status(400);
            done();
        });
    });


    it("6c. POST / failure case: Humidity (hum) higher than range value expected, resulting in a 400 response code", function(done) {
        let newObservation = {"temp": 3, "windSpeed": 21.0, "windDir": "e", "hum": 100.1, "prec": 0}
        
        chai.request('http://localhost:3000')
        .post('/api/v1/stations/' + stationId + '/observations/')
        .set('content-type', 'application/json')
        .send(newObservation)
        .end((err, res) => {
            chai.expect(res).to.have.status(400);
            done();
        });
    });

    
    //  7. DELETE/api/v1/stations/:stationId/observations/:obsId
    it("7. DELETE / delete observation request for station ID", function(done) {
        chai.request('http://localhost:3000')
        .delete('/api/v1/stations/' + stationId + '/observations/' + observationId)
        .set('content-type', 'application/json')
        .end((err, res) => {
            chai.expect(res).to.have.status(200);
            chai.expect(res).to.be.json;
            chai.expect(res.body).to.be.a('object');

            chai.expect(Object.keys(res.body).length).to.be.equal(6);

            chai.expect(res.body).to.have.property('_id').to.be.a('string');
            chai.expect(res.body).to.have.property('temp').to.be.a('number').eql(2);
            chai.expect(res.body).to.have.property('windSpeed').to.be.a('number').eql(30.5);
            chai.expect(res.body).to.have.property('windDir').to.be.a('string').eql('ne');
            chai.expect(res.body).to.have.property('hum').to.be.a('number').eql(20.5);
            chai.expect(res.body).to.have.property('prec').to.be.a('number').eql(0);

            done();
        });
    });


    // 8. DELETE/api/v1/stations/:id.
    it("8. DELETE / delete station with given ID request", function(done) {
        chai.request('http://localhost:3000')
        .delete('/api/v1/stations/' + stationId)
        .set('content-type', 'application/json')
        /* .set('Authorization', 'HMAC: L3zr8x6P25e1gNoBXnbMZjdEmHrh6cmCluRcWld4KRWk9lm7vYJVDEOapqwy')
        5a36d322db0b7c8c6a7133b174645b9ceab3964d72590942cdf9efa7c4c097af')
        L3zr8x6P25e1gNoBXnbMZjdEmHrh6cmCluRcWld4KRWk9lm7vYJVDEOapqwy') */
        .end((err, res) => {
            chai.expect(res).to.have.status(401);
            chai.expect(res).to.be.json;
            chai.expect(res.body).to.be.a('object');

            chai.expect(Object.keys(res.body).length).to.be.equal(1);
            done();
        });
    });


    // Extra.  A call to /api/v1/stations with an unsupported HTTP verb results in  an 405 response code.
    it("Extra. PUT /unsupported HTTP verb: 405 response code", function(done) {
        chai.request('http://localhost:3000')
        .put('/api/v1/stations')
        .end((err, res) => {
            chai.expect(res).to.have.status(405);
            done();
        });
    });
});





















/*     
    it("1b. GET / failure case: wrong URL request (not plural)", function (done) {
        let fakeStationId = "f3k409kf2j098ffe";

        chai.request('http://localhost:3000')
        .get('/api/v1/station1/')
        .end((err, res) => {
            chai.expect(res).to.have.status(405);
            done();
        });
    });


    it("2b. GET / failure case: station with non-existing ID request", function (done) {
        let fakeStationId = "f3k409kf2j098ffe";

        chai.request('http://localhost:3000')
        .get('/api/v1/stations/' + fakeStationId)
        .end((err, res) => {
            chai.expect(res).to.have.status(404);
            done();
        });
    });


    it("3b. POST / failure case: latitude missing (for example)", function(done) {
        let newStation = {'description': 'Vík í Mýrdal', 'lon': 77.5482};

        chai.request('http://localhost:3000')
        .post('/api/v1/stations')
        .set('content-type', 'application/json')
        .send(newStation)
        .end((err, res) => {
            chai.expect(res).to.have.status(400);
            done();
        });
    });

*/