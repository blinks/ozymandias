#!/bin/sh
# Release the rules to the gh-pages branch.

asciidoctor README.asciidoc
git checkout gh-pages
mv README.html index.html
git add index.html
