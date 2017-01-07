# Source Serif Pro

Source Serif Pro is a set of OpenType fonts to complement the [Source Sans Pro](https://github.com/adobe-fonts/source-sans-pro) family.
In addition to functional OpenType fonts, this open source repository provides all of the source files that were used to build them using the [Adobe Font Development Kit for OpenType](http://www.adobe.com/devnet/opentype/afdko.html) (AFDKO).

## Download the fonts (OTF, TTF, WOFF, EOT)

* [Latest release](../../releases/latest)
* [All releases](../../releases)

## Font installation instructions

* [Mac OS X](http://support.apple.com/kb/HT2509)
* [Windows](https://www.microsoft.com/en-us/Typography/TrueTypeInstall.aspx)
* [Linux/Unix-based systems](https://github.com/adobe-fonts/source-code-pro/issues/17#issuecomment-8967116)
* Bower<br/>
	`bower install git://github.com/adobe-fonts/source-serif-pro.git#release`
* npm 2.x<br/>
	`npm install --fetch-only git://github.com/adobe-fonts/source-serif-pro.git#release`
* npm 3.x<br/>
	`npm install git://github.com/adobe-fonts/source-serif-pro.git#release`

## Building the fonts from source

### Requirements

To build the binary font files from source, you need to have the [Adobe Font Development Kit for OpenType](http://www.adobe.com/devnet/opentype/afdko.html) (AFDKO) installed. The AFDKO tools are widely used for font development today, and are part of most font editor applications.

### Building one font

The key to building OTF or TTF fonts is `makeotf`, which is part of the AFDKO toolset. Information and usage instructions can be found by executing `makeotf -h`.

In this repository, all necessary files are in place for building the OTF and TTF fonts.  
For example, build a binary OTF font for the Regular style like this:

```sh
$ cd Roman/Regular/
$ makeotf -r
```

### Building all fonts

For convenience, a shell script named `build.sh` is provided in the root directory.  
It builds all OTFs and TTFs, and can be executed by typing:

```sh
$ ./build.sh
```

## Getting Involved

Send suggestions for changes to the Source Serif OpenType font project maintainer, [Frank Grießhammer](mailto:opensourcefonts@adobe.com?subject=[GitHub] Source Serif Pro), for consideration.

## Further information

For information about the design and background of Source Serif, please refer to the [official font readme file](http://www.adobe.com/products/type/font-information/source-serif-pro-readme.html).  
For a quick glance at the design of Source Serif, see the [editable web specimen](http://adobe-fonts.github.io/source-serif-pro/).
