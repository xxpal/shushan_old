import datetime
import time
import random


odds = [ 1,  3,  5,  7,  9, 11, 13, 15, 17, 19,
        21, 23, 25, 27, 29, 31, 33, 35, 37, 39,
        41, 43, 45, 47, 49, 51, 53, 55, 57, 59 ]

right_this_minute = datetime.datetime.today().minute

# iterate 5 times and ensure each iteration paused random seconds
for i in range(5):
    if right_this_minute in odds:
        print("This minute seems a little odd.")
    else:
        print("Not an odd minute.")
    sleep_interval = random.randint(1, 60)
    time.sleep(sleep_interval)
    print('Paused', sleep_interval, 'seconds.')
    print('Iteration', i, 'completed.')
