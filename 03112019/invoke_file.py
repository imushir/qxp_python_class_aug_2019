import subprocess

s = subprocess.check_output(r"C:\Users\allusers\AppData\Local\Programs\Python\Python37-32\python.exe system_argument.py 12 23", shell=True)
print(s)