require 'squib'

Squib::Deck.new(cards: 60, layout: 'economy.yml') do
  background color: 'white'
  rect layout: 'cut'
  rect layout: 'safe'
  save_png
end
