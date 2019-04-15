#!/usr/bin/python3
#coding: utf-8
#
# A simple indicator applet displaying cpu and memory information
#
# Author: Alex Eftimie <alex@eftimie.ro>
# Fork Author: fossfreedom <foss.freedom@gmail.com>
# Original Homepage: http://launchpad.net/indicator-sysmonitor
# Fork Homepage: https://github.com/fossfreedom/indicator-sysmonitor
# License: GPL v3
# modified by luo shijie
import json
import time
import subprocess
import copy
import logging
import re
import os
import platform
import psutil as ps
from threading import Thread
from gettext import gettext as _
import matplotlib as mpl

class CPUsensor():
    def __init__(self):
        cpu = ps.Process(os.getpid())
        self.cpu_number = ps.cpu_count()

    def cpu_freqency(self):
        sum = 0.0
        file = open("/proc/cpuinfo")
        for i in range(35*self.cpu_number):
            lines = file.readline()
            if "MHz" in lines:
                print(lines)
                sum += float(lines[-9:])
        file.close()
        freqency = sum/self.cpu_number
        return freqency


