import os
import time
def rep(filename,search,replace):
    data = ""
    with open(filename, 'r') as file:
        data = file.read()
        data = data.replace(search,replace)
    with open(filename, 'w') as file:
        file.write(data)

filepath = input("path:")
sname = input("service name:")
serversn = input("server names:")

rep("sname.ini","sname",sname)
os.rename("wsgi.py",f"{filepath}/wsgi.py")
os.rename("sname.ini",f"{filepath}/{sname}.ini")

rep("servicefile.txt","filepath",filepath)
rep("servicefile.txt","sname",sname)

os.rename("servicefile.txt",f"/etc/systemd/system/{sname}.service")
os.system(f"sudo systemctl start {sname}")
time.sleep(1)
os.system(f"sudo systemctl enable {sname}")

rep("nginx.txt","sname",sname)
rep("nginx.txt","filepath",filepath)
rep("nginx.txt","serversn",serversn)

dat = ""
with open("nginx.txt",'r') as file:
    dat = file.read()
with open("nginx2.txt",'w') as file:
    file.write(dat)

os.rename("nginx.txt",f"/etc/nginx/sites-available/{sname}")
os.rename("nginx2.txt",f"/etc/nginx/sites-enabled/{sname}")

os.system("sudo systemctl restart nginx")
print("done")
exit(0)
