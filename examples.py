import etc
import sys
import time

print("Test 1:")
print("Iterate over a range of 10, getting progress at each step")
for i, pi in etc.range(10):
    if pi:
        print("progress at %g"%pi.progress)
        print("%g seconds elapsed"%pi.elapsed_time)
        print("%g seconds remaining"%pi.time_remaining())
        print("")
    time.sleep(0.1)
print("")

print("Test 2:")
test_string = 'some test string to iterate over'
print("Iterate over a string, getting progress every 1 seconds")
for i, pi in etc.sequence_timer(test_string, info_frequency=1):
    sys.stdout.write(i)
    sys.stdout.flush()
    if pi:
        sys.stdout.write('\n')
        print("progress at %g"%pi.progress)
        print("%g seconds elapsed"%pi.elapsed_time)
        print("%g seconds remaining"%pi.time_remaining())
        print("")
    time.sleep(0.1)
print('\n\n')

print("Test 3:")
print("Iterate over a file, getting progress every 1 seconds")
for i, pi in etc.file_timer(open('examples.py', 'r'), info_frequency=1):
    if pi:
        print("progress at %g"%pi.progress)
        print("%g seconds elapsed"%pi.elapsed_time)
        print("%g seconds remaining"%pi.time_remaining())
        print("")
    time.sleep(0.1)
print("") 
