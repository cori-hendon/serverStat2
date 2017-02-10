#!/bin/bash

# copy new files from /home/ec2-user/qnodes.out.*
curdate=$(date +%Y_%B_%d_%H:)
cp -u -p /home/ec2-user/qnodes.out.$curdate* .




# update github directory
newfile=$(date +%Y_%B_%d_%H:%M:%S)
git add *
git commit -am "Adding file $newfile"
