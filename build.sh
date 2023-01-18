#!/usr/bin/env sh

set -e

family=SourceSerif4
optical_sizes=(Caption SmText Text Subhead Display)
roman_weights=(ExtraLight Light Regular Semibold Bold Black)
italic_weights=(ExtraLightIt LightIt It SemiboldIt BoldIt BlackIt)

# get absolute path to bash script
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null && pwd )"

# clean existing build artifacts and rebuild output directories
rm -rf $DIR/target/OTF
rm -rf $DIR/target/TTF
otf_dir="$DIR/target/OTF"
ttf_dir="$DIR/target/TTF"
mkdir -p $otf_dir $ttf_dir

# copy LICENSE.md to the target folder
cp $DIR/LICENSE.md target/

function build_font {
	local slope=${1}
	local opsz=${2}
	local weight=${3}
	font_dir=$DIR/$slope/Instances/$opsz/$weight
	font_ufo=$font_dir/font.ufo
	ps_name=$family$opsz-$weight
	if [[ $opsz == 'Text' ]]
		# the 'Text' styles do not include their opsz name
		then ps_name=$family-$weight
	fi
	echo $ps_name
	echo "Building OTF ..."
	# -r is for "release mode" (subroutinization + applied glyph order)
	# -gs is for filtering the output font to contain only glyphs in the GOADB
	makeotf -f $font_ufo -r -gs -omitMacNames -o $font_dir/$ps_name.otf
	echo "Building TTF ..."
	otf2ttf $font_dir/$ps_name.otf
	echo "Componentizing TTF ..."
	ttfcomponentizer $font_dir/$ps_name.ttf
	# move font files to target directory
	mv $font_dir/$ps_name.otf $otf_dir
	mv $font_dir/$ps_name.ttf $ttf_dir
	echo "Done with $ps_name"
	echo ""
	echo ""
}

for s in ${optical_sizes[@]}
do
	for w in ${roman_weights[@]}
	do
		build_font Roman $s $w
	done
done

for s in ${optical_sizes[@]}
do
	for w in ${italic_weights[@]}
	do
		build_font Italic $s $w
	done
done
