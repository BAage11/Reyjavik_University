const express = require('express');
const app = express();
const port = 3000;
const mymodule = require('./math.js')
const url = require('url');

// Can't get the validation to work - therefore commented out.
app.get('/divide', (req, res) => {
    /* var url = req.url; 
       if ('/divide' === url.slice(0,7)) {   */
    var a = req.query.a;
    var b = req.query.b;

    res.writeHead(200, {'Content-Type': 'text/html'});
    var txt = mymodule.stringifyDivision(a,b);
    res.write(txt);
    res.end();
     
/*    }  else {
    res.writeHead(405, {'Content-Type': 'text/html'});
    res.write('This operation is not supported.');
    res.end(); */

});


app.listen(port, () => {
    console.log('Listening on port', port, '...')
});