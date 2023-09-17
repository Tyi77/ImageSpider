import threading
import time

def func(x):
    print("start")
    print(x+1)
    time.sleep(5)
    print("sleep done")

a = 1
t = threading.Thread(target=func, args=(a,))
t.start()
print("end")

# print("start")
# print("end")