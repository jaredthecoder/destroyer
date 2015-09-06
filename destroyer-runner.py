#!/usr/bin/python
"""destroyer-runner.py - Run the main application"""


import sys
import subprocess


if __name__ == '__main__':
    subprocess.call(['python', './destroyer/destroyer.py'] + [str(arg) for arg in sys.argv[1:]])

