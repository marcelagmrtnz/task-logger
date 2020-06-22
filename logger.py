import argparse
import time
import datetime

def log_task(new: bool, filename: str, task: str, time:float, date, start_hour, end_hour) -> None:
    hours, mins = (time//60)//60, (time//60)%60
    date = [str(date.month), str(date.day), str(date.year)]
    hour = [str(start_hour.tm_hour)+':'+str(start_hour.tm_min), str(end_hour.tm_hour)+':'+str(end_hour.tm_min)]
    output = ['Date: '+'/'.join(date),
              'Time Elapsed: '+'-'.join(hour),
              'Total in hrs/mins: '+str(hours)+' hrs, '+str(mins)+' mins',
              'Total in seconds: '+str(time),
              'Work completed: \n'+task]
    
    if new:
        with open(filename, 'w') as log_file:
            log_file.write('\n'.join(output)+'\n\n')
    else:
        with open(filename, 'a') as log_file:
            log_file.write('\n'.join(output)+'\n\n')
    
    return None

def main(args):
    '''
    if args.manual:
        log_task(args.new, args.file, args.manual[1], task_time, datetime.date.today(), hour, end_hour)
        print('\nTask logged!')
    else:
        in_use = True
    '''

    in_use = True
    while in_use:
        # Start timer
        hour = time.localtime()
        start = time.time()
        
        # Wait for user to end timer
        end_timer = str(input('Press enter to stop the timer...\n'))
        end_hour = time.localtime()
        task_time = time.time()-start

        # Collect task data
        task = str(input('What did you work on?\n'))

        # Write to file
        log_task(args.new, args.file, task, task_time, datetime.date.today(), hour, end_hour)
        print('\nTask logged!')
        if args.new:
            question = False
            in_use = False
        else:
            question = True

        while question:
            run_again = input('\nTime another task?\n').lower()
            if run_again in ['yes', 'y']:
                question = False
            elif run_again in ['no', 'n']:
                in_use = False
                question = False
            else:
                print('\nInvalid input. Try again. Either yes (y) or no (n).')


if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser(description='Log hours spent on tasks.')
    # New file
    arg_parser.add_argument('-n', '--new', action='store_true')
    # Specify file
    arg_parser.add_argument('-f', '--file', default='./log.txt')
    # Manually add to log
    #arg_parser.add_argument('-m', '--manual', nargs=2)
    main(arg_parser.parse_args())
