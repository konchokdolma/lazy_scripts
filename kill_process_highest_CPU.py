import os

# stores the top output
process = os.popen('top -b -n1')
b = process.readlines()

# starting point where the list of processes start
check = b[0]
i = 0

# running untill the list of processes
while '%CPU' not in b[i]:
        i += 1

# getting PID from the next line
ID =  b[i+1].split(' ')[0]

os.system('kill -9 ' + ID)