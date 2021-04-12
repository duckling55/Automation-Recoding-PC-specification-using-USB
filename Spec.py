# import module
import subprocess

# traverse the info
Id = subprocess.check_output(['systeminfo']).decode('utf-8').split('\n')
new = []

report = open('specification.txt', 'w')
# arrange the string into clear info
for item in Id:
    new.append(str(item.split("\r")[:-1]))
for i in new:
    report.write(i[2:-2]+'\n')
report.close()
