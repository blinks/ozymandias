# Ozymandias
> And on the pedestal these words appear:  
> ’My name is Ozymandias, king of kings:  
> Look on my works, ye Mighty, and despair!’  
> Nothing beside remains.  
> — Percy Bysshe Shelley, Ozymandias

Ozymandias is a card game for two to four players.

(See PLAYTESTING.md for print-and-play information.)

![https://camo.githubusercontent.com/f511cda35cc1bf6888a94062e1dd84f19e65b385/68747470733a2f2f7062732e7477696d672e636f6d2f6d656469612f4333375850725757494145307245352e6a7067](On a litter.)

## Components
- ~16 Sector cards.
- ~12 Myth cards, ~6 cities, and a history marker for each faction.
- A history track card (6, 8, ..., 24, 26, 30).
- Influence tokens in several denominations.

![https://camo.githubusercontent.com/0ed4c7dda939eefe38cd659dd866ed62bad31b86/68747470733a2f2f312e62702e626c6f6773706f742e636f6d2f2d77434754474e436b4663512f574f30565a2d52373659492f41414141414141415173592f53635a5843596f6f6e56304b486c374f7361493468394f564c4e53477864706b67434c63422f73313630302f6465736572742d6e696768742d74696e792d6c616e6473636170652e6a7067](Through the desert.)

## Setup
1. Put each faction's history marker on the track at 6.
2. Set the faction cities and influence tokens aside.
3. Choose a starting sector at random.
4. Shuffle up the remaining cards and deal out hands of seven to each player.
5. Flip the top card of the deck over to make a discard pile.
6. Choose a starting player at random. [TODO: Balance?]

![https://camo.githubusercontent.com/786d55c10b6c9ced8f6295d823045da7e767ff47/68747470733a2f2f7062732e7477696d672e636f6d2f6d656469612f4333314b467774574d4141376d65742e6a7067](Ships landing.)

## Play
Players take turns until at least one faction has reached the end of the
history track, and then score their influence and whatever's in their hand.

On a turn, choose one:

- Play a card for one of several effects.
- Sell a card and gain influence.
- Fight a war and perhaps gain influence.
- Recover your hand and perhaps buy cards.

### Play a Card
Sectors and myths play differently, and myths often have two potential uses.

- When you *play a sector,* choose where to place it on the map. If you place
  next to at least one city, choose one and gain influence equal to that
  faction's place on the history track. Then take another turn.
- When you *play a myth to expand,* take a city from off the board and place
  it at the edge of a sector. For that city and everything under it, increase
  the corresponding faction's value on the history track. Put the myth in your
  tableau.
  - If there's already a city of that faction on the map, you must share a
    sector with it.
  - The number on the adjacent sectors must be at least the number on the myth.
  - The height of the city must be at most the number on the myth.
  - If there are no free cities to place, you cannot take this action.
- When you *play a myth for its event,* do what it says, then put it in your
  tableau.

### Sell a Card
Place the card onto the discard pile and gain its value in influence.

- For sectors, this is twice the number of sectors on the map.
- For myths, this is the faction's value on the history track.

### Fight a War
Play cards to destroy cities, then collect influence.

- Choose a sector next to at least one city, and take its action, if any.
- All players choose a card from their hands and simultaneously reveal.
- If any cards have a WAR effect, do what they say, then those cards go to each
  player's tableau.
- Add the number of ruling cities at the sector to the numbers on matching
  revealed cards; the faction(s) with the highest total is/are the winner(s).
- Destroy each winning city (ruling or not): they're free to be placed again.
- For each city destroyed, players gain influence equal to the number of
  cards for that faction in their tableau.

### Recover your Hand
Put all the cards in your tableau back into your hand. Then as long as you have
less than seven cards in your hand, you may buy cards from the top of the deck
or the discard pile.

- From the deck, purchase unseen at the second-highest faction's value on the
  history track.
- From _anywhere_ in the discard pile, purchase sectors at twice the number of
  sectors on the map, or myths at the faction's value on the history track.

![https://camo.githubusercontent.com/be60e6c36aaace972918c0cdb6e51ea7a063261a/68747470733a2f2f7062732e7477696d672e636f6d2f6d656469612f433337584f306457514141636b48632e6a7067](On a throne.)

## Game End and Victory
When a faction hits the end of the history track, the game ends at the end of
that turn.

Players sell the rest of the cards in their hand, then the player with the most
influence wins. In the case of a tie, the tied player who would take the next
turn wins.

![https://camo.githubusercontent.com/72edbdc675924826863c50e42de0b7be3a0da0f8/68747470733a2f2f7062732e7477696d672e636f6d2f6d656469612f43374a63657855586b4155716f6f7a2e6a7067](Aftermath.)
