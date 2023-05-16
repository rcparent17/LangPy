import sys

def realtime_print(obj):
    sys.stdout.write(str(obj))
    sys.stdout.flush()

def realtime_println(obj):
    realtime_print(str(obj) + "\n")
