#!/usr/bin/env python
# Build the rulebook for release.

import csv
import glob
import os
import os.path
import subprocess
import yaml

def main():
    cards2csv()
    rev = git('rev-parse', '--short', '--verify', 'HEAD')
    asciidoctor(rev)
    git('checkout', 'gh-pages')
    os.rename('../index.html', './index.html')
    git('add', 'index.html')
    git('commit', '-m', 'Release v' + rev.strip())

def cards2csv():
    """Turn YAML card database into card CSV manifest."""
    out = csv.writer(open('cards.csv', 'w'))
    out.writerow(['color', 'name', 'text'])
    docs = None

    for f in glob.iglob('./capsule/*.yaml'):
        color = os.path.basename(f)[:-5]
        if color == 'unknown': continue
        with open(f, 'r') as y:
            docs = sorted(yaml.load_all(y),
                    key=lambda d: d['name'].replace('The ', ''))
        if not isinstance(docs[0], dict): continue
        for card in docs:
            try:
                out.writerow([color,
                    card.get('name', 'Untitled'),
                    card.get('text') ])
            except Exception as e:
                raise Exception(u'%s: %s -> %s' % (f, card, e))

def asciidoctor(rev):
    subprocess.check_output(['asciidoctor',
        '--attribute=revision=' + rev,
        '--destination-dir=..',
        '--out-file=index.html',
        'README.asciidoc'])

def git(*cmd):
    return subprocess.check_output(['git'] + list(cmd),
            stderr=subprocess.STDOUT)

if __name__ == '__main__':
    main()
