#!/usr/bin/env python
# Assist in asynchronous play.

import glob
import itertools
import os.path
import random
import yaml

def parse_args():
    """Encapsulate command-line flags."""
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--state',
            help='path to the game state file')
    parser.add_argument('player', choices=[ 'alpha', 'beta' ])
    parser.add_argument('action', choices=[
        'event', 'expand', 'auction', 'harvest' ], nargs='?')
    parser.add_argument('card', type=int, nargs='?')
    return parser.parse_args()

def main(args):
    # Create or open a game.
    if args.state and os.path.exists(args.state):
        game = yaml.load(open(args.state, 'r'))
    else:
        game = Game(load_cards())

    if not game.sector_map:
        game.sector_map = []

    active = game.alpha
    if args.player == 'beta':
        active = game.beta
    if 'discard' not in active:
        active['discard'] = []

    # Execute that player's action.
    if args.action == 'event':
        c = active['hand'].pop(args.card)
        active['discard'].insert(0, c)
        print '%s plays %s for event.' % (args.player, c.name)

    elif args.action == 'expand':
        c = active['hand'].pop(args.card)
        active['discard'].insert(0, c)
        print '%s expands with %s, placing %s.' % (
                args.player, c.name, c.color)

        coord = input('Coordinates? ')
        if not isinstance(coord, tuple) or len(coord) != 2:
            raise SyntaxError

        for s in game.sector_map:
            if (s.x, s.y) == s:
                break
        else:
            s = Sector(game.sectors.pop())
            s.x, s.y = coord
            game.sector_map.append(s)
            print '  Exploration:', game.peek()[0]

        assert game.pool[c.color] > 0
        game.pool[c.color] -= 1
        s.stack.insert(0, c.color)
        active['bank'] += s.value + s.gems
        print '  [%s]' % s

    elif args.action == 'auction':
        print 'Auction', game.market[args.card].name

    elif args.action == 'harvest':
        c = active['hand'].pop(args.card)
        game.deck.append(c)
        val = 0
        for s in game.sector_map or []:
            if s.stack and s.stack[0] == c.color:
                val += s.value + s.gems
        print 'Harvest', c.name, 'for', val
        active['bank'] += val

    # Refresh the market.
    while len(game.market) < 4:
        game.market.extend(game.pop())

    # Display game state.
    def show(cards, visible=True):
        if not visible:
            print ' ', '%s card(s).' % len(game.alpha['hand'])
        else:
            for i, card in enumerate(cards):
                print ' ', i, card

    print
    print 'Alpha [%s]:' % game.alpha['bank']
    show(game.alpha['hand'], args.player == 'alpha')
    print ' Discard:'
    show(game.alpha.get('discard', []))
    print

    print 'Beta [%s]:' % game.beta['bank']
    show(game.beta['hand'], args.player == 'beta')
    print ' Discard:'
    show(game.beta.get('discard', []))
    print

    print 'Market:'
    show(game.market)
    print

    print 'Pool:', game.pool
    print 'Map:', game.sector_map

    if sum(game.pool.values()) == 0:
        print 'This will end the game.'
    if raw_input('Ok? (yN) ') == 'y':
        # Save game state.
        if args.action and args.state:
            yaml.dump(game, stream=open(args.state, 'w'))
        print 'Saved.'


class Card(yaml.YAMLObject):
    yaml_tag = u'!Card'

    def __init__(self, args):
        self.color = args['color'].strip().upper()
        self.name = args['name'].strip()
        self.text = args['text'].strip()

    def __repr__(self):
        return '%s [%s] %s' % (self.name, self.color, self.text)


class Sector(yaml.YAMLObject):
    yaml_tag = u'!Sect'

    def __init__(self, value):
        self.x = None
        self.y = None
        self.value = value
        self.gems = 0
        self.stack = []

    def __repr__(self):
        return '(%s, %s): %s=%s%s' % (
                self.x, self.y, self.stack, self.value,
                ('+%s' % self.gems) if self.gems else '')


class Game(yaml.YAMLObject):
    yaml_tag = u'!Game'

    def __init__(self, deck):
        self.create(deck)

    def create(self, deck):
        # Instantiate the deck and initial market.
        random.shuffle(deck)
        self.deck = deck
        self.market = self.pop(4)

        # Two players with three cards each and a bank of 9 gems.
        self.alpha = { 'hand': self.pop(3), 'bank': 9 }
        self.beta = { 'hand': self.pop(3), 'bank': 9 }

        # Sector map starts with an unexplored sector at the origin.
        self.sector_map = []
        self.sectors = [Sector(v) for v in
                [2 * (2 * [0] + 2 * [4] + 4 * [3] + 6 * [2] + 8 * [1])]]
        random.shuffle(self.sectors)

        # Initial disk count.
        self.pool = { 'W': 6, 'K': 6, 'R': 6, 'B': 6 }

    def pop(self, n=1):
        """Pop cards off the top of the deck."""
        cs, self.deck[:n] = self.deck[:n], []
        return cs

    def peek(self, n=1):
        """Reveal cards from the top of the deck."""
        return self.deck[:n]

    def push(self, cs):
        """Push cards to the bottom of the deck."""
        self.deck += cs


def load_cards():
    """Load cards from the data files."""
    colors = {
        './capsule/black.yaml': 'K',
        './capsule/blue.yaml': 'B',
        './capsule/red.yaml': 'R',
        './capsule/white.yaml': 'W',
    }

    cards = []
    for src in colors:
        cards += list(Card(dict(d, color=colors[src]))
                for d in yaml.load_all(open(src, 'r')))
    return cards


if __name__ == '__main__':
    main(parse_args())
