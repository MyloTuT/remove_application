#!/usr/bin/env python3
#
# This script will remove MS Office 2011
# By: Myles Rayfield

import sys
import os

applications = '/Applications'
ms_office = '/Applications/Microsoft\Office'
ms_link = 'Applications/Microsoft Link.app'

for app in os.listdir(applications):
    #os.remove('Microsoft Office 2011')
    os.remove('Docker.app')
    print(app)
