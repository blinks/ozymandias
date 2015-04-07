// Hex size and important hexagon constant.
const SIZE = 32.0;
const SIN60 = Math.sqrt(3.0) / 2.0;
const HEXAGON = [0, 1, SIN60, .5, SIN60, -.5,
     0, -1, -SIN60, -.5, -SIN60, .5].map(function(p) { return p * 32.0; });

var dt = angular.module('dt', ['ngResource', 'ngRoute']);

dt.config(function($routeProvider, $locationProvider) {
  $routeProvider
    .when('/', {
      templateUrl: 'game.html',
      controller: 'GameCtrl',
      controllerAs: 'game'
    })
    .when('/Game/:gameId', {
      templateUrl: 'game.html',
      controller: 'GameCtrl',
      controllerAs: 'game'
    });
  $locationProvider.html5Mode(true);
});

dt.controller('GameCtrl', function($scope, $resource) {
  var Game = $resource('/api/game');
  this.createGame = function() {
    // Fire off a creation RPC
    var newGame = Game.get({}, function() {
      d3update(newGame);
      newGame.$save();
    });
  };
});

// Use d3 to update SVG.
function d3update(data) {
  function CardString(d) { return d.name + ' [' + d.color + ']: ' + d.text; }

  var market = d3.select('#market')
    .selectAll('a')
    .data(data.market);
  market.enter().append('a')
    .attr('class', 'list-group-item')
    .attr('href', '#')
    .text(CardString);
  market.exit().remove();

  var immortals = d3.select('#hand')
    .selectAll('a')
    .data(data.immortals[0].hand);  // FIXME
  immortals.enter().append('a')
    .attr('class', 'list-group-item')
    .attr('href', '#')
    .text(CardString);
  immortals.exit().remove();

  var svg = d3.select('svg');
  var sector = svg.selectAll('g').data(data.galaxy);

  var g = sector.enter().append('g')
    .attr('transform', function(d) {
      // Axial coordinate system.
      // http://www.redblobgames.com/grids/hexagons/#coordinates
      var x = 320 + SIZE * Math.sqrt(3) * (d.q + d.r/2);
      var y = 240 + SIZE * 1.5 * d.r;
      return 'translate(' + x + ',' + y + ')';
    });
  sector.exit().remove();
  sector.on('mousedown', function(d) { console.log(d); });

  // Inside the sector group:
  // ... the background hexagon
  g.append('polygon')
    .attr('points', HEXAGON)
    .style('stroke', 'gray')
    .style('fill', function(d) { return d.value < 0 ? '#444' : 'black'; })
    .style('opacity', '0')
    .transition()
    .style('opacity', '1');
  // ... the natural and invested value
  g.append('text')
    .attr('y', SIZE - 10)
    .text(function(d) { return d.value < 0 ? '?' : d.value + '+' + d.gems; })
    .style('opacity', '0')
    .transition()
    .style('opacity', '1');
  // ... the stack of control disks
  var disk = g.selectAll('circle')
    .data(function(d) {
      return d.stack.reverse();
    });
  disk.enter().append('circle')
      .style('fill', function(d) { return d; })
      .attr('r', function(d, i) { return SIZE / 4; })
      .attr('cy', SIZE).style('opacity', '0')
      .transition()
      .style('opacity', '1')
      .attr('cy', function(d, i) { return SIZE / 8 * i; });
  disk.exit().remove();
}
