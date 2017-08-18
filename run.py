import psutil
import subprocess
import sys
import os
import time
import random
cpu_p = psutil.cpu_percent(interval=None, percpu=True)
cpu_usage = sum(cpu_p) / len(cpu_p)
mem_usage = '{:.2f} MiB'.format(__import__('psutil').Process().memory_full_info().uss / 1024 ** 2)
IS_WINDOWS = os.name == "nt"
IS_MAC = sys.platform == "darwin"

def clear_screen():
    if IS_WINDOWS:
        os.system("cls")
    else:
        os.system("clear")
        
def sysinfo():
    updates = 0
    times = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
    t1 = time.perf_counter()
    time.sleep(random.choice(times))
    t2 = time.perf_counter()
    start_time = time.time()
    updates += 1
    clear_screen()
    print("===============\n"
          "   Sysinfo\n"
          "===============\n\n")
    print("System Info:\n")
    print("Name:")
    subprocess.call(("uname", "-a"))
    if IS_WINDOWS:
        print("\nOperating System\n"
              "\nWINDOWS\n")
    if IS_MAC:
        print("\nOperating System\n"
              "\nMAC\n")
    else:
        print("\nOperating System:\n"
              "Linux\n")
    print("\nProcessor:")
    subprocess.call(("uname", "-m"))
    print("\nSystem Version:")
    subprocess.call(("uname", "-r"))
    print("\nPing:")
    print("{}ms".format(str(round((t2-t1)*1000))))
    print("\nCpu Usage:\n"
          "{}%\n".format(cpu_usage))
    print("Memory Usage:\n"
          "{}".format(mem_usage))
    print("\n"
          "Been Running For\n"
          "{}ms\n".format(time.time() - start_time))
    sysinfo()
    

sysinfo()
