from subprocess import call

st1="asdfasdf"
st2="qwerqwer"
arr=[]
arr.append(st1)
arr.append(st2)

st3=st1+"\n"+st2+"\n"

call(["echo", st3, "|", "mail", "-s", "FCCC Notification", "chendon@dstonline.com"])
