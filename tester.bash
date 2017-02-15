# move old stuff to directories for storage
yr=$(date +%Y)
mo=$(date +%B)
da=$(date +%d)
pathvar=$yr/$mo/$da
filenamevar=qnodes.out.${yr}_${mo}_${da}

echo $filenamevar
echo $pathvar

#WORKS mkdir -p /mnt/ftp/httpd/customers/fccc/$pathvar
#WORKS mv /home/ec2-user/$filenamevar* /home/ec2-user/$pathvar/.

newfile=$(ls -ltr /home/ec2-user/$pathvar | tail -1 | awk '{print $9}')
cp /home/ec2-user/$pathvar/$newfile /mnt/ftp/httpd/customers/fccc/newest.data
