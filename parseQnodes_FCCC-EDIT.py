import sys
import subprocess
import smtplib
from email.mime.text import MIMEText

# file name given as command line argument
filename = sys.argv[1]

# open given file
myfile = open(filename,"r")


# read line by line and store info in string to print
mystr=""
group=""
name=""
state=""
power_state=""
np=""
prop=""
ntype=""
dummy=""

problemState=False
sendNotification=False
notificationText=""

debugFile = open("/mnt/ftp/httpd/customers/fccc/notifications/debug.txt","w")

for line in myfile:
	if line != "\n":
		linedata=line.split()
		if len(linedata) == 1:
			# this is a new node
			mystr=ntype + "," + name + "," + state + "," + power_state + "," + np# + "," + prop
			if mystr != ",,,,":
				print mystr
			name=linedata[0]
			# -------------------------------------
			# notification processing of bad states
			# -------------------------------------
			# send notification email if state is *
                        # active
                        # busy
                        # down 		*
                        # free
                        # job-exclusive ****
                        # job-sharing
                        # offline 	*
                        # reserve
                        # state-unknown *
                        # time-shared
                        # up
			if state == "down" or state == "offline" or state == "state-unknown" or state == "job-exclusive":
				problemState=True
				notificationText += mystr + "\n"
				#debugFile.write(notificationText)
	
		elif linedata[0] == "state":
			state=linedata[2]
		elif linedata[0] == "power_state":
			power_state=linedata[2]
		elif linedata[0] == "np":
			np=linedata[2]
		elif linedata[0] == "properties":
			#prop=linedata[2]
			# the qnodes property for FCCC cluster gives high mem vs reg mem info
			# use this to categorize cluster nodes into two sections
			if linedata[2]=="64GB":
				ntype="Standard Mem: " + linedata[2]
			elif linedata[2]=="128GB":
				ntype="High Mem: " + linedata[2]
			else:
				ntype=linedata[2]
		#elif linedata[0] == "ntype":
		#	ntype=linedata[2]
		else:
			# dont include this data for now...
			dummy="a"


if problemState:
	# create the new notification email txt file
	notifyMsg = open("/mnt/ftp/httpd/customers/fccc/notifications/newAlert.txt","w")
	notifyMsg.write("This is an automated notification from Data in Science Technologies.\nThe following FCCC nodes have trouble states:\n\n")
	notifyMsg.write("Type,	name,	state,	power_state,	numProc\n")
	notifyMsg.write("----------------------------------------------\n")
	notifyMsg.write(notificationText)
	notifyMsg.close()

	# test if the new email txt contains different data from the lastAlert.txt
	last=open("/mnt/ftp/httpd/customers/fccc/notifications/lastAlert.txt","r")
	curr=open("/mnt/ftp/httpd/customers/fccc/notifications/newAlert.txt","r")
	last_txt=last.read()
	curr_txt=curr.read()
	if last_txt != curr_txt:
		# this is a change in state
		sendNotification=True

	# send the new file as an email message
	if sendNotification:
		fp = open('newAlert.txt','rb')
		msg = MIMEText(fp.read())
		fp.close()

		msg['Subject'] = 'FCCC-AutoNotify'
		msg['From'] = ''
		mailTo = 'chendon@dstonline.com'
		s = smtplib.SMTP('localhost')
		s.sendmail('',mailTo,msg.as_string())
		s.quit()

		debugFile.write("got to end of conditionals...")


debugFile.close()
