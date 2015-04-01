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
        'play', 'expand', 'auction', 'harvest' ], nargs='?')
    parser.add_argument('card', type=int, nargs='?')
    return parser.parse_args()

def main(args):
    # Create or open a game.
    if args.state and os.path.exists(args.state):
        game = yaml.load(open(args.state, 'r'))
    else:
        game = Game(load_cards())

    active = game.alpha
    if args.player == 'beta':
        active = game.beta
    if 'discard' not in active:
        active['discard'] = []

    # Execute that player's action.
    if args.action == 'play':
        c = active['hand'].pop(args.card)
        active['discard'].insert(0, c)
        print 'Play %s for event.' % c

    elif args.action == 'expand':
        c = active['hand'].pop(args.card)
        active['discard'].insert(0, active['hand'].pop(args.card))
        print 'Expand with %s.' % c
        # TODO: Sector draw and alter?

    elif args.action == 'auction':
        print 'Auction', game.market[args.card]

    elif args.action == 'harvest':
        c = active['hand'].pop(args.card)
        game.deck.append(c)
        print c
        # TODO: Compute color value?

    # Save game state.
    if args.action and args.state:
        yaml.dump(game, stream=open(args.state, 'w'))

    # Display game state.
    def show(cards, visible=True):
        if not visible:
            print ' ', '%s card(s).' % len(game.alpha['hand'])
        else:
            for i, card in enumerate(cards):
                print ' ', i, card

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
