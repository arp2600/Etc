import time
import math

class ProgressInfo:
    def __init__(self, elapsed_time, progress):
        self.elapsed_time = elapsed_time
        self.progress = progress

    def time_remaining(self):
        if (self.progress > 0):
            return self.elapsed_time * (1/self.progress) - self.elapsed_time
        return 0


def range(n, info_frequency=0):
    i = 0
    start = time.time()
    if_counter = start
    while i < n:
        now = time.time()
        if now - if_counter > info_frequency:
            pi = ProgressInfo(now - start, float(i)/n)
            if_counter += info_frequency
        else:
            pi = None
        yield i, pi
        i += 1

def sequence_timer(sequence, info_frequency=0):
    i = 0
    start = time.time()
    if_counter = start
    length = len(sequence)
    for elem in sequence:
        now = time.time()
        if now - if_counter < info_frequency:
            yield elem, None
        else:
            pi = ProgressInfo(now - start, float(i)/length)
            if_counter += info_frequency
            yield elem, pi
        i += 1

def file_timer(in_file, info_frequency=0):
    i = 0
    start = time.time()
    if_counter = start
    in_file.seek(0, 2)
    length = in_file.tell()
    in_file.seek(0)

    while True:
        line = in_file.readline()
        if line == "":
            break

        now = time.time()
        if now - if_counter < info_frequency:
            yield line, None
        else:
            pi = ProgressInfo(now - start, float(in_file.tell())/length)
            if_counter += info_frequency
            yield line, pi
        i += 1

def format_seconds(seconds):
    out_string = ''
    comma = False
    if seconds > 60*60:
        hours = math.floor(seconds / (60*60))
        seconds -= hours*60*60
        out_string += '%g hours'%hours
    if seconds > 60:
        minutes = math.floor(seconds / 60)
        seconds -= minutes*60
        if out_string:
            out_string += ', '
        out_string += '%g minutes'%minutes
    if round(seconds) > 1:
        if out_string:
            out_string += ', '
        out_string += '%g seconds'%round(seconds)
    return out_string
