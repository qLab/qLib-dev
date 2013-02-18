#!/bin/sh
#
#		@file		backup.sh
#		@author		xy
#		@since		2011-03-29
#
#		@brief		Create a quick backup of the whole shebang.
#

ROOT_DIR_NAME=qLib-dev

BASE_DIR=..
ARCHIVE_NAME=qLib-dev_`date +%Y-%m-%d_%H%M_%S`_`hostname`.tar.bz2

OLD_DIR=`pwd`
cd $BASE_DIR

echo in dir `pwd`, archiving to file $ARCHIVE_NAME

tar cjvf $ARCHIVE_NAME $ROOT_DIR_NAME --exclude='examples/images/*'

cd $OLD_DIR
unset OLD_DIR

