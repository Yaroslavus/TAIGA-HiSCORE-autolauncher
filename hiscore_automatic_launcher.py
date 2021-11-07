#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 00:52:49 2021

@author: yaroslav
"""
import os
import time
import sys
#import datetime
#import pytz

#timezone_utc = pytz.timezone('UTC')
#day_utc, month_utc, year_utc = datetime.datetime.now(timezone_utc).strftime("%d:%m:%y").split(":")

def simple_window_opening():

    for ip_name in ('115', '116', '119'):
        os.system("ssh hiscore@192.168.1." + ip_name)
        for window_number in range(3):
            os.system("x-terminal-emulator -e /bin/bash")
            os.system("cd /home/hiscore/krs/NEW_PROGRAMS/hiscore_2018; mc")
            
    os.system("ssh hiscore@192.168.1.119")
    for window_number in range(3):
        os.system("x-terminal-emulator -e /bin/bash")
        os.system("cd /home/hiscore/krs/NEW_PROGRAMS/HiSCORE_4; mc")
        

def open_with_launch():
    
    for ip_name in ('115', '116', '119'):
        os.system("ssh hiscore@192.168.1." + ip_name)
        os.system("x-terminal-emulator -e /bin/bash")
        os.system("cd /home/hiscore/krs/NEW_PROGRAMS/hiscore_2018")
#        with open ("00_target.lst", "w+") as target_list:
#            target_list.write("{} {} {} 0 0".format(day_utc, month_utc, year_utc))
        os.system("prog40.exe")
        time.sleep(120)
        
        for program_name in ('coins4.exe', 'count_rate.exe'):
            os.system("x-terminal-emulator -e /bin/bash")
            os.system("cd /home/hiscore/krs/NEW_PROGRAMS/hiscore_2018")
            os.system(program_name)
            
    os.system("ssh hiscore@192.168.1.119")
    os.system("x-terminal-emulator -e /bin/bash")
    os.system("cd /home/hiscore/krs/NEW_PROGRAMS/hiscore_2018")
#    with open ("00_target.lst", "w+") as target_list:
#        target_list.write("{} {} {} 0 0".format(day_utc, month_utc, year_utc))
    os.system("prog40.exe")
    time.sleep(120)

    for program_name in ('coins4.exe', 'count_rate.exe'):
        os.system("x-terminal-emulator -e /bin/bash")
        os.system("cd /home/hiscore/krs/NEW_PROGRAMS/hiscore_2018")
        os.system(program_name)
        
def set_stop_time(hour, minute, second):
    
    for ip_name in ('115', '116', '119'):
        os.system("ssh hiscore@192.168.1." + ip_name)
        os.system("cd /home/hiscore/krs/NEW_PROGRAMS/hiscore_2018")
        with open ("STOPRUN.CNF", "w+") as stop_time_file:
            stop_time_file.write("{}:{}:{}".format(hour, minute, second))
    os.system("ssh hiscore@192.168.1.119")
    os.system("cd /home/hiscore/krs/NEW_PROGRAMS/HiSCORE_4")
    with open ("STOPRUN.CNF", "w+") as stop_time_file:
        stop_time_file.write("{}:{}:{}".format(hour, minute, second))

open_mode = sys.argv[1]
if len(sys.argv) == 3:
    try:
        hour, minute, second = sys.argv[2].split(":")
        set_stop_time(hour, minute, second)
    except Exception:
        print("Time string decoding error!")
        sys.exit()

if open_mode == "0":
    simple_window_opening
elif open_mode == "1":
    open_with_launch
else:
    print("Wrong opening flag! Use 1 or 0!")
    sys.exit()
