#!/bin/sh

rm -rf *.dir *.contents
ls -1 *.hip | awk '{ print "hexpand -p " $0  }' | bash


