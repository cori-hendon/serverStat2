#!/bin/bash

# move old stuff to directories for storage
yr=$(date +%Y)
mo=$(date +%B)
da=$(date +%d)
pathvar=$yr/$mo/$da/
echo $pathvar

mv qnodes.* $pathvar.

