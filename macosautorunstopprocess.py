import subprocess
import re
import getpass
import time

##diagnostic active user start
whoami = subprocess.Popen(["whoami"],
                           stdout=subprocess.PIPE,
                           universal_newlines=True) #diagnostic
get_active_user = whoami.stdout.readline()
##diagnostic get ctive user stop


#time.sleep(1) #Time sleep after start script


process = subprocess.Popen(['lsof', '-i'],
                           stdout=subprocess.PIPE,
                           universal_newlines=True)

#This is array get all active process after load OS
autorun = []
get_all_info_output_console = []
user_name_os = getpass.getuser()

while True:
    output = process.stdout.readline()
    #print(output.strip())
    # Do something else
    return_code = process.poll()
    get_all_info_output_console.append(output)  # Diagnostic get all info from console
    if return_code is not None:
        print('RETURN CODE', return_code)
        # Process has finished, read rest of the output
        for output in process.stdout.readlines():
            row = re.search('ESTABLISHED', output)
            if row is not None:
                result = re.search('Python', output)        #Don't kill Python scripts
                if result is None:
                    result2 = re.search('pycharm', output)  # Don't kill IDE
                    if result2 is None:
                        regular_expression = '(?<=\ )\d*?(?=\ ' + user_name_os + ')'
                        number_process = re.search(regular_expression, output)
                        autorun.append(number_process.group(0))
            #print(output.strip())
        break

autorun = list(dict.fromkeys(autorun)) #Delete dublicate from list

while autorun:
    time.sleep(1)
    process_kill = autorun.pop(-1)
    subprocess.run(["kill", "-9", process_kill]) #Command line kill -9 2321
#print(autorun)
