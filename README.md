# task-logger
Simple command line app that tracks hours spent working on tasks in a basic, continous text file.

## System Requirements
- Python 3.7+

## Instructions for Use
```
python3 logger.py [-f, --file] [-n, --new]
```
- '-f' allows you to specify a file where the logged task should be appended to.
- '-n' allows you to specify that the standard log file should be restarted.


## System Output
The system will append task updates to a file (unless otherwise specified) called log.txt. These updates have the following format.<br>
```
Date: DD/MM/YY
Time Elapsed: 00:00-00:00
Total in hrs/mins: 0hrs, 0mins
Total in seconds: 0.0
Work completed:
Task description...
```
