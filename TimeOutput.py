import sys, time, msvcrt

def readInput( caption, default, timeout = 5):

    start_time = time.time()
    input = ''
    while True:
        if msvcrt.kbhit():
            byte_arr = msvcrt.getche()
            if ord(byte_arr) == 13: # enter_key
                break
            elif ord(byte_arr) >= 32: #space_char
                input += "".join(map(chr,byte_arr))
        if len(input) == 0 and (time.time() - start_time) > timeout:
#           print("timing out, using default value.")
            break

    if len(input) > 0:
        return input
    else:
        return default
