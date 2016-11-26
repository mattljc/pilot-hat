'''
Code fragment to test out the data logging and pause process.
'''

import time
from datetime import datetime
import random
import numpy as np
import math

sample_freq = 100.0; #Hz
sample_rate = 1/sample_freq; #sec

fido = open('test_log', 'w',0) #note that this is unbuffered, instantly writes to file.

header_string ='<TimeStamp>,<ad0%>,<ad1%>,<ad2%>,<ad3%>,<TimeDelta>\n'
template_string = '{:s},{:10.5g},{:10.5g},{:10.5g},{:10.5g},{:.3e};\n'

fido.write(header_string)
old_time = datetime.utcnow()

cycle_times = list
for ct in range(start=0, end=10000000, step=1)
#while True:
    time_stamp = datetime.utcnow()
    time_delta = time_stamp - old_time
    time_delta = (time_delta.seconds + time_delta.microseconds/1e6) - sample_rate
    ad0 = random.random()
    ad1 = random.random()
    ad2 = random.random()
    ad3 = random.random()
    data_string = template_string.format(time_stamp.isoformat(),ad0,ad1,ad2,ad3,time_delta)
    fido.write(data_string)
    time.sleep(sample_rate)
    old_time = time_stamp

min_cycle = min(cycle_times)
max_cycle = max(cycle_times)
avg_cycle =
