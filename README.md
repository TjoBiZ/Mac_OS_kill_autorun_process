# Python scirpt - "Mac OS autorun stop processes"

This script do "kill -9 {process}" from console command after start OS and use linux command "lsof -i | grep -E ESTABLISHED". When processes will have search, script would kill with parameters - "ESTABLISHED".

## Installation

You should add this script to "crontab -e". Add this row to you crontabe file

```bash
@reboot                 cd /Users/UserName/Downloads/consolemacos/ && python macosautorunstopprocess.py >> ~/Downloads/consolemacos/cron.txt 2>&1
```

You should change in macosautorunstopprocess.py
- Password your Mac OS user
```python
spw = 'User_Password_Mac_OS'
```
- You need write full path to log file - kill-processes.log"
```python
open_notes_with_log = "open /Applications/TextEdit.app /Users/joker/Downloads/websites/python/consolemacos/kill-processes.log"
```

After reboot or load Mac OS you must wait open log file then after close this and terminal process you can work on your PC

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)