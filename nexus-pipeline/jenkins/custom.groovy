import jenkins.model.*
import jenkins.*
import hudson.model.*
import hudson.*

Jenkins.instance.setSlaveAgentPort(50000)

jlc = JenkinsLocationConfiguration.get()
jlc.setUrl("http://jenkins:8080")
jlc.save()
