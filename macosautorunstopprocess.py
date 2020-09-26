import subprocess
import re

process = subprocess.Popen(['lsof', '-i'],
                           stdout=subprocess.PIPE,
                           universal_newlines=True)

#This is array get all active process after load OS
autorun = []

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
                autorun.append(row.string)
            #print(output.strip())
        break

print(autorun)