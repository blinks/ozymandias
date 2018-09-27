# Ozymandias
> And on the pedestal these words appear:  
> ’My name is Ozymandias, king of kings:  
> Look on my works, ye Mighty, and despair!’  
> Nothing beside remains.  
> — Percy Bysshe Shelley, Ozymandias

Ozymandias is a card game for two to five players, gods overseeing the rise and
fall of galactic empires. Each uses their hand of cards to ensure that the
right empires are rising, and balances the short-term gain of war with the
long-term gain of cultivating growth.

Players don't control specific factions, they only hold some influence over
that faction based on the cards in their hand. Each faction can swing from one
player to another to another over the course of the game. In fact, you likely
won't know exactly who's winning the war of influence until the end, when cards
are revealed.

(See PLAYTESTING.md for print-and-play information.)
(Art credits and links [on the wiki](https://github.com/blinks/ozymandias/wiki).)

![Sergey Kolesov](https://camo.githubusercontent.com/f511cda35cc1bf6888a94062e1dd84f19e65b385/68747470733a2f2f7062732e7477696d672e636f6d2f6d656469612f4333375850725757494145307245352e6a7067)

## Components
- A bunch of hexagonal sector tiles.
- A bunch of Myth cards, cities, and one history marker for each faction.
- A history track card (6, 8, ..., 24, 26, 30).
- Influence tokens (money) in several denominations.

### Sectors [Landscape]
TODO: Now that these are tiles (#51), we need to differentiate somehow.

### Myths [Portrait]
Each myth has a faction (suit), title, text, and a rank, from 1 to ?. Higher
numbers are better in a crisis, but lower numbers will be worth more in the
vault.

### Cities [Disks]
Cities are represented by colored wooden disks, and are stacked on the corners
of sectors so that each city can be adjacent to three sectors and each edge of
each sector can have at most one stack of cities on one of its two corners.
When stacked, the city on top is the _ruling_ city, and that city's faction is
the _ruling_ faction.

![Nate Marcel](https://camo.githubusercontent.com/0ed4c7dda939eefe38cd659dd866ed62bad31b86/68747470733a2f2f312e62702e626c6f6773706f742e636f6d2f2d77434754474e436b4663512f574f30565a2d52373659492f41414141414141415173592f53635a5843596f6f6e56304b486c374f7361493468394f564c4e53477864706b67434c63422f73313630302f6465736572742d6e696768742d74696e792d6c616e6473636170652e6a7067)

## Setup
1. Put each faction's history marker on the track at 6.
2. Set the faction cities and influence tokens aside.
3. Put a random sector in the middle of the table.
4. Shuffle up the remaining cards and deal out hands of five to each player.
   Players start with no influence.
5. Choose a starting player at random.

![Ian McQue](https://camo.githubusercontent.com/786d55c10b6c9ced8f6295d823045da7e767ff47/68747470733a2f2f7062732e7477696d672e636f6d2f6d656469612f4333314b467774574d4141376d65742e6a7067)

## Play
Players take turns until at least one faction has reached the end of the
history track, and then score their influence and cards in their vault.

On a turn, choose one:

- Explore: Sell a card and place a sector.
- Expand: Play a card and place a city disk.
- Crisis: Pick up your tableau and bid on factions.

Then everyone with less than five cards in their hand and tableau combined must
buy a new card, placing it in their hand. (Start with the active player and
proceed clockwise.)

### Explore a sector
Discard a card to the market and take influence equal to its value on the
history track. Then draw a random sector.  Place that sector on the map,
adjacent to at least one city.

Take cards off the top of the deck equal to the sector's value and place them
in the market.

Each player may activate exploration effects matching each faction (suit)
adjacent to the newly-placed sector.

### Build a city
Play a card to your tableau and take a city of its faction from off-board. If
no cities of that faction remain, you cannot take this action.

Place that city at the corner of a sector. You may place on top of other
factions' cities -- only one stack of cities may be on any given corner, and
there must be at least one corner between any two stacks of cities.

Each player may activate expansion effects matching each faction (suit) in the
stack.

### Resolve a Crisis
*The Prelude*: Pick up any number of cards from your tableau and choose a
sector with at least one city on it.

*The Crisis*: Each player (in turn order, starting with the active player) may
contribute at most one card from their hand to the crisis, matching a faction
at that sector (no matter where it is in its stack).  Simultaneously reveal
cards and resolve revealed crisis effects. The highest rank (with each city at
that sector contributing a +1 bonus to matching cards' ranks) wins. If nobody
contributed a card, stop here -- no faction wins.

*The Aftermath*: All non-winning cities are destroyed, and the winning
faction(s) move up on the history track for each destroyed city. If no cities
were destroyed, winning faction(s) still move up once on the history track.

Finally, contributed cards that match a winning faction get placed face-down in
their player's vault, to be scored for their faction's value at the end of the
game. Non-matching cards go into their players' tableaus.

#### Buy a Card
At the end of each turn, if you have less than five cards combined in your hand
and tableau, you must buy a card: Pay influence to take a card from the top of
the deck or the discard pile and put it into your hand.

- From the deck, purchase sight-unseen at the second-highest faction's value on
  the history track.
- From _anywhere_ in the discard pile, purchase a myth at the faction's value
  on the history track.

If you must buy a card but don't have enough money to do so, the game ends and
you lose. Be careful if you're low on influence.

![Sergey Kolesov](https://camo.githubusercontent.com/be60e6c36aaace972918c0cdb6e51ea7a063261a/68747470733a2f2f7062732e7477696d672e636f6d2f6d656469612f433337584f306457514141636b48632e6a7067)

## Game End and Victory
When a faction hits the end of the history track, the game ends at the end of
that turn.

Players convert cards in their vaults into influence, then the player with the
most influence wins. In the case of a tie, the tied player who would take the
next turn wins.

![Victor Mosquera](https://camo.githubusercontent.com/72edbdc675924826863c50e42de0b7be3a0da0f8/68747470733a2f2f7062732e7477696d672e636f6d2f6d656469612f43374a63657855586b4155716f6f7a2e6a7067)
