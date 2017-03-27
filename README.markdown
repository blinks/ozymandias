# Ozymandias
> And on the pedestal these words appear:  
> ’My name is Ozymandias, king of kings:  
> Look on my works, ye Mighty, and despair!’  
> Nothing beside remains.  
> — Percy Bysshe Shelley, Ozymandias

See PLAYTESTING.md for print-and-play information.

## Components
* A black obelisk to mark the first player in each age.
* A deck of cards in three suits (gold, red, blue).
* Sector tiles for the modular galaxy map, with paths and intersections,
  hazards (black dots), and colonies (shapes).
* A collection of resource cubes (red strength, gold wealth, blue secrets).
* For each player:
  * A set of four fleet pawns.
  * A set of eight disks.

## Game Setup
1. Shuffle the cards and sector tiles.
2. Place one sector tile in the middle of the table.
3. Have each player choose a set of fleet pawns and disks.
4. Give one player the obelisk -- they’ll take the first action.
5. Give each player seven cards and one of each resource.

## Game Sequence
Ozymandias is played in a sequence of ages.  Each age consists of two parts:
planning and execution.  The planning stage happens simultaneously, as each
player decides what they want to do.  Execution rolls those plans out one
activation at a time.

### Planning
Untap all your leaders.

In each age after the first, draw two cards.  Pay secrets to draw additional
cards: one for the first, two for the second, three for the third.

Choose one card as your new leader for this age, and place a new fleet on it.
This card's ability will be revealed when that fleet is warped in, and will
be connected to that fleet for the rest of the game.

Place any number of cards face-down (landscape) under each leader.  These
cards can be revealed to gather resources during the age (see: Harvest).

### Execution
Take turns activating a fleet or passing until all players have passed.

When you activate a fleet, it gets one action.  You cannot activate a fleet
with a tapped leader card.  If it's off-map (on the leader card or an
exploring sector), warp it in:

- When you warp in from your card, put it on any location that doesn't
  contain a fleet or an enemy-controlled colony.
- When you warp in from an explored sector, reveal and place that sector
  tile, gain a resource for each colony (of that type), and place your fleet
  on any location on that tile.

When you pass, tap all your fleet cards.  If you were the first player to
pass, take the obelisk (first player marker).  Once all players have passed,
begin the next age.

#### Action: Move
Move this fleet.

- You may move as far as you like along a single unbroken line.
- Pay no wealth when you hit an intersection; you may stop or continue in the
  same direction for free, or a different direction for one wealth.
- Pay one wealth when you hit a hazard or a colony; then you may continue in
  any direction.
- Pay one wealth when you hit a friendly fleet; then you _must_ continue in
  any direction.
- *Skirmish*: If your final location is occupied by an enemy fleet, there is
  a skirmish.  See below.
- *Exploration:* If you move off the edge of the galaxy, take a face-down
  sector tile and put the fleet on it.  If there are no more sector tiles,
  put the fleet back on its leader card.  Either way, tap the leader card
  (this fleet cannot be activated again this age).

#### Action: Conquer
Pay strength equal to one plus the number of disks in this fleet's location
and place a disk on this fleet's location.

- You may only conquer colonies.
- You may take one of your disks from anywhere if you've run out of your
  pool.

#### Action: Harvest
Reveal a face-down card under this fleet and gain resources equal to its
rank, based on its suit.  Then give that card to an opponent.

* A [gold] card gathers wealth, which is spent to move.
* A [red] card gathers strength, which is spent to conquer and reinforce.
* A [blue] card gathers secrets, which is spent to alter and draw cards.

*Secret Plans:* Any time you reveal a card, you may spend secrets equal to
half its rank (rounded down) to transform it into any suit.

*Emergency Resources:* At any time, you may discard a card to gain one
resource of _any_ type.

## Skirmish
Players will add strength to their fleets, then play cards until one decides
to retreat and take losses.  The active fleet is the attacker, the other
fleet is the defender.

1. Reinforcement: Both you and the defending player secretly choose and then
   reveal any amount of strength to add to your fleets.
2. Initiative:  The difference between the total fleet strengths is called
   the initial score. This score is negative for the player inferior in fleet
   strength, and that player has the initiative.
3. The player with the initiative may play a single card or accept defeat.
   - To play a card, it must match the suit of your fleet or you must also
     pay a secret to make it match.  Discard that card and add its rank to
     your score.
   - If you're now zero or positive, initiative changes.  Otherwise, you
     retain initiative.  Either way, continue this step.
4. If the skirmish ends in a tie, nothing else happens.  Otherwise, the
   losing fleet loses strength equal to the final score.
5. If there is strength loss left over, the winner moves the losing fleet as
   if spending wealth equal to the difference.
   - The losing fleet may be forced to explore (and become tapped) in this
     way, but cannot be forced to skirmish.
   - The losing fleet may not backtrack.
   - If the losing fleet is moved _out_ of a habitable location, the winner
     may conquer that location.

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
