#!/usr/bin/env python3
import time

def pomodoro(work=25, rest=5):
    print(f'Work {work} min')
    time.sleep(work * 60)
