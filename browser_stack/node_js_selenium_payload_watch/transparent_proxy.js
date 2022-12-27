//Steps for setup
//Install node if not already installed
//Run 'npm install body-parser -s' (This will install body-parser dependency)
//Run 'npm install express -s' (This will install express dependency)
//Save this code with a .js file extension and run it using 'node filename.js'
//This should intercept all traffic flowing into localhost:4444. This code can be extended to forward request to desired endpoint

var http = require('http');
var express   = require('express'),
app= express();
var bodyParser = require('body-parser');
app.use(bodyParser.urlencoded({
        extended: true
    }));
app.use(bodyParser.json());
app.set('port',4444);
app.all('*',function(req,res){
    console.log('req',req.body)
})

http.createServer(app).listen(app.get('port'),function(){
    console.log('server started using port'+ app.get('port'))
})