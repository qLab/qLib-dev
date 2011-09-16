#!/bin/bash

./otl_delete_built.sh

echo "*** BUILDING OTLS ***"

find . -name "*_OTL" | awk '{ d=$0; sub(/_OTL$/, ".otl", d); print "hotl -C " $0 " " d }' | bash


