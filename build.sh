#!/bin/sh

family=SourceSerifPro
weights='ExtraLight Light Regular Semibold Bold Black'

# clean existing build artifacts
rm -rf target/
mkdir target/ target/OTF/ target/TTF/

for w in $weights
do
  makeotf -f Roman/$w/font.ufo -r -o target/OTF/$family-$w.otf
  makeotf -f Roman/$w/font.ttf -r -o target/TTF/$family-$w.ttf
  rm Roman/$w/current.fpr # remove default options file from the source tree after building
done
