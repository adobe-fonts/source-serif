# Source Serif

[Source Serif](https://adobe-fonts.github.io/source-serif/) is an open-source typeface to complement the [Source Sans](https://github.com/adobe-fonts/source-sans-pro) family.


## Getting Involved

Please [open an issue](https://github.com/adobe-fonts/source-serif/issues) to start the discussion.

## Releases

* [Latest release](../../releases/latest)
* [All releases](../../releases)


## Building the fonts from source

### Requirements

To build the binary font files from source, you need to have the [Adobe Font Development Kit for OpenType](https://github.com/adobe-type-tools/afdko/) (AFDKO) installed.

### Building one font

The key to building OTF fonts is `makeotf`, which is part of the AFDKO toolkit. Information and usage instructions can be found by executing `makeotf -h`. TTFs are generated with the `otf2ttf` and `ttfcomponentizer` tools.

Commands to build the Regular style OTF font:

```sh
$ cd /Roman/Instances/Text/Regular
$ makeotf -r
```

Commands to generate the Regular style TTF font:

```sh
$ otf2ttf SourceSerifPro-Regular.otf
$ ttfcomponentizer SourceSerifPro-Regular.ttf
```

### Building all static fonts

For convenience, a shell script named **build.sh** is provided in the root directory. It builds all OTFs and TTFs, and can be executed by typing:

```sh
$ ./build.sh
```

### Building variable fonts

To build the variable TTFs you must install **fontmake**:

```sh
$ pip install fontmake
```

A shell script named **buildVFs.sh** is provided in the root directory.
It generates four variable fonts (two CFF2-OTFs and two TTFs), and can be executed by typing:

```sh
$ ./buildVF.sh
```


