#!/usr/bin/env sh

rom=Roman/Masters

ro_name=SourceSerifVariable-Roman

# build variable OTFs
buildMasterOTFs $rom/$ro_name.designspace
buildCFF2VF $rom/$ro_name.designspace

# extract and subroutinize the CFF2 table
tx -cff2 +S +b -std $rom/$ro_name.otf $rom/.tb_cff2

# replace CFF2 table with subroutinized version
sfntedit -a CFF2=$rom/.tb_cff2 $rom/$ro_name.otf

# build variable TTFs
fontmake -m $rom/$ro_name.designspace -o variable --production-names

# use DSIG, name, OS/2, hhea, post, and STAT tables from OTFs
sfntedit -x DSIG=$rom/.tb_DSIG,name=$rom/.tb_name,OS/2=$rom/.tb_os2,hhea=$rom/.tb_hhea,post=$rom/.tb_post,STAT=$rom/.tb_STAT $rom/$ro_name.otf
sfntedit -a DSIG=$rom/.tb_DSIG,name=$rom/.tb_name,OS/2=$rom/.tb_os2,hhea=$rom/.tb_hhea,post=$rom/.tb_post,STAT=$rom/.tb_STAT $rom/$ro_name.ttf

# use cmap, GDEF, GPOS, and GSUB tables from TTFs
sfntedit -x cmap=$rom/.tb_cmap,GDEF=$rom/.tb_GDEF,GPOS=$rom/.tb_GPOS,GSUB=$rom/.tb_GSUB $rom/$ro_name.ttf
sfntedit -a cmap=$rom/.tb_cmap,GDEF=$rom/.tb_GDEF,GPOS=$rom/.tb_GPOS,GSUB=$rom/.tb_GSUB $rom/$ro_name.otf

# delete build artifacts
rm */Masters/.tb_*
rm */Masters/master_*/*.*tf
