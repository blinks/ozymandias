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
    parser.add_argument('command', choices=[
        'alpha', 'beta',
        ])
    return parser.parse_args()

def main(args):
    # Create or open a game.
    if args.state and os.path.exists(args.state):
        game = yaml.load(open(args.state, 'r'))
    else:
        game = Game(load_cards())
        if args.state:
            yaml.dump(game, stream=open(args.state, 'w'))

    # Display game info.

    print 'Alpha [%s]:' % game.alpha['bank']
    if args.command == 'alpha':
        for card in game.alpha['hand']:
            print ' ', card
    else:
        print ' ', '%s card(s).' % len(game.alpha['hand'])
    print

    print 'Beta [%s]:' % game.beta['bank']
    if args.command == 'beta':
        for card in game.beta['hand']:
            print ' ', card
    else:
        print ' ', '%s card(s).' % len(game.beta['hand'])
    print

    print 'Market:'
    for card in game.market:
        print ' ', card
    print

    print 'Pool:', game.pool

    print 'Ok.'


class Card(yaml.YAMLObject):
    yaml_tag = u'!Card'

    def __init__(self, args):
        self.color = args['color'].strip().upper()
        self.name = args['name'].strip()
        self.text = args['text'].strip()

    def __repr__(self):
        return '%s [%s] %s' % (self.name, self.color, self.text)


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
        self.sector_map = { (0, 0): None }
        self.sectors = 2 * ( 2 * [0] + 2 * [4] + 4 * [3] + 6 * [2] + 8 * [1])
        random.shuffle(self.sectors)

        # Initial disk count.
        self.pool = { 'W': 6, 'K': 6, 'R': 6, 'B': 6 }

    def pop(self, n):
        """Pop cards off the top of the deck."""
        cs, self.deck[:n] = self.deck[:n], []
        return cs

    def peek(self, n):
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
