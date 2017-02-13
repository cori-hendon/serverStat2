#!/bin/bash

# copy new files from /home/ec2-user/qnodes.out.*
cp -u -p /home/ec2-user/qnodes.out.* /mnt/ftp/httpd/customers/fccc/.




# update github directory
#git --git-dir=/mnt/ftp/httpd/customers/fccc/.git --work-tree=/ add -A
#git --git-dir=/mnt/ftp/httpd/customers/fccc/.git --work-tree=/ commit -am "Adding file"

git add -A
git commit -am "automated file upload"
git push origin master
