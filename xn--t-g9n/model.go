package ozymandias

import (
  "appengine/user"
  "encoding/csv"
  "log"
  "math/rand"
  "os"
)

type Color string
const (
  W Color = "white"
  K Color = "black"
  R Color = "red"
  B Color = "blue"
)

type State struct {
  Deck []Card
  Market []Card
  Map []Sector
  Tiles []int
  Pool map[Color]int
}

func MakeGame() *State {
  deck := make([]Card, 52)
  file, err := os.Open("cards.csv")
  if err != nil {
    log.Fatal(err)
  }

  rs, err := csv.NewReader(file).ReadAll()
  if err != nil {
    log.Fatal(err)
  }

  for i, r := range rs {
    deck[i] = Card{Color(r[0]), r[1], r[2]}
  }

  Shuffle(deck)
  return &State{
    Deck: deck,
    Pool: map[Color]int{ W: 6, K: 6, R: 6, B: 6 },
  }
}

func Shuffle(deck []Card) {
  for i := len(deck) - 1; i >= 0; i -= 1 {
    j := rand.Int() % (i + 1)
    deck[i], deck[j] = deck[j], deck[i]
  }
}

type Card struct {
  Color Color
  Name string
  Text string
}

type Player struct {
  Controller []*user.User
  Hand []Card
  Discard []Card
  Bank int
}

type Sector struct {
  X, Y int
  Natural, Invested int
  Stack []Color
}
