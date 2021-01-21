'''
Rebuild all html files to be included in the main site
'''

import os
import random

iso_languages = {
    # https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes
    'az': 'Azerbaijani',
    'be': 'Belarusian',
    'bg': 'Bulgarian',
    'cs': 'Czech',
    'de': 'German',
    'el': 'Greek',
    'en': 'English',
    'eo': 'Esperanto',
    'es': 'Spanish',
    'et': 'Estonian',
    'eu': 'Basque',
    'fi': 'Finnish',
    'fr': 'French',
    'hu': 'Hungarian',
    'kk': 'Kazakh',
    'lv': 'Latvian',
    'pl': 'Polish',
    'pt': 'Portuguese',
    'ru': 'Russian',
    'se': 'Swedish',
    'sk': 'Slovak',
    'sr': 'Serbian',
    'uk': 'Ukrainian',
    'vi': 'Vietnamese',
}

article_template = '''
<h3 contenteditable lang="{lang_tag_a}">{header}</h3>
<h4 contenteditable lang="{lang_tag_a}">{subhead}</h4>

<p contenteditable class="opsz_text">
{content}</p>

<div class="columns opsz_caption">
<p class="hide_on_mobile" contenteditable>
{content_caption}</p>

<p lang="en">
This text comes from the
<a href="{url_a}">{language_a}</a>
and
<a href="{url_b}">{language_b}</a>
Wikipedia pages about the {animal}.
It was assembled in Winter 2020/21, and lightly edited for typography.
</p>
</div>
'''


def text_files_to_html(animal, txt_files):
    '''
    Combine one or more text files to a single html <article>.

    The input file names identify the animal name and text language
    (ISO codes) -- e.g.
        anteater-fi.txt
        anteater-ru.txt

    The structure within the text files is very simple:
    header, subhead, content and URL are separated by double line breaks.

    The resulting html code will toggle from one language to another within
    the body text. In 30% of the cases, Italics are set for a paragraph
    (random choice).

    '''
    # hold all data for multiple languages
    cmb_dict = {}

    for txt_file in txt_files:
        txt_file_basename = os.path.basename(txt_file)
        animal, lang_tag = os.path.splitext(txt_file_basename)[0].split('-')
        with open(txt_file, 'r') as f:
            data = f.read()

        cmb_dict.setdefault('lang_tags', []).append(
            lang_tag)
        cmb_dict.setdefault('language', []).append(
            iso_languages.get(lang_tag, 'no language'))

        header, subhead, content, url = data.split('\n\n')
        cmb_dict.setdefault('header', []).append(header)
        cmb_dict.setdefault('subhead', []).append(subhead)
        cmb_dict.setdefault('content', []).append(content)
        cmb_dict.setdefault('url', []).append(url.strip('\n'))

    # Randomly assign language a and b.
    # choice_b is a bit more complex in case there are more than 2 text
    # files for the given animal.
    options = range(len(txt_files))
    choice_a = random.choice(options)
    choice_b = next((i for i in options if i is not choice_a), choice_a)

    lang_tag_a = cmb_dict['lang_tags'][choice_a]
    lang_tag_b = cmb_dict['lang_tags'][choice_b]

    content_a = cmb_dict['content'][choice_a].split('\n')
    content_b = cmb_dict['content'][choice_b].split('\n')

    if len(txt_files) > 1:
        # more than 1 languages exist for this animal
        content_body = ''
        content_caption = ''

        for p_index, paragraphs in enumerate(
            list(zip(content_a, content_b))
        ):
            # make body text in which paragraphs alternate by language
            paragraph_a, paragraph_b = paragraphs

            # set some paragraphs to be italic
            if random.random() <= .3:
                italic_toggle_open = '<i>'
                italic_toggle_close = '</i>'
            else:
                italic_toggle_open = ''
                italic_toggle_close = ''

            # set alternating language for even and odd lines
            # at the same time, add the “leftover” paragraph to the
            # caption content
            if p_index % 2 == 0:
                content_body += '{}<span lang="{}">{}</span>{}\n'.format(
                    italic_toggle_open,
                    lang_tag_b, paragraph_b,
                    italic_toggle_close)
                content_caption += (
                    '<span lang="{}">{}</span>\n'.format(
                        lang_tag_a, paragraph_a))
            else:
                content_body += '{}<span lang="{}">{}</span>{}\n'.format(
                    italic_toggle_open,
                    lang_tag_a, paragraph_a,
                    italic_toggle_close)
                content_caption += (
                    '<span lang="{}">{}</span>\n'.format(
                        lang_tag_b, paragraph_b))

    else:
        # only one language exists for this animal
        content_body = '\n'.join(content_a)
        content_caption = '\n'.join(content_a)

    output_dict = {}
    output_dict['animal'] = animal.title()
    output_dict['header'] = cmb_dict['header'][choice_a]
    output_dict['subhead'] = cmb_dict['subhead'][choice_a]
    output_dict['lang_tag_a'] = lang_tag_a
    output_dict['lang_tag_b'] = lang_tag_b
    output_dict['language_a'] = iso_languages.get(lang_tag_a)
    output_dict['language_b'] = iso_languages.get(lang_tag_b)
    output_dict['url_a'] = cmb_dict['url'][choice_a]
    output_dict['url_b'] = cmb_dict['url'][choice_b]
    output_dict['content'] = content_body
    output_dict['content_caption'] = content_caption

    html_file_name = animal.replace(' ', '_') + '.html'
    output_path = os.path.normpath(os.path.join(
        os.path.dirname(__file__), '../_includes', html_file_name))
    html_data = article_template.format(**output_dict)
    with open(output_path, 'w') as htmlfile:
        htmlfile.write(html_data)


def refresh():
    '''
    find text files in the content directory, and use them to refresh
    the HTML files in the ../_includes directory
    '''
    animals = {}
    content_dir = os.path.abspath(
        os.path.join(os.path.dirname(__file__), '../content'))
    for file in os.listdir(content_dir):
        if os.path.splitext(file)[-1].lower() == '.txt':
            file_path = os.path.join(content_dir, file)
            animal, _ = os.path.splitext(file)[0].split('-')
            animals.setdefault(animal, []).append(file_path)

    print('animals found:')
    for animal, text_files in sorted(animals.items()):
        print('❤️ ' + animal.title())
        text_files_to_html(animal, text_files)


if __name__ == '__main__':
    refresh()
