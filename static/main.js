window.onload = function(){

  // set defaults
  url = '/pattern/sweep_rainbow/brightness/100';
  brightness = 100;

  // turn on if brightness is 0
  $('#static, #dynamic, #static-random').click(function(e){
    if (brightness == 0) {
      brightness = 50;
    }
  });

  // static color
  $('#' + 'static').click(function(e){
    var color = e.target.id;
    url = get_url_static(color, brightness);
    $.get(url, function(data, status){});
  });

  // static color random
  $('#' + 'static-random').click(function(e){
    var color_red = get_random_int(1,255);
    var color_green = get_random_int(1,255);
    var color_blue = get_random_int(1,255);
    var color = color_red.toString(16).padStart(2, '0') +
      color_green.toString(16).padStart(2, '0') +
      color_blue.toString(16).padStart(2, '0');
    url = '/color/' + color + '/brightness/' + brightness;
    url = get_url_static(color, brightness);
    $.get(url, function(data, status){});
  });

  // dynamic color
  $('#' + 'dynamic').click(function(e){
    var pattern = e.target.id;
    url = get_url_dynamic(pattern, brightness);
    $.get(url, function(data, status){});
  });

  // control off
  $('#' + 'off').click(function(e){
    brightness = 0;
    url = get_url_brightness(url, brightness);
    $.get(url, function(data, status){});
  });

  // control brightness
  $('#' + 'brightness').click(function(e){
    id = e.target.id.split('_');
    brightness = id[1];
    url = get_url_brightness(url, brightness);
    $.get(url, function(data, status){});
  });

	/*
  $('#demo-input').colorpicker();
  $('#demo-input').on('colorpickerChange', function(event) {
    $('#demo-input').css('background-color', event.color.toString());
  });
*/

};

function get_random_int(min, max) {
  return Math.floor(Math.random() * (max - min + 1)) + min;
}

function get_url_static(color, brightness) {
  return '/color/' + color + '/brightness/' + String(brightness);
}

function get_url_dynamic(pattern, brightness) {
  return '/pattern/' + pattern + '/brightness/' + String(brightness);
}

function get_url_brightness(url, brightness) {
  urlSplit = url.split('/');
  urlSplit[4] = String(brightness);
  return urlSplit.join('/');
}
