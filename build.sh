#!/usr/bin/env sh

family=SourceSerifPro
roman_weights='ExtraLight Light Regular Semibold Bold Black'
italic_weights='ExtraLightIt LightIt It SemiboldIt BoldIt BlackIt'
fonttools_dir=~/code/fonttools

# clean existing build artifacts
rm -rf target/OTF
rm -rf target/TTF
otf_dir="target/OTF"
ttf_dir="target/TTF"
mkdir -p $otf_dir $ttf_dir

for w in $roman_weights
do
  font_dir=Roman/Instances/$w
  font_ufo=$font_dir/font.ufo
  ps_name=$family-$w
  echo $ps_name
  echo "Building OTF ..."
  # -r is for "release mode" (subroutinization + applied glyph order)
  # -gs is for filtering the output font to contain only glyphs in the GOADB
  makeotf -f $font_ufo -r -gs -o $font_dir/$ps_name.otf
  echo "Building TTF ..."
  otf2ttf $font_dir/$ps_name.otf -o $font_dir/$ps_name.ttf
  echo "Componentizing TTF ..."
  ttfcomponentizer $font_dir/$ps_name.ttf

  # move font files to target directory
  mv $font_dir/$ps_name.otf $otf_dir/
  mv $font_dir/$ps_name.ttf $ttf_dir/
  echo "Done with $ps_name"
  echo ""
  echo ""
done


for w in $italic_weights
do
  font_dir=Italic/Instances/$w
  font_ufo=$font_dir/font.ufo
  ps_name=$family-$w

  echo "Building OTF ..."
  makeotf -f $font_ufo -r -gs -o $font_dir/$ps_name.otf
  echo "Building TTF ..."
  otf2ttf $font_dir/$ps_name.otf -o $font_dir/$ps_name.ttf
  echo "Componentizing TTF ..."
  ttfcomponentizer $font_dir/$ps_name.ttf

  # move font files to target directory
  mv $font_dir/$ps_name.otf $otf_dir/
  mv $font_dir/$ps_name.ttf $ttf_dir/
  echo "Done with $ps_name"
  echo ""
  echo ""
done
