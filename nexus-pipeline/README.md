# Nexus Pipeline

#### Jenkins Container

running on http://localhost:8080

This instance uploads a pipeline called `nexus-pipeline` with the following stages:

> Note: Be aware that the nexus container needs to be already up before executing the pipeline

- *Build Artifact:* Creates a file _example.txt_
- *Tests:* This stage is symbolic and does not perform any tasks. Unit testing would be here
- *Upload to Nexus (alpha):* The file is uploaded into the nexus repository under the _alpha_ repository
- *QA:* This is also a symbolic stage where manual testing is done. It needs to be approved in order for the pipeline to continue. If not approved the pipeline does not proceed.
- *Promote artifact to Beta:* Automatically promotes the file under the _alpha_ repository into the _beta_ repository.

The steps are coded under a declarative pipeline. For more information you can refer to [Pipeline Syntax](https://jenkins.io/doc/book/pipeline/syntax/)

#### Nexus Container

running on http://localhost:8081

> Note: This container takes a while to come up. Please wait for it.

For more details on this container go to [Nexus Section](nexus/README.md)

#### Pending features

- [ ] Validation that the repository exists
- curl -X GET -sI -u admin:admin123 http://nexus:8081/repository/beta/myApp/2/example.txt | head -1
- [ ] Validation that the artifact has been uploaded
- [ ] Validation that the artifact has been promoted
- [ ] Pass methods above into a library
