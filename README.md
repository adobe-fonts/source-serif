# Source Serif

Source Serif is a set of OpenType fonts to complement the [Source Sans](https://github.com/adobe-fonts/source-sans-pro) family.
In addition to the fonts, this open-source repository provides all of the source files that were used to build them using the [Adobe Font Development Kit for OpenType](https://github.com/adobe-type-tools/afdko/) (AFDKO).


## Download the fonts (OTF, TTF, WOFF, WOFF2, variable)

* [Latest release](../../releases/latest)
* [All releases](../../releases)


## Font installation instructions

* [macOS](https://support.apple.com/en-us/HT201749)
* [Windows](https://www.microsoft.com/en-us/Typography/TrueTypeInstall.aspx)
* [Linux/Unix-based systems](https://github.com/adobe-fonts/source-code-pro/issues/17#issuecomment-8967116)
* Bower<br/>
	`bower install git://github.com/adobe-fonts/source-serif.git#release`
* npm 2.x<br/>
	`npm install --fetch-only git://github.com/adobe-fonts/source-serif.git#release`
* npm 3.x<br/>
	`npm install git://github.com/adobe-fonts/source-serif.git#release`


## Building the fonts from source

### Requirements

To build the binary font files from source, you need to have the [Adobe Font Development Kit for OpenType](https://github.com/adobe-type-tools/afdko/) (AFDKO) installed. The AFDKO tools are widely used for font development today, and are part of most font editor applications.

### Building one font

The key to building OTF fonts is `makeotf`, which is part of the AFDKO toolset. Information and usage instructions can be found by executing `makeotf -h`.

In this repository, all necessary files are in place for building the OTF and TTF fonts. For example, build a binary OTF font for the Regular style like this:

```sh
$ cd /Roman/Instances/Text/Regular
$ makeotf -r
```

### Building all fonts

For convenience, a shell script named `build.sh` is provided in the root directory. It builds all OTFs and TTFs, and can be executed by typing:

```sh
$ ./build.sh
```


## Getting Involved

Please file an issue to start the discussion.


## Further information

[Blog post on the introductory release of Source Serif](https://blog.typekit.com/2014/05/20/source-serif-pro/) (2014)  

[Blog post on the six-weight extension](https://blog.typekit.com/2014/12/11/source-serif-update-three-new-weights/) (2014)  

[Source Serif 2.0](https://blog.typekit.com/2017/01/10/introducing-source-serif-2-0/) (2017)  

[Source Serif Italics](https://blog.typekit.com/2018/08/16/source-serif-italics/) (2018)  

For information about the design and background of Source Serif, please refer to the [official font readme file](http://www.adobe.com/products/type/font-information/source-serif-readme.html).  

For a glance at the design of Source Serif, see the [editable web specimen](http://adobe-fonts.github.io/source-serif/).
