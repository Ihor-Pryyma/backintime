"""
This file contains constants that are used in the test files.
"""
import grp
import os
import pwd

CURRENTUID = os.geteuid()
CURRENTUSER = pwd.getpwuid(CURRENTUID).pw_name
CURRENTGID = os.getegid()
CURRENTGROUP = grp.getgrgid(CURRENTGID).gr_name
CURRENTUID = os.geteuid()
CURRENTGID = os.getegid()
