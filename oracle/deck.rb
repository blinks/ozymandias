require 'squib'

data = Squib.csv file: 'manifest.csv'
layouts = ['layout.yml']

Squib::Deck.new(cards: data['Name'].size, layout: layouts) do
  rect fill_color: '#fff', layout: 'safe'

  # Card information.
  type = {}; data['Color'].each_with_index{ |t, i| (type[t] ||= []) << i}

  # Color bar
  rect range: type['K'], layout: :title_box,
    fill_color: '#444', stroke_width: 0
  text range: type['K'], layout: :title_middle,
    color: :black, str: data['Name']
  text range: type['K'], layout: :type_icon,
    color: :white, str: data['Rank']
  text range: type['K'], layout: :title,
    color: :white, str: data['Color']

  rect range: type['B'], layout: :title_box,
    fill_color: :deep_sky_blue, stroke_width: 0
  text range: type['B'], layout: :title_middle,
    color: :black, str: data['Name']
  text range: type['B'], layout: :type_icon,
    color: :black, str: data['Rank']
  text range: type['B'], layout: :title,
    color: :black, str: data['Color']

  rect range: type['W'], layout: :title_box,
    fill_color: '#bbb', stroke_width: 0
  text range: type['W'], layout: :title_middle,
    color: :black, str: data['Name']
  text range: type['W'], layout: :type_icon,
    color: :black, str: data['Rank']
  text range: type['W'], layout: :title,
    color: :black, str: data['Color']

  rect range: type['R'], layout: :title_box,
    fill_color: :red, stroke_width: 0
  text range: type['R'], layout: :title_middle,
    color: :black, str: data['Name']
  text range: type['R'], layout: :type_icon,
    color: :black, str: data['Rank']
  text range: type['R'], layout: :title,
    color: :black, str: data['Color']

  rect range: type['S'], layout: :title_box,
    fill_color: :black, stroke_width: 0
  text range: type['S'], layout: :title,
    color: :white, str: data['Name']
  text range: type['S'], layout: :type_icon,
    color: :white, str: data['Rank']

  text str: data['Text'], layout: :rule_bottom

  save_sheet sprue: 'letter_poker_card_9up.yml'
end
