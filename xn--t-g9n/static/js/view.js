// Hexagon points.
var points = [0, 1, .866, .5, .866, -.5, 0, -1, -.866, -.5, -.866, .5];
// Manual scaling; perhaps use transform instead?
const SIZE = 32;
for (var i in points) { points[i] *= SIZE; }

// TODO: Calculate real x and y from hex coord x and y.
// http://www.redblobgames.com/grids/hexagons/#coordinates
var data = [
  {q: 1, r: 2, gems: 0, value: 1, stack: ['#33e', '#222']},
  {q: 2, r: 1, gems: 1, value: 3, stack: ['#e33', '#eee']}
];

var sector = d3.select('svg')
    .selectAll('g').data(data)
  .enter().append('g')
    .attr('transform', function(d) {
      var x = SIZE * Math.sqrt(3) * (d.q + d.r/2);
      var y = SIZE * 1.5 * d.r;
      return 'translate(' + x + ',' + y + ')'; })
    .on('mouseover', function(d, i) {
      d3.select(this).select('polygon')
        .transition()
        .style('stroke', 'white')
        .style('stroke-opacity', '1');
    })
    .on('mouseout', function(d, i) {
      d3.select(this).select('polygon')
        .transition()
        .style('stroke-opacity', '0');
    })

var polygon = sector.append('polygon')
  .attr('points', points)
  .transition()
  .styleTween('fill', function() {
    return d3.interpolate('gray', 'black'); })

sector.append('text')
  .attr('x', 0)
  .attr('y', SIZE - 10)
  .text(function(d) { return d.value + '+' + d.gems; });

var disk = sector.selectAll('circle')
  .data(function(d) { return d.stack.reverse(); })
  .enter().append('circle')
    .attr('cy', function(_, i) { return -4 * i; })
    .style('fill', function(d) { return d; })
    .attr('r', 0)
    .transition()
    .duration(250)
    .delay(function(d, i) { return (i + 1) * 250; })
    .attr('r', 8)
