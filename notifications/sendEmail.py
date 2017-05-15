from subprocess import call
import subprocess

st1="asdfasdf"
st2="qwerqwer"
arr=[]
arr.append(st1)
arr.append(st2)

st3=st1+"\n"+st2+"\n"


command_line = 'echo "' + st3 + '" | mail -s "testing subj" chendon@dstonline.com'
process = subprocess.Popen(command_line, shell=True)
