#!/bin/env sh

rom=Roman/Masters

# build variable OTFs
buildMasterOTFs $rom/SourceSerifVariable-Roman.designspace
buildCFF2VF $rom/SourceSerifVariable-Roman.designspace

# extract and subroutinize the CFF2 table
tx -cff2 +S +b -std $rom/SourceSerifVariable-Roman.otf $rom/.tb_cff2

# replace CFF2 table with subroutinized version
sfntedit -a CFF2=$rom/.tb_cff2 $rom/SourceSerifVariable-Roman.otf

# build variable TTFs
fontmake -m $rom/SourceSerifVariable-Roman.designspace -o variable --production-names

# use DSIG, name, OS/2, and STAT tables from OTFs
sfntedit -x DSIG=$rom/.tb_DSIG,name=$rom/.tb_name,OS/2=$rom/.tb_os2,STAT=$rom/.tb_STAT $rom/SourceSerifVariable-Roman.otf
sfntedit -a DSIG=$rom/.tb_DSIG,name=$rom/.tb_name,OS/2=$rom/.tb_os2,STAT=$rom/.tb_STAT $rom/SourceSerifVariable-Roman.ttf

# use cmap, GDEF, GPOS, and GSUB tables from TTFs
sfntedit -x cmap=$rom/.tb_cmap,GDEF=$rom/.tb_GDEF,GPOS=$rom/.tb_GPOS,GSUB=$rom/.tb_GSUB $rom/SourceSerifVariable-Roman.ttf
sfntedit -a cmap=$rom/.tb_cmap,GDEF=$rom/.tb_GDEF,GPOS=$rom/.tb_GPOS,GSUB=$rom/.tb_GSUB $rom/SourceSerifVariable-Roman.otf

# delete build artifacts
rm */Masters/master_*/master.*tf
rm */Masters/.tb_*
