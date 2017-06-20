#!/usr/bin/env python3
#
# This script will remove MS Office 2011
# By: Myles Rayfield

import sys
import os

applications = '/Applications'
ms_office = '/Applications/Microsoft\Office'
ms_link = 'Applications/Microsoft Link.app'
count = 0

for app in os.listdir(applications):
    if count < 1:
        #os.remove('Microsoft Office 2011')
        os.system("rm -rf Chromecast.app")
    print(app)
    count += 1
