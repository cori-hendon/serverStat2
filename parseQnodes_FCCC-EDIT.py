import sys

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

sendNotification=False
notificationText=[]

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
                        # job-exclusive
                        # job-sharing
                        # offline 	*
                        # reserve
                        # state-unknown *
                        # time-shared
                        # up
			if state == "down" or state == "offline" or state == "state-unknown":
				sendNotification==True
				notificationText.append(mystr)
	
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


#if sendNotification:
	
