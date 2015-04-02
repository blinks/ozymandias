# ∂t: The Playtester's Rise Webapp

- Holds game state so it can be referenced on the web at any time.
- Hands are ACL'd to players.
- Moves are logged (Command pattern) both to provide a record of the game and
  make it easier to work bids into a pseudo-barrier.  (Active command could be
  an auction, for instance.)
