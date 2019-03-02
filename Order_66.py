import os
import time


def order_66():
    os.system("TASKKILL /F /IM bfv.exe")
    os.system('cls')
    print("BFV.EXE er dead now :'( ")
    time.sleep(4)
    quit()


order_66()
