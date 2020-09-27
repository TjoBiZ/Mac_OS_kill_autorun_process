import subprocess
import re
import getpass
import time
from datetime import datetime

##diagnostic active user start
whoami = subprocess.Popen(["whoami"],
                           stdout=subprocess.PIPE,
                           universal_newlines=True) #diagnostic
get_active_user = whoami.stdout.readline()
##diagnostic get active user stop

#Open log file and write
# Program to show various ways to read and
# write data in a file.
file_log = open("kill-processes.log", "w")

#L = ["This is Delhi \n", "This is Paris \n", "This is London \n"] #examle write list to file
#file_log.writelines(L)


i = 0
while i <= 15:
    i += 1
    # datetime object containing current date and time
    now = datetime.now()
    # dd/mm/YY H:M:S
    today_time = now.strftime("%d/%m/%Y %H:%M:%S")

    # \n is placed to indicate EOL (End of Line)
    divider_line = "\n\n\n============================ " + today_time + "\n"
    if i == 1:
        divider_line = "============================ " + today_time + "\n"
    file_log.write(divider_line)

    time.sleep(4) #Time sleep after start script
    if i == 15:
        time.sleep(60)

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
                get_all_info_output_console.append(output)
                row = re.search('ESTABLISHED', output)
                if row is not None:
                    result = re.search('Python', output)        #Don't kill Python scripts
                    if result is None:
                        result2 = re.search('pycharm', output)  # Don't kill IDE
                        if result2 is None:
                            regular_expression = '(?<=\ )\d*?(?=\ ' + user_name_os + ')'
                            number_process = re.search(regular_expression, output)
                            autorun.append(number_process.group(0) + '\n')
                #print(output.strip())
            break

    autorun = list(dict.fromkeys(autorun)) #Delete dublicate from list

    #L = ["This is Delhi \n", "This is Paris \n", "This is London \n"] #examle write list to file
    file_log.write("Username: " + get_active_user + "\nProcesses killed:\n")
    file_log.writelines(autorun)
    file_log.write("\nTerminal console show result the command - 'lsof -i | grep -E ESTABLISHED':\n")
    file_log.writelines(get_all_info_output_console)

    while autorun:
        #time.sleep(1)
        process_kill = autorun.pop(-1)

        spw = 'User_Password_Mac_OS'
        bashp = subprocess.Popen(['echo', spw], stdout=subprocess.PIPE)

        command = 'kill -9 ' + process_kill
        command = command.split()
        bash1 = subprocess.Popen(['sudo', '-S'] + command, stdin=bashp.stdout, stdout=subprocess.PIPE)

        #subprocess.run(["kill", "-9", process_kill]) #Command line kill -9 2321
    #print(autorun)



file_log.close()  # to change file access modes
open_notes_with_log = "open /Applications/TextEdit.app /Users/joker/Downloads/websites/python/consolemacos/kill-processes.log"
open_notes_with_log = open_notes_with_log.split()
spw = 'User_Password_Mac_OS'
bashp = subprocess.Popen(['echo', spw], stdout=subprocess.PIPE)
bash = subprocess.Popen(['sudo', '-S'] + open_notes_with_log, stdin=bashp.stdout, stdout=subprocess.PIPE)
