# A simple setup script to create an executable using PyQt4/PySide. This also
# demonstrates the method for creating a Windows executable that does not have
# an associated console.
#
# Thisis a very simple type of PyQt4/PySide application
#
# Run the build process by running the command 'python setup.py build'
# on a mac run 'python setup.py bdist_mac' to create an app.
# or run 'python setup.py bdist_dmg' to create a dmg.
#
# If everything works well you should find a subdirectory in the build
# subdirectory that contains the files needed to run the application

application_title = "mp3tagstripper" #what you want to application to be called
main_python_file = "main.py" #the name of the python file you use to run the program

import sys

from cx_Freeze import setup, Executable

base = None
if sys.platform == "win32":
    base = "Win32GUI"

includes = ["atexit","re"]

setup(
    name = application_title,
    version = "0.1",
    description = "Sample cx_Freeze PyQt4 script",
    options = {"build_exe" : {"includes" : includes }},
    executables = [Executable(main_python_file, base = base)]
)

