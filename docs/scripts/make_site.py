'''
Rebuild complete index.html.

With option -r, external html files are re-built
With option -s, the content is re-shuffled on the site
'''

import os
import argparse
import random
import make_content
import make_footer

html_prologue = '''\
---
title: Source Serif 4
---

<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <meta name="format-detection" content="telephone=no">
        <title>Source Serif 4</title>
        <link rel="stylesheet" href="/style.css">
        <link rel="stylesheet" href="/source-serif-variable.css">
        <link rel="stylesheet" href="/source-serif-static.css">
    </head>
    <body class="dynamic_color">
        <header class="dynamic_color sticky">
            <h1><a class="dynamic_text_color" href="http://github.com/adobe-fonts/source-serif/releases/latest">
            Source Serif 4
            </a>
            </h1>
            <div class="header_links smcp">
                <a href="https://github.com/adobe-fonts/source-serif/tree/main">fork</a>
                &ensp;|&ensp;
                <a href="http://github.com/adobe-fonts/source-serif/releases/latest">fonts</a>
            </div>
        </header>
        <div class="spacer">
            &nbsp;
        </div>
        <main spellcheck="false">
'''

html_epilogue = '''\
        </main>
        <footer>
            {% include footer.html %}
        </footer>
    </body>
</html>'''

weights = [
    'ExtraLight',
    'Light',
    'Regular',
    'Semibold',
    'Bold',
    'Black',
]

article_tag_template = (
    '            <article class="{}">\n'
    '                <h2>{}</h2>\n'
    '                {{% include {} %}}\n'
    '            </article>\n'
)


def get_args():
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument(
        '-r', '--refresh',
        help='rebuild html includes',
        action='store_true',
    )

    parser.add_argument(
        '-s', '--shuffle',
        help='re-shuffle content on site',
        action='store_true',
    )

    return parser.parse_args()


args = get_args()
if args.refresh:
    make_content.refresh()

make_footer.refresh()

if args.shuffle:
    article_dir = os.path.join(os.path.dirname(__file__), '../_includes')
    animal_htmls = [
        file for file in os.listdir(article_dir) if
        os.path.splitext(file)[-1].lower() == '.html']
    random.shuffle(animal_htmls)

else:
    animal_htmls = [
        'capybara.html',
        'beaver.html',
        'anteater.html',
        'wombat.html',
        'sand_cat.html',
        'hedgehog.html',
        'iberian_lynx.html',
        'hamster.html',
        'raccoon.html',
        'flying_squirrel.html',
        'opossum.html',
        'ocelot.html',
    ]


html_output = html_prologue

for w_index, weight in enumerate(weights * 2):
    article_html = animal_htmls[w_index]
    html_output += article_tag_template.format(weight, weight, article_html)
html_output += html_epilogue

index_html = os.path.join(os.path.dirname(__file__), '../index.html')
with open(index_html, 'w') as html_out:
    html_out.write(html_output)
