# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 10:26:35 2016

@author: wn9
"""

def runSimulation(worDir, cmd):
    ''' Run the simulation.

    :param worDir: The working directory.
    :param cmd: An array which is passed to the `args` argument of
                :mod:`subprocess.Popen`

    .. note:: This method is outside the class definition to
              allow parallel computing.
    '''

    import subprocess
    runfil = "C:\Users\wn9\Documents\TRANSFORM-Library\Resources\Scripts\Dymola\PHTS_v1_Test2.mos"
    logFilNam=os.path.join(worDir, 'stdout.log')
    logFil = open(logFilNam, 'w')
    pro = subprocess.Popen(args=cmd,
                           #stdin=runfil,
                           stdout=logFil,
                           stderr=logFil,
                           shell=False,
                           cwd=worDir)
    print "subprocess popen complete"
    try:
       print "waiting.."
       retcode = pro.wait()
       print "closing logfil..."
       logFil.close()
       if retcode != 0:
            print "Child was terminated by signal", retcode
            return retcode
       else:
            return 0
    except OSError as e:
        sys.stderr.write("Execution of '" + " ".join(map(str, cmd)) + " failed.\n" +
                         "Working directory is '" + worDir + "'.")
        raise(e)
    except KeyboardInterrupt as e:
        pro.kill()
        sys.stderr.write("Users stopped simulation in %s.\n" % worDir)



import sys, os

BPDir = os.path.abspath(os.path.dirname(sys.argv[0]))
print "Looking for BuildingsPy in" , BPDir
sys.path.append(BPDir)
#os.chdir(rootDir)

cmd = ["Dymola", "C:\Users\wn9\Documents\TRANSFORM-Library\Resources\Scripts\Dymola\PHTS_v1_Test2.mos"]
WorDir = "C:\Users\wn9\Documents\TRANSFORM-Library\Resources\Scripts\Dymola"
 
#import buildingspy.development.regressiontesttwo as regTest

runSimulation(WorDir,cmd)