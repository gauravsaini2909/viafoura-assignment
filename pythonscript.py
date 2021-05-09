import os
import stat
import sys


user_input = input("Enter the path of your directory: ")
executable = stat.S_IEXEC | stat.S_IXGRP | stat.S_IXOTH
for filename in os.listdir(user_input):
    if os.path.isfile(filename):
        st = os.stat(filename)
        mode = st.st_mode
        if mode & executable:
            print(filename,oct(mode))