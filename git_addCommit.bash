#!/bin/bash
# this should run once ever 10 mins 


# move old stuff to directories for storage
yr=$(date +%Y)
mo=$(date +%B)
da=$(date +%d)
pathvar=$yr/$mo/$da/
mkdir -p $pathvar
mv qnodes.* $pathvar/.



# copy new files from /home/ec2-user/qnodes.out.*
cp -u -p /home/ec2-user/qnodes.out.* /mnt/ftp/httpd/customers/fccc/.



# make a copy of the newest file for easy reference naming
newest=$(ls -la | tail -1 | awk '{print $9}')
rm -f newest.data
cp $newest newest.data



# update github directory
#git --git-dir=/mnt/ftp/httpd/customers/fccc/.git --work-tree=/ add -A
#git --git-dir=/mnt/ftp/httpd/customers/fccc/.git --work-tree=/ commit -am "Adding file"

git add -A
git commit -am "automated file upload"
git push origin master
