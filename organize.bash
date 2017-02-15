# make a directory once a day for storing old files
#!/bin/bash

yr=$(date +%Y)
mo=$(date +%B)
#da=$(date +%d)
da=13

newdir=$yr/$mo/$da
mkdir -p $newdir

# move files from this day to new directory
mv qnodes*$yr_$mo_$da* $newdir/.
