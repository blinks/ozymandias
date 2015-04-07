# Ozymandias game API

from google.appengine.api import users
from google.appengine.ext import ndb

import csv
import json
import random
import webapp2

class Card(ndb.Model):
  name = ndb.StringProperty('n')
  color = ndb.StringProperty('c')
  text = ndb.StringProperty('t')

  def json(self):
    return {
      'name': self.name,
      'color': self.color,
      'text': self.text,
      }


class Immortal(ndb.Model):
  owners = ndb.StringProperty('u', repeated=True)
  bank = ndb.IntegerProperty('g', default=9)
  hand = ndb.LocalStructuredProperty(Card, 'h', repeated=True)
  discard = ndb.LocalStructuredProperty(Card, 'x', repeated=True)
  dead = ndb.StringProperty('p', repeated=True)

  def json(self):
    return {
      'owners': self.owners,
      'bank': self.bank,
      'hand': [c.json() for c in self.hand],
      'discard': [c.json() for c in self.discard],
      'dead': self.dead,
      }


class Sector(ndb.Model):
  q = ndb.IntegerProperty('q', required=True)
  r = ndb.IntegerProperty('r', required=True)
  value = ndb.IntegerProperty('v', required=True)
  gems = ndb.IntegerProperty('g', default=0)
  stack = ndb.StringProperty('s', repeated=True)

  def json(self):
    return {
      'q': self.q,
      'r': self.r,
      'value': self.value,
      'gems': self.gems,
      'stack': self.stack,
      }


class Game(ndb.Model):
  immortals = ndb.LocalStructuredProperty(Immortal, 'i', repeated=True)
  deck = ndb.LocalStructuredProperty(Card, 'd', repeated=True)
  market = ndb.LocalStructuredProperty(Card, 'm', repeated=True)
  tiles = ndb.IntegerProperty('t', repeated=True)
  galaxy = ndb.LocalStructuredProperty(Sector, 's', repeated=True)
  pool = ndb.LocalStructuredProperty(dict, 'p')
  created = ndb.DateTimeProperty(auto_now_add=True)
  updated = ndb.DateTimeProperty(auto_now=True)

  @classmethod
  def create(cls):
    """Set up a new game object."""
    # TODO: Support other player counts.
    immortals = [ Immortal(), Immortal() ]

    deck = [Card(name=c['name'], color=c['color'], text=c['text'])
        for c in csv.DictReader(open('cards.csv'))]
    random.shuffle(deck)
    market, deck = deck[:3], deck[3:]
    for i in immortals:
      i.hand, deck = deck[:3], deck[3:]

    tiles = [0]*2 + [1]*8 + [2]*6 + [3]*4 + [4]*2
    random.shuffle(tiles)
    galaxy = [ Sector(q=0, r=0, value=tiles.pop()), ]

    pool = {'white': 6, 'black': 6, 'red': 6, 'blue': 6}
    return Game(immortals=immortals,
        deck=deck, market=market,
        tiles=tiles, galaxy=galaxy, pool=pool)

  def json(self):
    return {
      'immortals': [i.json() for i in self.immortals],
      'deck': [c.json() for c in self.deck],
      'market': [c.json() for c in self.market],
      'tiles': self.tiles,
      'galaxy': [s.json() for s in self.galaxy],
      'pool': self.pool,
      }


class GameApi(webapp2.RequestHandler):
  def get(self):
    self.response.headers['Content-Type'] = 'application/json'
    self.response.write(json.dumps(Game.create().json()))

  def post(self):
    pass  # save game state?

app = webapp2.WSGIApplication([
  ('/api/game', GameApi),
], debug=True)
