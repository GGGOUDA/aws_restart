# import os
# os.system("ls")

import subprocess
# subprocess.run(["ls"])
# subprocess.run(["ls","-l"])
# subprocess.run(["ls","-l","test.py"])

command="ps"
commandArgument="-x"
print(f'Gathering system information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])






