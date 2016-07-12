# -*- coding: utf-8 -*-
"""
Created on Thu Jun 09 14:13:04 2016

@author: wn9
"""
print """
****************Unit Testing for ModelicaPy v1.0****************
---- This is a unit test for any Modelica Library that
---- utilizes a modified version of the BuildingsPy library.
---- This script was designed to run regression tests when
---- the resources folder is not in the same directory as
---- the top level package.mo file (the origional BuildingsPy
---- assumes Resources and top level package.mo are in the
---- same direcroty).
----
---- To run properly Dymola must be on the system path.
----
---- :param libHome: directory that contains top level package.mo
---- :param rootDir: directory that contains Resources folder.
----
---- This script assumes it is within ModelicaPy itself.
---- However, it can be modified to:
---- *Assume Buildingspy is on system path
----         -Comment out line 52 and 64
----         -Uncomment line 63
---- *Hardcode in a custom path to BuildingsPy
----         -Comment out line 52
----         -Uncomment line 54 and enter path manually
----
---- This script will run simulations, gather output, and
---- compare to existing results issuing a pass or fail.
---- If there are no stored results or results differ you
---- can accept or reject simulation results.
----
---- For more documentation on BuildingsPy please visit
---- http://simulationresearch.lbl.gov/modelica/buildingspy/
************************************************************
"""
import sys, os


def run_unit_tests(libHome, rootDir):
    """
    function run_unit_tests takes inputs that are the absolute path to the
    resources folder and top level package.mo
    this is important since BuildingsPy was written in a way that the resources
    folder and package.mo must be in the same directory. This does not work in our
    application since we want to protect the resources folder.

    """
    BPDir = os.path.abspath(os.path.dirname(sys.argv[0]))

    #BPDir = ""

    print "Looking for BuildingsPy in" , BPDir
    sys.path.append(BPDir)

    #log files are written to the working directory
    os.chdir(rootDir)


    #import buildingspy.development.regressiontesttwo as regTest
    import buildingspy.development.regressiontesttwo as regTest
    tester=regTest.Tester(check_html=False)
    tester.setLibraryRoot(libHome, rootDir)
    #tester.showGUI(show=True)
    tester.setNumberOfThreads(4)
    #tester.setSinglePackage("C:\Users\wn9\Documents\Dymola\NHES-ORNL\NHES-ORNL\Resources\Scripts\Dymola\FuelTest")

    numPassed = 0
    numPassedWarn = 0
    numFailed = 0
    rv=tester.run()
    if rv == 0:
      print "#  BuildingsPy Test Framework Returns: ", rv ," (PASSED)"
      numPassed = numPassed + 1
    elif rv == 2:
      print "#  BuildingsPy Test Framework Returns: ", rv ," (PASSED WITH WARNINGS)"
      numPassedWarn = numPassedWarn + 1
    else:
      print "#  BuildingsPy Test Framework Returns: ", rv ," (FAILED)"
      numFailed = numFailed + 1

if __name__ == '__main__':
    

    #prevents escape characters in path
    
    hom = r"C:\Users\wn9\Documents\Dymola\NHES-ORNL\NHES-ORNL\NHES" #directory with package.mo file
    res = r"C:\Users\wn9\Documents\Dymola\NHES-ORNL\NHES-ORNL" #directory containing Resources folder


    run_unit_tests(hom,res)
