import re
import time
from mechanize import Browser
import os # needed to execute shell commands - ex. os.system('ls')
import socket

hostname = socket.gethostname()

def activate_cb_instance(url):
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

    for form in br.forms():
        if count == 2:
            formname = form.attrs['name']
        count = count + 1
    br.select_form(name=formname)

    response = br.response()

    br.form['firstName'] = 'test'
    br.form['lastName'] = 'test'
    br.form['email'] = 'test@mail.com'
    br.form['company'] = 'test'
    br.form.find_control(name='agree').items[0].selected = True #set all checkboxes to true

    response = br.submit() # submit form with new parameters

# Activate Jenkins operation center
url="http://localhost:8080/registration#btn-com_cloudbees_jenkins_plugins_license_nectar_EvaluationRegistrar" # URL to open
activate_cb_instance(url)

os.system("sed -i 's/hostname/"+hostname+"/g' /home/configure_attach_cjoc.groovy")
# Get CLI from operation center
os.system('wget http://cjoc:8080/jnlpJars/jenkins-cli.jar')
# Attach master to operation center
os.system('java -jar jenkins-cli.jar -s http://cjoc:8080/ groovy /home/configure_attach_cjoc.groovy')
