import argparse
import time
import datetime

def log_task(task: str, time:float, date, start_hour, end_hour) -> list:
    hours, mins = (time//60)//60, (time//60)%60
    date = [str(date.month), str(date.day), str(date.year)]
    hour = [str(start_hour.tm_hour)+':'+str(start_hour.tm_min), str(end_hour.tm_hour)+':'+str(end_hour.tm_min)]
    output = ['Date: '+'/'.join(date),
              'Time Elapsed: '+'-'.join(hour),
              'Total in hrs/mins: '+str(hours)+' hrs, '+str(mins)+' mins',
              'Total in seconds: '+str(time),
              'Work completed: \n'+task]
    
    return output

def log_manual(date_obj) -> list:
    attempting = True
    while attempting:
        try:
            date = [str(date_obj.month), str(date_obj.day), str(date_obj.year)]
            span = str(input('What span of time (e.g. 10:30-12:45) did you work?\n'))

            begin, end = span.split('-')
            time = []
            time += begin.split(':')
            time += end.split(':')
            span_begin = datetime.timedelta(hours=int(time[0]), minutes=int(time[1]))
            span_end = datetime.timedelta(hours=int(time[2]), minutes=int(time[3]))
            attempting = False
        except ValueError:
            print('Invalid time format. Please input a time span in this format: "00:00-00:00".')
    elapsed = span_end - span_begin
    hours, mins = (elapsed.seconds//60)//60, (elapsed.seconds//60)%60
    task = str(input('What did you work on?\n'))
            
    output = ['Date: '+'/'.join(date),
              'Time Elapsed: '+span,
              'Total in hrs/mins: '+str(hours)+' hrs, '+str(mins)+' mins',
              'Total in seconds: '+str(float(elapsed.seconds)),
              'Work completed: \n'+task]
    
    return output

def write_log(new: bool, filename: str, output: list) -> None:
    with open(filename, 'a') as log_file:
        log_file.write('\n'.join(output)+'\n\n')
    
    return None

def main(args):
    if args.new:
        with open(args.file, 'w') as log:
            log.write('')

    in_use = True
    while in_use:
        if args.manual:
            write_log(args.new, args.file, log_manual(datetime.date.today()))
            print('\nTask logged!')
        else:
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
            write_log(args.new, args.file, log_task(task, task_time, datetime.date.today(), hour, end_hour))
            print('\nTask logged!')

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
    arg_parser.add_argument('-n', '--new', action='store_true', help='Using this flag forces the log file to reset. Any subsequent tasks will be logged as the first tasks.')
    # Specify file
    arg_parser.add_argument('-f', '--file', default='./log.txt', help='Using this flag lets you specify a file to output your log to. The default is log.txt.')
    # Manually add to log
    arg_parser.add_argument('-m', '--manual', action='store_true', help='Using this flag allows you to manually add a completed task.')
    main(arg_parser.parse_args())
