import subprocess
import re
import getpass
import time

time.sleep(10) #Time sleep after start script

process = subprocess.Popen(['lsof', '-i'],
                           stdout=subprocess.PIPE,
                           universal_newlines=True)

#This is array get all active process after load OS
autorun = []
user_name_os = getpass.getuser()

while True:
    output = process.stdout.readline()
    #print(output.strip())
    # Do something else
    return_code = process.poll()
    if return_code is not None:
        print('RETURN CODE', return_code)
        # Process has finished, read rest of the output
        for output in process.stdout.readlines():
            row = re.search('ESTABLISHED', output)
            if row is not None:
                result = re.search('Python', output)
                if result is None:
                    regular_expression = '(?<=\ )\d*?(?=\ ' + user_name_os + ')'
                    number_process = re.search(regular_expression, output)
                    autorun.append(number_process.group(0))
            #print(output.strip())
        break

autorun = list(dict.fromkeys(autorun)) #Delete dublicate from list
print(autorun)