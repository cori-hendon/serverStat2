

# send email if newAlert.txt is not the same as lastAlert.txt

DIFF=$(diff lastAlert.txt newAlert.txt)
if [ "$DIFF" != "" ]
then
	echo | mail -s "script subj" -q /mnt/ftp/httpd/customers/fccc/notifications/newAlert.txt chendon@dstonline.com
fi
