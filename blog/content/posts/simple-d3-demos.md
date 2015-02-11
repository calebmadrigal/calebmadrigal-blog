author: Caleb Madrigal
comments: true
date: 2015-02-11 11:35:00
layout: post
slug: simple-d3-demos
title: Simple D3 demos
category: javascript
tags: javascript, programming, data

I've been playing with [d3](http://d3js.org/) recently, and it awesome! I'm especially amazed by the ease of animating [transitions](https://github.com/mbostock/d3/wiki/Transitions) with it.

There are plenty of [amazing d3 demos](https://github.com/mbostock/d3/wiki/Gallery) out there, but I wanted to write some simpler ones to help me understand the basics of d3. You can find them here:

<http://calebmadrigal.github.io/d3-demos/>

For example, here's how to draw a circle with d3:

<div id="d3-simple-circle"></div>

<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/d3/3.5.3/d3.min.js"></script>

<script type="text/javascript">
  var width = 400;
  var height = 400;

  var x = width/2;
  var y = height/2;
  var radius = 100;
  var fill = '#F012BE';
  
  var svg = d3.select("#d3-simple-circle").append("svg")
    .attr("width", width)
    .attr("height", height)
    .append('circle')
    .attr({ r: radius, cx: x, cy: y, fill: fill});
</script>

Code:

      var width = 400;
      var height = 400;

      var x = width/2;
      var y = height/2;
      var radius = 100;
      var fill = '#F012BE';
      
      var svg = d3.select("#d3-simple-circle").append("svg")
        .attr("width", width)
        .attr("height", height)
        .append('circle')
        .attr({ r: radius, cx: x, cy: y, fill: fill});

And here's one of the cooler-looking ones:


<div id="dancing-sin-graph"></div>

<script type="text/javascript">
  var width = 700;
  var height = 500;

  var linspace = function(start, stop, num_samples) {
    return d3.range(start, stop * (num_samples / (stop-start)))
      .map(function (n) { return n / (num_samples / (stop-start)); });
  };

  var direction = 1;
  var x = linspace(0, 20, 500);
  var y = x.map(function (i) { return ((height/2)-50) * direction * Math.sin(i); });

  var x_step = width / x.length;
  var y_middle = height / 2;

  var radius = 100;
  var fill = '#F012BE';

  var sin_svg = d3.select("#dancing-sin-graph").append("svg")
    .attr("width", width)
    .attr("height", height);
  
  sin_svg.selectAll('circle')
    .data(y)
    .enter()
    .append('circle')
    .attr({r: 2, fill: fill})
    .attr('cx', function (d, i) {
      return x_step * i;
    })
    .attr('cy', function (d, i) {
      return y_middle - d;
    });

  function invert() {
    direction = direction * -1;
    y = x.map(function (i) { return ((height/2)-50) * direction * Math.sin(i); });

    d3.select("#dancing-sin-graph").selectAll('circle')
      .data(y)
      .transition()
      .duration(1000)
      .attr({r: 2, fill: fill})
      .attr('cx', function (d, i) {
        return x_step * i;
      })
      .attr('cy', function (d, i) {
        return y_middle - d;
      });
  }

  // Make the interval just less than the transition duration so motion never stops
  setInterval(invert, 900);
</script>

Code (granted, this one is a bit more complicated):

    var width = 700;
    var height = 500;

    var linspace = function(start, stop, num_samples) {
      return d3.range(start, stop * (num_samples / (stop-start)))
        .map(function (n) { return n / (num_samples / (stop-start)); });
    };

    var direction = 1;
    var x = linspace(0, 20, 500);
    var y = x.map(function (i) { return ((height/2)-50) * direction * Math.sin(i); });

    var x_step = width / x.length;
    var y_middle = height / 2;

    var radius = 100;
    var fill = '#F012BE';

    var sin_svg = d3.select("#dancing-sin-graph").append("svg")
      .attr("width", width)
      .attr("height", height);
    
    sin_svg.selectAll('circle')
      .data(y)
      .enter()
      .append('circle')
      .attr({r: 2, fill: fill})
      .attr('cx', function (d, i) {
        return x_step * i;
      })
      .attr('cy', function (d, i) {
        return y_middle - d;
      });

    function invert() {
      direction = direction * -1;
      y = x.map(function (i) { return ((height/2)-50) * direction * Math.sin(i); });

      d3.select("#dancing-sin-graph").selectAll('circle')
        .data(y)
        .transition()
        .duration(1000)
        .attr({r: 2, fill: fill})
        .attr('cx', function (d, i) {
          return x_step * i;
        })
        .attr('cy', function (d, i) {
          return y_middle - d;
        });
    }

    // Make the interval just less than the transition duration so motion never stops
    setInterval(invert, 900);

