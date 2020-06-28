# task-logger
Simple command line app that tracks hours spent working on tasks in a basic, continuous text file.

## System Requirements
- Python 3.7+

## Instructions for Use
```
python3 logger.py [-f, --file filename] [-n, --new] [-m, --manual]
```
- '-f' allows you to specify a file where the logged task should be appended to.
- '-n' allows you to specify that the standard log file should be restarted.
- '-m' allows you to manually add a task completed without having to time yourself. Note: This system does not currently support timespans over 24 hours.


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
