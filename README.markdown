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
* Sector tiles for the modular galaxy map.
* A collection of resource cubes (red strength, gold wealth, blue secrets).
* For each player:
  * A set of four fleet pawns.
  * A set of eight colonies.

## Game Setup
1. Shuffle the cards and sector tiles.
2. Place one sector tile in the middle of the table.
3. Have each player choose a set of fleet pawns and colonies.
4. Give one player the obelisk -- they’ll take the first action.
5. Give each player seven cards and one of each resource.

## Game Sequence
Ozymandias is played in a sequence of ages.  Each age consists of three
parts: planning, execution, and regroup.  The planning stage happens
simultaneously, as each player decides what they want to do.  Execution rolls
those plans out one activation at a time.  At the end of the age is all the
cleanup and some card draw.

### Planning
Choose one card as your new leader for this age, and place a new fleet on it.
This card's ability will be revealed when that fleet is activated, and will
be connected to that fleet for the rest of the game.

Place any number of cards face-down (landscape) under each leader.  These
cards can be revealed to gather resources during the age (see: Harvest).

### Execution
Take turns activating a fleet or passing until all players have passed.

To activate a fleet, pay wealth determined by how many times that fleet has
been activated this age.  The first activation costs one wealth, the second
two, the third three.  (A fleet may not be activated more than three times in
one age.)  When you activate a fleet, it gets three actions, which last until
either spent or the end of your activation.

To pass, remove the gold from your fleets and pick up any remaining face-down
cards.   If you were the first player to pass, take the obelisk (first player
marker).  You may no longer activate fleets this age.

Once all players have passed, continue to regroup.

#### Action: Harvest
Reveal a face-down card under this fleet and gain resources equal to its
rank, based on its suit.  Then give that card to an opponent.

* A [gold] card gathers wealth, which is spent to move.
* A [red] card gathers strength, which is spent to colonize and reinforce.
* A [blue] card gathers secrets, which is spent to alter and draw cards.

*Secret Plans:* Any time you reveal a card, you may spend secrets equal to
half its rank (rounded down) to transform it into any suit.

*Emergency Resources:* At any time, you may discard a card to gain one
resource of _any_ type.

#### Action: Warp
If this fleet is on its leader, place it onto any location without a fleet.

#### Action: Move
Move this fleet to an adjacent location.

- You may not move onto or through another fleet.
- You may not move off a sector (see: Explore).

#### Action: Explore
Move this fleet to an adjacent sector edge on the rim of the galaxy.

- It is exploring until a new sector is placed on that edge at the end of the
  age, and _may not be activated again this age._

#### Action: Colonize
Pay strength equal to one plus the number of colonies in this fleet's
location and place a colony in the active fleet's location.

- You may only colonize habitable locations.
- If you colonize a location where you already have a colony disk, move that
  disk to the top instead of placing an additional disk.

#### Action: Skirmish
Players will add strength to their fleets, then play cards until one decides
to retreat and take losses.  The winner controls the losing fleet for several
move / explore / colonize actions at the end of a skirmish.  _A skirmish
action ends your turn._

1. This fleet is the attacker.  Choose an adjacent enemy fleet as the
   defender.
2. Reinforcement: Both you and the defending player secretly choose and then
   reveal any amount of strength to add to your fleets.
3. Initiative:  The difference between the total fleet strengths is called
   the initial score. This score is negative for the player inferior in fleet
   strength, and that player has the initiative.
4. The player with the initiative may play a single card or accept defeat.
   - To *play a card*, it must match the suit of your fleet or you must also
     pay a secret to make it match.
   - Discard that card and add its rank to your score.
   - If you're now zero or positive, initiative changes.  Otherwise, you
     retain initiative.
   - Either way, continue with #4.
5. If the skirmish ends in a tie, nothing else happens.  Otherwise:
6. The losing fleet loses strength equal to the final score.
7. The winner moves the losing fleet a number of spaces equal to the final
   score.
   - The losing fleet may be forced to explore in this way.
   - The losing fleet may not backtrack, nor move through another fleet.
   - If the losing fleet is moved _out_ of a habitable location, the winner
     may pay strength _from the winning fleet_ to colonize that location
     (based on the number of disks there, as usual).

*Secret Plans:* Any time you reveal a card, you may spend secrets equal to
half its rank (rounded down) to transform it into any suit.

### Regroup
Clean up for the age in three steps.

1. *Exploration:* In turn order, each player draws sectors for each of their
   exploring fleets to land on.  Draw in fleet order if you have multiple
   exploring fleets.  If you can't place a sector on a fleet, put it back on
   its leader.  (You may warp it in next age.)
2. *Draw:* In turn order, each player may pay 0, 1, 3, or 6 secrets to draw
   2, 3, 4, or 5 cards.

## Victory
At the end of the fourth age, the player with the most ruling colonies (those
on top of a colony stack) wins.  If this is a tie, the player with the most
resources left wins.

## Inspiration
* Friedrich and Maria for the skirmish system.
* 7 Ages for the action plotting system and [kinda] trade mechanism.
* Glory to Rome for cards as either simple actions or complex static effects.
* Cosmic Encounter for crazy powers and “last colony ends it”.
* Race for the Galaxy for a tableau of powers triggered by actions.
