'''
Rebuild footer.
The footer text consists of the statement below, as well as a html-formatted
variant of CONTRIBUTORS.md.


'''

import os
import re
import time

statement = '''
Source Serif is an open-source typeface for setting text in many sizes,
weights, and languages. The design of Source Serif represents a contemporary
interpretation of the transitional typefaces of
<a href="https://en.wikipedia.org/wiki/Pierre_Simon_Fournier">
Pierre-Simon Fournier</a>.
Additionally, Source Serif has been conceived as a friendly companion to
Paul D. Hunt’s
<a href="https://adobe-fonts.github.io/source-sans-pro/">
Source Sans</a>.

Source Serif supports the
<a href="https://github.com/adobe-type-tools/adobe-latin-charsets#adobe-latin-4">
Adobe Latin-4</a> character set, as well as
<a href="https://github.com/adobe-type-tools/adobe-cyrillic-charsets#adobe-cyrillic-2">
Cyrillic</a> and
<a href="https://github.com/adobe-type-tools/adobe-greek-charsets#adobe-greek-1">
Greek</a> writing systems.
With six weights in five optical sizes, the Source Serif family has a total of
60 styles, shared across Roman and Italic. In spite of this impressive bouquet,
a browser that supports variable fonts will only load two font files for this
specimen.

Source Serif was designed by Frank Grießhammer, with contributions by
Reymund Schroeder, Emilios Theofanous, Thomas Thiemich, and Irene Vlachou.

Significant extensions of this project (italics for Greek, optical sizes) were
made possible through support from
<a href="https://design.google/library/variable-fonts-are-here-to-stay/">
Google Fonts</a>.
'''

person_template = '''\
<li><a href="{url}">{name}</a><br><p class="indent">{role}</p></li>'''


def refresh():
    txt_file = os.path.join(
        os.path.dirname(__file__), '../../CONTRIBUTORS.md')
    footer_html = os.path.join(
        os.path.dirname(__file__), '../_includes/footer.html')
    with open(txt_file, 'r') as f:
        txt_data = f.read()

    # build HTML output starting with the statement from above
    html_output = ['<div class="opsz_smtext">']

    statement_paragraphs = statement.split('\n\n')
    for paragraph in statement_paragraphs:
        html_output.append(
            f'<p class="para_padding" lang="en">{paragraph}</p>')

    # parse CONTRIBUTORS.md for persons
    rx_person = re.compile(
        # rx named subgroups:
        # https://docs.python.org/3/library/re.html#re.Match.groupdict
        r'\[(?P<name>.+?)\]\((?P<url>.+?)\)\s+?\n\t(?P<role>.+?) \((?P<time>.+?)\)',
        re.MULTILINE)

    person_dicts = [m.groupdict() for m in re.finditer(rx_person, txt_data)]
    contributors = {}
    for p_dict in person_dicts:
        # organize contributors by last name
        last_name = p_dict['name'].split()[-1]
        contributors[last_name] = p_dict

    html_output.extend([
        '<h5>credits</h5>',
        '<ul>'])

    for last_name, group_dict in sorted(contributors.items()):
        html_output.append(person_template.format(**group_dict))

    html_output.append('</ul>')

    year = time.gmtime().tm_year
    html_output.append(
        '<h5><span style="vertical-align: -0.05em;">©</span> '
        f'Adobe 2014 – {year}</h5></div>\n')

    with open(footer_html, 'w') as footer:
        footer.write('\n'.join(html_output))


if __name__ == '__main__':
    refresh()
