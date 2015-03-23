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
    git('commit', '-m "Release v' + rev.strip() + '"', shell=True)

def cards2csv():
    """Turn YAML card database into card CSV manifest."""
    out = csv.writer(open('cards.csv', 'w'))
    out.writerow(['color', 'name', 'text'])
    docs = None

    for f in glob.iglob('./capsule/*.yaml'):
        color = os.path.basename(f)[:-5]
        with open(f, 'r') as y:
            docs = list(yaml.load_all(y))
        if not isinstance(docs[0], dict): continue
        for card in docs:
            out.writerow([color,
                card.get('name', 'Untitled'),
                card.get('text')
                ])

def asciidoctor(rev):
    subprocess.check_output(['asciidoctor',
        '--attribute=revision=' + rev,
        '--destination-dir=..',
        '--out-file=index.html',
        'README.asciidoc'])

def git(*cmd, **kwargs):
    return subprocess.check_output(['git'] + list(cmd),
            shell=kwargs.get('shell', False))

if __name__ == '__main__':
    main()
