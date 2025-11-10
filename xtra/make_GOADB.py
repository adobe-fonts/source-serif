'''
Takes no arguments, expects a masterGOADB file in repo root folder.
Distributes GlyphOrderAndAliasDB files into Roman/Italic subfolders.
'''

import re
from pathlib import Path


def run():
    italic_tag = '#-[italic]'
    roman_tag = '#-[roman]'
    script_name = Path(__file__).name
    edit_warning = (
        '# Please do not edit this GOADB. This file is built from a master GOADB,\n'
        f'# found in the _xtra folder of this repository, using {script_name}.\n'
    )

    script_path = Path(__file__)
    global_GOADB_path = script_path.parent / 'masterGOADB'
    root_path = script_path.parents[1]

    with open(global_GOADB_path, 'r') as goadb_blob:
        raw_mapping = goadb_blob.read().splitlines()

    raw_roman_GOADB = [
        line for line in raw_mapping if not line.startswith(italic_tag)]
    raw_italic_GOADB = [
        line for line in raw_mapping if not line.startswith(roman_tag)]

    roman_mapping = [edit_warning] + [re.sub(
        rf'{re.escape(roman_tag)} ?', '', line) for line in raw_roman_GOADB]
    italic_mapping = [edit_warning] + [re.sub(
        rf'{re.escape(italic_tag)} ?', '', line) for line in raw_italic_GOADB]

    with open(root_path / 'Roman/GlyphOrderAndAliasDB', 'w') as f:
        f.write('\n'.join(roman_mapping) + '\n')

    with open(root_path / 'Italic/GlyphOrderAndAliasDB', 'w') as f:
        f.write('\n'.join(italic_mapping) + '\n')


if __name__ == '__main__':
    run()
