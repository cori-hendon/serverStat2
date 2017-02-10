#!/bin/bash

# copy new files from /home/ec2-user/qnodes.out.*
cp -u -p /home/ec2-user/qnodes.out.* /mnt/ftp/httpd/customers/fccc/.




# update github directory
git --git-dir=/mnt/ftp/httpd/customers/fccc/.git --work-tree=/ add *
git --git-dir=/mnt/ftp/httpd/customers/fccc/.git --work-tree=/ commit -am "Adding file"
