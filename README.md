# DOCKER

## Useful Commands

#### Removing all images under the <none> tag

docker rmi $(docker images | awk '$2=="<none>"' | awk '{print $3}')
