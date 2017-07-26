#!/usr/bin/env sh

family=SourceSerifPro
romanWeights='ExtraLight Light Regular Semibold Bold Black'

# clean existing build artifacts
rm -rf target/
otfDir="target/OTF"
ttfDir="target/TTF"
mkdir -p $otfDir $ttfDir

for w in $romanWeights
do
  font_path=Roman/Instances/$w/font
  makeotf -f $font_path.ufo -r -o $otfDir/$family-$w.otf
  makeotf -f $font_path.ttf -r -o $ttfDir/$family-$w.ttf -ff $font_path.ufo/features.fea
done
