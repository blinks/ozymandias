require 'squib'
require 'game_icons'
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
suits = {
  'merchant' => GameIcons.get('lorc/ouroboros')
    .recolor(fg: 'gold', bg_opacity: 0),
  'soldier' => GameIcons.get('lorc/layered-armor')
    .recolor(fg: 'red', bg_opacity: 0),
  'sage' => GameIcons.get('lorc/erlenmeyer')
    .recolor(fg: 'blue', bg_opacity: 0),
}

Squib::Deck.new cards: data['title'].size, layout: layouts do
  background color: 'white'
  rect layout: 'cut'
  rect layout: 'safe'
  svg data: data['suit'].map { |k| suits[k].string }, layout: 'suit'
  text str: data['rank'], layout: 'rank'
  text str: data['title'], layout: 'title'
  text str: data['text'], layout: 'text'
  save_png
end
