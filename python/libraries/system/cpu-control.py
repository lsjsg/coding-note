#!/usr/bin/env python
import os
class CPU:
    def __init__(self):
        file = open("/sys/devices/system/cpu/intel_pstate/max_perf_pct","r")
        now = file.read(10)
        self.now = now
        print("Your CPU originally runs at:%",self.now)
        file.close()
        self.mode = 99

    def set_power(self):
        command = "echo " + "\'" + str(self.mode) + "\'" + "| sudo tee /sys/devices/system/cpu/intel_pstate/max_perf_pct"
        os.system(command)
        print("Now your CPU runs at:%",self.mode)

    def run(self):
        self.mode = input("Please enter the power of the CPU:")
        try:
            self.mode = int(self.mode)
        except:
            print("Not a integer, please enter an integer!")
            self.run() 
        if isinstance(self.mode,int):
            if self.mode < 50:
                print("Please don't set too low !")
                self.run()
            elif self.mode >= 100:
                print("Please don't set too high !")
                self.run()
            else:
                self.set_power()
        else:
            print("Not a integer, please enter an integer!")
            self.run()

if __name__ == "__main__":
    my_cpu = CPU()
    my_cpu.run()
    os.system("watch -n 0 \"cat /proc/cpuinfo | grep -i mhz\"")
