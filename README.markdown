# Ozymandias
> And on the pedestal these words appear:  
> ’My name is Ozymandias, king of kings:  
> Look on my works, ye Mighty, and despair!’  
> Nothing beside remains.  
> — Percy Bysshe Shelley, Ozymandias

Ozymandias is a card game for two to four players.

(See PLAYTESTING.md for print-and-play information.)
(Art credits and links [on the wiki](https://github.com/blinks/ozymandias/wiki).)

![Sergey Kolesov](https://camo.githubusercontent.com/f511cda35cc1bf6888a94062e1dd84f19e65b385/68747470733a2f2f7062732e7477696d672e636f6d2f6d656469612f4333375850725757494145307245352e6a7067)

## Components
- ~16 Sector cards.
- ~12 Myth cards, ~6 cities, and a history marker for each faction.
- A history track card (6, 8, ..., 24, 26, 30).
- Influence tokens in several denominations.

### Sectors [Landscape]
Each sector has a number, from 1 to ~6. Lower numbers make placement harder,
higher numbers make it easier. Sectors also have a title and sometimes rules
text.

### Myths [Portrait]
Each myth has a faction and a number, from 1 to ~6. Lower numbers are better
for expansion, higher numbers are better for war. Myths also have a title and
sometimes rules text.

### Cities [Disks]
Cities are represented by colored wooden disks, and are stacked between sectors
so that each city can be adjacent to at most two sectors and the edge of each
sector can have at most one stack of cities. When stacked, the city on top is
the _ruling_ city, and that city's faction is the _ruling_ faction.

![Nate Marcel](https://camo.githubusercontent.com/0ed4c7dda939eefe38cd659dd866ed62bad31b86/68747470733a2f2f312e62702e626c6f6773706f742e636f6d2f2d77434754474e436b4663512f574f30565a2d52373659492f41414141414141415173592f53635a5843596f6f6e56304b486c374f7361493468394f564c4e53477864706b67434c63422f73313630302f6465736572742d6e696768742d74696e792d6c616e6473636170652e6a7067)

## Setup
1. Put each faction's history marker on the track at 6.
2. Set the faction cities and influence tokens aside.
3. Choose a starting sector at random.
4. Shuffle up the remaining cards and deal out hands of seven to each player.
5. Flip the top card of the deck over to make a discard pile.
6. Choose a starting player at random. [TODO: Balance?]

![Ian McQue](https://camo.githubusercontent.com/786d55c10b6c9ced8f6295d823045da7e767ff47/68747470733a2f2f7062732e7477696d672e636f6d2f6d656469612f4333314b467774574d4141376d65742e6a7067)

## Play
Players take turns until at least one faction has reached the end of the
history track, and then score their influence and cards.

On a turn, choose one:

- Play a card for one of several effects.
- Buy a card for influence.
- Fight a war and perhaps gain influence.
- Recover your hand and sell down to your hand size.

### Play a Card
Sectors and myths play differently:

- When you *play a sector,* choose where to place it on the map. If you place
  next to at least one city, choose a ruling faction next to your new sector
  and gain influence equal to its place on the history track. Flip the top of
  the deck into the discard pile. Then take another turn.
- When you *play a myth to expand,* take a city of its faction from off-board
  and place it at the edge of a sector. For that city and everything under it,
  increase the corresponding faction's value on the history track. Put the myth
  in your tableau.
  - If there's already a city of that faction on the map, you must share a
    sector with it.
  - The number on each adjacent sector must be at least the number on the myth.
  - The height of the city must be at most the number on the myth.
  - If there are no free cities to place, you cannot take this action.

### Buy a Card
Pay influence to take a card from the top of the deck or the discard pile and
put it into your hand.

- From the deck, purchase unseen at the second-highest faction's value on the
  history track.
- From _anywhere_ in the discard pile, purchase a sector at twice the number of
  sectors on the map, or a myth at the faction's value on the history track.

### Fight a War
Play cards to destroy cities, then collect influence.

- Choose a sector next to at least one city.
- All players choose a card from their hands and simultaneously reveal and
  place in their tableau.
- Add the number of ruling cities at the sector to the numbers on matching
  revealed cards; the faction(s) with the highest total is/are the winner(s).
- Destroy each non-winning city (ruling or not): they're free to be placed again.
- For each winning faction card in their tableau, players gain the sector's
  value.

### Recover your Hand
Put all the cards in your tableau back into your hand. Then sell cards for
influence until you get back down to seven cards.

- For sectors, this is twice the number of sectors on the map.
- For myths, this is the faction's value on the history track.

![Sergey Kolesov](https://camo.githubusercontent.com/be60e6c36aaace972918c0cdb6e51ea7a063261a/68747470733a2f2f7062732e7477696d672e636f6d2f6d656469612f433337584f306457514141636b48632e6a7067)

## Game End and Victory
When a faction hits the end of the history track, the game ends at the end of
that turn.

Players recover tableaus and sell all the cards in their hands, then the player
with the most influence wins. In the case of a tie, the tied player who would
take the next turn wins.

![Victor Mosquera](https://camo.githubusercontent.com/72edbdc675924826863c50e42de0b7be3a0da0f8/68747470733a2f2f7062732e7477696d672e636f6d2f6d656469612f43374a63657855586b4155716f6f7a2e6a7067)
