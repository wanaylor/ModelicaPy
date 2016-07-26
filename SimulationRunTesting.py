# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 11:49:00 2016

@author: wn9
"""
"""
this script is useless
"""
import subprocess

#log = "C:\\Users\\wn9\\Documents\\Testing Results\\stdout.log"

#logFil = open(log, 'w')
    #logFilNam=os.path.join(worDir, 'stdout.log')
    #logFil = open(logFilNam, 'w')
#PIPE = subprocess.PIPE
#subprocess.Popen(["Dymola", "C:\Users\wn9\Documents\TRANSFORM-Library\Resources\Scripts\Dymola\PHTS_v1_Test2.mos"], stdout=logFil)
#"C:\Users\wn9\Documents\TRANSFORM-Library\Resources\Scripts\Dymola\PHTS_v1_Test2.mos"
#for line in proc.stdout:
  #  print line

#proc.communicate("C:\Users\wn9\Documents\TRANSFORM-Library\Resources\Scripts\Dymola\PHTS_v1_Test2.mos")

#pro = subprocess.Popen(args=cmd,
#                           stdout=logFil,
#                           stderr=logFil,
#                           shell=False,
#                           cwd=worDir)

import multiprocessing

pool = multiprocessing.Pool(8)

print pool(1)