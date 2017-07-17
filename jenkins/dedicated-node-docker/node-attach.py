############################################################
# This script creates a node on the Jenkins master through
# a REST API call by executing a groovy script. After creating
# it, the corresponding command is executed to attach it
# through a JNLP connection.
############################################################
import re
import time
import os
from mechanize import Browser

max_retries=20                          # maximum number of times to retry.
interval=5                              # number of seconds to wait between retries.
url= os.environ['JENKINS_URL']          # Jenkins URL. Environmet var defined in docker-compose.
node_name = os.environ['NODE_NAME']     # Name of the node to be created. Environmet var defined in docker-compose.
br = Browser()                          # Initianing Browser
br.set_handle_robots(False)             # Ignore robots
tried=0                                 # Initiating counter for connection tries.
connected = False                       # Initianing connection flag.
message_success = "Jenkins URL reached successfully"
message_retry = "Connection with Jenkins could not be establish"

while not connected:
    try:
        response = br.open(url)         # attempt to open Jenkins URL.
        connected = True                # if line above fails, this is never executed.
    except:
        print message_retry
        time.sleep(interval)            # wait until next retry.
        tried += 1                      # increment number of retries.
    if tried > max_retries:
        exit()                          # if max number of retries is reached the code below is not executed.

print message_success

if not os.path.isdir("/node_workspace"):
    os.system("mkdir /node_workspace")

# Expand /tmp size to 1.5G since a lower ammount does not allow the node to be used by Jenkins.
os.system("mount -t tmpfs -o size=1610612736,mode=1777 overflow /tmp")

# Replacing groovy script variables with corresponding values. Environmet vars are defined in docker-compose.
os.system("sed -i 's/node_name_value/"+os.environ['NODE_NAME']+"/' /home/node-create.groovy")
os.system("sed -i 's/node_labels_value/"+os.environ['NODE_LABELS']+"/' /home/node-create.groovy")
os.system("sed -i 's/node_executors_value/"+os.environ['NODE_EXECUTORS']+"/' /home/node-create.groovy")
os.system("sed -i 's/node_description_value/"+os.environ['NODE_DESCRIPTION']+"/' /home/node-create.groovy")

# Execute RESP API call that executes a groovy script under Jenkins to create a new node.
os.system('curl -d "script=$(cat /home/node-create.groovy)" -v ' + url + '/scriptText')

# Download slave.jar file from Jenkins master. This is needed to attach through JNLP
os.system('wget ' + url + '/jnlpJars/slave.jar')

# Execute required command to connect this container to the Jenkins master as a node.
os.system('nohup java -jar slave.jar -jnlpUrl ' + url + '/computer/' + node_name + '/slave-agent.jnlp &')
