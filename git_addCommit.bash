#!/bin/bash
# this should run once every 10 mins 


# move old stuff to directories for storage
yr=$(date +%Y)
mo=$(date +%B)
da=$(date +%d)
pathvar=$yr/$mo/$da
filenamevar=qnodes.out.${yr}_${mo}_${da}

mkdir -p /home/ec2-user/$pathvar
mv /home/ec2-user/$filenamevar* /home/ec2-user/$pathvar/.



# copy new files from /home/ec2-user/qnodes.out.*
#cp -u -p /home/ec2-user/qnodes.out.* /mnt/ftp/httpd/customers/fccc/




# make a copy of the newest file for easy reference naming
newfile=$(ls -ltr /home/ec2-user/$pathvar | tail -1 | awk '{print $9}')
rm -f /mnt/ftp/httpd/customers/fccc/serverStat/newest.data
cp /home/ec2-user/$pathvar/$newfile /mnt/ftp/httpd/customers/fccc/serverStat/newest.data

# parse the newest file
rm /mnt/ftp/httpd/customers/fccc/serverStat/newest_parsed.data
python /mnt/ftp/httpd/customers/fccc/serverStat/parseQnodes_FCCC-EDIT.py /mnt/ftp/httpd/customers/fccc/serverStat/newest.data > /mnt/ftp/httpd/customers/fccc/serverStat/newest_parsed.data



# update github directory
#git --git-dir=/mnt/ftp/httpd/customers/fccc/.git --work-tree=/ add -A
#git --git-dir=/mnt/ftp/httpd/customers/fccc/.git --work-tree=/ commit -am "Adding file"

cd /mnt/ftp/httpd/customers/fccc/serverStat/
git add -A &> /dev/null
git commit -am "automated file upload" &> /dev/null
git push origin master &> /dev/null

# redirecting output to /dev/null to clean up mailbox clutter
