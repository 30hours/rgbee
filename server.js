const express = require('express')
const {exec} = require("child_process");

const app = express()

app.use(function(req, res, next) {
  res.header("Access-Control-Allow-Origin", "*");
  next();
});

app.use( express.static( __dirname + '/static' ));

app.get('/', function (req, res) {
  res.sendFile(__dirname + '/static/index.html');
})

function is_valid_color(color) {

  return /^#[0-9A-F]{6}$/i.test('#' + color);

}

function is_valid_pattern(pattern) {

  patterns = [
    'sweep_red',
    'sweep_green',
    'sweep_blue',
    'sweep_rainbow'
  ];

  return patterns.includes(pattern);

}

function is_valid_brightness(brightness) {

  brightness = parseInt(brightness);

  return (brightness >= 0) && (brightness <= 100);

}

app.get('/color/:color/brightness/:brightness', function(req, res) {

  var color = req.params.color.toUpperCase();
  var brightness = req.params.brightness;

  // validate input
  var isValidColor = is_valid_color(color);
  var isValidBrightness = is_valid_brightness(brightness);
	
  if (isValidColor && isValidBrightness) {
    console.log('Request static color: ' + color);
    console.log('Request brightness: ' + brightness);
    var process = exec('killall python; python /opt/rgbee/script/static-fade.py ' + color + ' ' + brightness);
  }

  res.redirect('/')

})

app.get('/pattern/:pattern/brightness/:brightness', function(req, res) {
    
  var pattern = req.params.pattern;
  var brightness = req.params.brightness;

  // validate input
  var isValidPattern = is_valid_pattern(pattern);
  var isValidBrightness = is_valid_brightness(brightness);
  
  if (isValidPattern && isValidBrightness) {
    console.log('Request dynamic color: ' + pattern);
    console.log('Request brightness: ' + brightness);
    var process = exec('killall python; python /opt/rgbee/script/' + pattern + '.py' + ' ' + brightness);
  }

  res.redirect('/');

})

app.listen(3000)
