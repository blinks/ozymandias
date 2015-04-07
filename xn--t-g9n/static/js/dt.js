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
  var api = $resource('/api/');
  this.createGame = function() {
    // TODO: Fire off a creation RPC
    // Pass the game state to d3update.
    api.get({}, function(data) {
      d3update(data);
    });
  };
});

// Use d3 to update SVG.
function d3update(data) {
  // Sector group in the galaxy map.
  var sector = d3.select('svg').selectAll('g')
    .data(data.map);

  var g = sector.enter().append('g')
    .attr('transform', function(d) {
      // Axial coordinate system.
      // http://www.redblobgames.com/grids/hexagons/#coordinates
      var x = 320 + SIZE * Math.sqrt(3) * (d.q + d.r/2);
      var y = 240 + SIZE * 1.5 * d.r;
      return 'translate(' + x + ',' + y + ')';
    });
  sector.exit().remove();

  // Inside the sector group:
  // ... the background hexagon
  g.append('polygon')
    .attr('points', HEXAGON);
  // ... the natural and invested value
  g.append('text')
    .attr('y', SIZE - 10)
    .text(function(d) {
      return d.value + '+' + d.gems;
    });
  // ... the stack of control disks
  var disk = g.selectAll('circle')
    .data(function(d) {
      return d.stack.reverse();
    });
  disk.enter().append('circle')
      .style('fill', function(d) { return d; })
      .attr('cy', function(d, i) { return SIZE / 8 * i; })
      .attr('r', function(d, i) { return SIZE / 4; });
  disk.exit().remove();
}
