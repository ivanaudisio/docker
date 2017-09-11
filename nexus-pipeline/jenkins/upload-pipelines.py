import re
import time
from mechanize import Browser
import os # needed to execute shell commands - ex. os.system('ls')
import socket

hostname = socket.gethostname()

def confirm_master_runing(url):
    max_retries=1000 # maximum number of times to retry
    interval=3 # number of seconds to wait between retries
    br = Browser()
    br.set_handle_robots(False)
    tried=0
    connected = False
    count = 1 # count forms found in url

    while not connected:
        try:
            response = br.open(url)
            connected = True # if line above fails, this is never executed
        except:
            print "connection could not be establish"
            time.sleep(interval)
            tried += 1
        if tried > max_retries:
            exit()

# Activate Jenkins operation center
url="http://localhost:8080/" # URL to open
confirm_master_runing(url)

os.system("wget http://localhost:8080/jnlpJars/jenkins-cli.jar -P /home")
os.system("java -jar /home/jenkins-cli.jar -s http://localhost:8080 create-job nexus-pipeline < /tmp/jobs/nexus-pipeline/config.xml")
