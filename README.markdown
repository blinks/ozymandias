# Ozymandias
> And on the pedestal these words appear:  
> ’My name is Ozymandias, king of kings:  
> Look on my works, ye Mighty, and despair!’  
> Nothing beside remains.  
> — Percy Bysshe Shelley, Ozymandias

Ozymandias is a game for two to six players ruling galaxy-spanning
civilizations.  The game takes about twenty minutes per experienced player
across four rounds (ages).

(See PLAYTESTING.md for print-and-play information.)

## Components
- A black obelisk to mark the first player in each age.
- A collection of resource cubes.
- A deck of cards.
- A set of sector tiles.
- For each player:
  - A set of four fleet pawns.
  - A set of eight disks.

### The Resources
There are three suits of resources:

- *Wealth* (gold circles) is spent to grant additional actions.  Whenever you
  activate a fleet, you turn it sideways to mark it exhausted.  At the
  beginning of your turn, you can pay wealth to recover all your fleets.
- *Population* (red squares) is spent to conquer or drafted into war.  While
  you hold population in reserve, you can spend it however you wish.  Once
  population has been drafted into a fleet, it may no longer occupy a colony.
- *Secrets* (blue triangles) alter and draw cards.  Without secrets, your
  options dwindle -- you're restricted to the suits in your hand, and draw
  fewer cards when the next age begins.

### The Cards
Each card has a suit and a rank, which determines their value in war and
harvest.  Cards have three uses:

- As a *Leader*, apply its title and rules text to its fleet.
- As a *Sword*, add it to your fleet's strength in war, and discard it.
- As a *Plowshare*, gain resources in its suit, and give it away.

Card ranks go from two to seven, and determine the card's strength as a sword
or plowshare.  Higher ranks also tend to have stronger rules text.

You may spend a card as an *emergency resource* of any suit.  This should
often only be used as a last resort.

### The Sectors
Each sector has a suit, reflected in the symbol used for one to three
colonies on the sector, along with the color of the border around the
outside.

Sectors have lines running through them as well.  These are the paths your
fleets can take during movement.  Fleets can stop only at intersections,
colonies, or hazards (the black dots).  All legal stopping points are on
exactly one sector -- the suit you stop in is important for war.

The colonies on a sector can be occupied by multiple players.  When a player
conquers a colony, they place a disk on top of any already there.  The more
disks on a colony, the harder it is to conquer again.  The player who
controls the most colonies at the end of the game is the winner.

## Game Setup
1. Shuffle the cards and sector tiles.
2. Place one sector tile in the middle of the table.
3. Have each player choose a set of fleet pawns and disks.
4. Give one player the obelisk -- they’ll take the first action.
5. Give each player seven cards and one of each resource.

## Game Sequence
Ozymandias is played over four rounds, called "ages".  At the beginning of
each age, players choose a new leader and decide what cards they're willing
to trade for resources.  Once all players are ready, they all take turns
activating fleets or passing until everyone has passed.  Then the next age
begins.

### Planning
*In each age after the first, recover all your leaders and draw two cards.*
You may pay secrets to draw additional cards: one for the first, two for the
second, three for the third.

*Choose one card as your new leader for this age, and place a new fleet on
it.*  This card will be revealed when that fleet is activated, and will be
connected to that fleet for the rest of the game.

*Place any number of cards face-down under each leader.*  These cards can be
revealed and given away to gain resources during the age when the associated
fleet is activated.

### Execution
Take turns activating a fleet or passing until all players have passed.

You may not activate exhausted fleets.  At the beginning of your turn, you
may pay wealth to recover all your fleets: the first time in an age, this
costs one wealth.  The second time, two, and so on.  (Place wealth spent for
this to the side, so you can remember.)

When you activate a fleet, exhaust it.  That fleet gets one action.
If it's off-map (on the leader card or an exploring sector), warp it in
before taking your action:

- When you warp in from your card, put it anywhere that doesn't contain a
  fleet or an enemy-controlled colony.
- When you warp in from a sector its exploring, reveal and place that sector
  tile, gain a resource for each colony revealed, and place your fleet
  anywhere on that tile.

When you pass, you may not re-enter play this age.  If you were the first
player to pass, take the obelisk (first player marker).  Once all players
have passed, begin the next age.

#### Action: Move
Move this fleet, paying secrets to move further and change direction.

- You may move as far as you like along a single unbroken line.
- Hazards, colonies, and direction changes cost one secret for the first, two
  secrets for the second, and so on.
- When you hit an intersection, you may stop or continue in the same
  direction for free, but changing direction costs secrets.
- When you hit a hazard or a colony, pay secrets, but then you may continue
  in any direction.
- When you hit a friendly fleet, pay secrets, then you _must_ continue in any
  direction.
- *War*: If your final location is occupied by an enemy fleet, stop in the
  last legal intersection, hazard, or colony, and resolve a war.  If you
  force a retreat of at least one move, finish your movement on that space.
- *Exploration:* If you move off the edge of the galaxy, take a face-down
  sector tile and put the fleet on it.  If there are no more sector tiles,
  put the fleet back on its leader card.  (The next time this fleet is
  activated, it'll warp in as a free action.)

#### Action: Conquer
Pay population from your reserves equal to one plus the number of disks on
this fleet's location and place one of your own disks on top.  Then draw a
card.

- You may only conquer colonies.
- You may take one of your disks from anywhere if you've run out of your
  pool.

#### Action: Harvest
Reveal a face-down card under this fleet and gain resources equal to its
rank, based on its suit.  Then give that card to an opponent.

*Secret Plans:* Any time you reveal a card, you may spend secrets equal to
half its rank (rounded down) to transform it into any suit.

## War
Players will draft population into to their fleets, then play cards until one
decides to retreat and take losses.  The active fleet is the attacker, the
other fleet is the defender.

1. Reinforcement: Both you and the defending player secretly choose and then
   reveal any amount of population from your reserves to add to your fleet
   strengths.
2. Initiative: Whoever has the lower fleet strength starts with the
   initiative. If tied, the active player starts with it. The difference in
   strengths is your current *score*, which is negative for the player with
   the initiative.
3. The player with the initiative may play a single card or accept defeat.
   - To play a card, it must match the suit your fleet occupies.  Discard
     that card, add it to your score, and subtract it from your opponent's
     score.
   - If you're now zero or positive, initiative changes.  Otherwise, you
     retain initiative.  Either way, continue this step.
4. If the war ends in a tie, nothing else happens.  Otherwise, the
   losing fleet loses strength equal to the final score.
5. If there is strength loss left over, the winner moves the losing fleet as
   if spending secrets equal to the difference.
   - The losing fleet may be forced to explore (and become tapped) in this
     way, but cannot be forced to fight a new war.
   - The losing fleet may not backtrack.
   - If the losing fleet is moved _out_ of a colony, the winner may conquer
     that colony for free.

*Secret Plans:* Any time you reveal a card, you may spend secrets equal to
half its rank (rounded down) to transform it into any suit.

## Victory
At the end of the fourth age, the player controlling the most colonies wins.

TODO(#44): Write a satisfying tie-breaker.

## Inspiration
* Friedrich and Maria for the skirmish system.
* 7 Ages for the action plotting system and [kinda] trade mechanism, which
  has since become the harvest action.
* Glory to Rome for cards as either simple actions or complex static effects.
* Cosmic Encounter for crazy powers and "last colony ends it" -- though the
  latter always ended on age 4, so that's now the rule.
* Race for the Galaxy for a tableau of powers triggered by actions.
