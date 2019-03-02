import os
import time
import msvcrt


def order_66():
    os.system("TASKKILL /F /IM bfv.exe")
    os.system('cls')
    print("BFV.EXE er dead now :'( ")
    time.sleep(4)
    quit()


order_66()

#def kbfunc():
#    q = msvcrt.kbhit()
#    if q:
#        ret = msvcrt.getch()
#    else:
#        ret = False
#    return ret
#
#
#while True:
#    x = kbfunc()
#    if x is not False and x.decode() == 'o':
#        order_66()
#        break
#
#
#
