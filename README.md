# Source Serif Pro

[Source Serif Pro](http://adobe-fonts.github.io/source-serif-pro/)
is a set of OpenType fonts to complement the
[Source Sans Pro](https://github.com/adobe-fonts/source-sans-pro) family.

## Getting involved

[Open an issue](https://github.com/adobe-fonts/source-serif-pro/issues) or send a suggestion to Source Serif's designer [Frank Grießhammer](mailto:opensourcefonts@adobe.com?subject=[GitHub]%20Source%20Serif%20Pro), for consideration.

## Releases

* [Latest release](../../releases/latest)
* [All releases](../../releases)

## Building the fonts from source

### Requirements

To build the binary font files from source, you need to have installed the
[Adobe Font Development Kit for OpenType](https://github.com/adobe-type-tools/afdko/) (AFDKO).

### Building one font

The key to building the OTF fonts is `makeotf`, which is part of the AFDKO toolset.
Information and usage instructions can be found by executing `makeotf -h`. The TTFs
are generated with the `otf2ttf` and `ttfcomponentizer` tools.

Commands to build the Regular style OTF font:

```sh
$ cd Roman/Instances/Regular/
$ makeotf -r -gs -omitMacNames
```

Commands to generate the Regular style TTF font:

```sh
$ otf2ttf SourceSerifPro-Regular.otf
$ ttfcomponentizer SourceSerifPro-Regular.ttf
```

### Building all non-variable fonts

For convenience, a shell script named **build.sh** is provided in the root directory.
It builds all OTFs and TTFs, and can be executed by typing:

```sh
$ ./build.sh
```

### Building the variable fonts

To build the variable TTFs you must install **fontmake** using this command:

```sh
$ pip install fontmake
```

A shell script named **buildVFs.sh** is provided in the root directory.
It generates four variable fonts (two CFF2-OTFs and two TTFs), and can be executed by typing:

```sh
$ ./buildVFs.sh
```
