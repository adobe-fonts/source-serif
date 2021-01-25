This web specimen relies on Jekyll, which is automatically active on GitHub pages. The specimen does not need to be edited manually, but can be rebuilt using the Python files available in `/scripts`.

# \_includes

Various HTML files which are included in `index.html` through Jekyll’s `{% include %}` functionality. Most are created via `scripts/make_content.py`, except `footer.html`, which is built through `scripts/make_footer.py`.


# content

Text files in different languages which contain a headline, a subhead, body text, and a permalink. The content comes from the Wikipedia site the respective language, and was edited for better typography.


# fonts

All the fonts used on the specimen site.


# index.html

Scaffolding which holds the complete specimen site togeter.  
Built via `scripts/make_site.py`.


# scripts

These scripts are used to rebuild the complete web specimen.  
The web specimen consists of a static header, a combination of multi-lingual articles, and a footer.

### make_content.py – rebuild articles
Rebuild the HTML files in the `../_includes` folder.
The content of the individual articles is fed through the text files in `../content/`. For each article, two content files in different languages exist.

The content is split up into a headline, subhead, body text and caption text. Paragraphs are shuffled by language (picked randomly). In the body text, some paragraphs are formatted to be italic (also randomly). Finally, links to the Wikipedia sources are added.

### make_footer.py – rebuild footer
The footer contains a short text about Source Serif, as well as a list of contributors. This list relies on the presence of the file `../../CONTRIBUTORS.md`. No randomization here.

### make_site.py – rebuild complete site
Rebuild the complete site.

- With option `-r`, external html files are re-built (same as calling `make_content.py`)
- With option `-s`, the articles are shuffled on the site.



# css files

### source-serif-static.css
`@font-face` rules for static fonts

### source-serif-variable.css
`@font-face` rules for variable fonts

### style.css
general styling for the specimen site
