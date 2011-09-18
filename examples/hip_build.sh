#!/bin/sh

ls -1 cpio.*.contents | awk 'match($0, /[^.]+\.hip/) { print "hcollapse -p -r " substr($0,RSTART,RLENGTH) }' | bash

