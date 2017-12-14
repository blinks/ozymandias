require 'squib'
require 'yaml'

# TODO: Replace with built-in after pull req.
cards = YAML.load_file('oracle.yml')
data = Squib::DataFrame.new
keys = cards.map {|c| c.keys}.flatten.uniq
keys.each {|k| data[k] = [] }
cards.each do |card|
  keys.each do |k|
    data[k] << card[k]
  end
end

layouts = ['layout.yml']

Squib::Deck.new cards: data['title'].size, layout: layouts do
  rect fill_color: '#fff', layout: 'safe'

  # Placeholder "art."
  rect layout: 'art'

  # Suit icons are just filled shapes. TODO: Icons?
  suit = {}; data['suit'].each_with_index{ |t, i| (suit[t] ||= []) << i}
  circle range: suit['merchant'], fill_color: 'gold',
    x: 135, y: 135, radius: 50
  rect range: suit['soldier'], fill_color: '#faa',
    x: 90, y: 90, width: 90, height: 90
  triangle range: suit['sage'], fill_color: '#aaf',
    x1: 135, y1: 80, x2: 190, y2: 170, x3: 80, y3: 170

  # Card information. TODO: Sector layouts.
  text str: data['rank'], layout: 'rank'
  text str: data['title'], layout: 'title'
  text str: data['text'], layout: 'text'

  build :print_n_play do
    save_pdf file: 'pnp.pdf',
      width: '8.5in', height: '11in', margin: '0.5in',
      gap: 0, trim: '0.25in'
  end

  build :pngs do
    save_png
  end
end
