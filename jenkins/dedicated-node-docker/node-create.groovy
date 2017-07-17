import jenkins.model.*
import hudson.model.*
import hudson.slaves.*

name = node_name_value
executors = node_executors_value
labels = node_labels_value
description = node_description_value
directory = "/node_workspace"

Jenkins.instance.addNode(
  new DumbSlave(
    "${name}",
    "${description}",
    "${directory}",
    "${executors}",
    Node.Mode.NORMAL,
    "${labels}",
    new JNLPLauncher(),
    new RetentionStrategy.Always(),
    new LinkedList()))
