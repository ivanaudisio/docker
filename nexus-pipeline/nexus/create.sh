#!/bin/bash

jsonFile=$1
name=createRepositories
response="$(curl -Is http://localhost:8081 | head -1)"

printf "Creating Integration API Script from $jsonFile\n\n"

while [[ $response != *"HTTP/1.1 200 OK"* ]]
do
    echo "Checking connectivity to nexus"
    response="$(curl -Is http://localhost:8081 | head -1)"
    sleep 3s
done

curl -v -u admin:admin123 --header "Content-Type: application/json" 'http://nexus:8081/service/siesta/rest/v1/script/' -d @$jsonFile
curl -v -X GET -u admin:admin123 'http://nexus:8081/service/siesta/rest/v1/script'
curl -v -X POST -u admin:admin123 --header "Content-Type: text/plain" "http://nexus:8081/service/siesta/rest/v1/script/$name/run"
