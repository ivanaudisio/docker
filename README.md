# DOCKER

## Useful Commands

#### Removing all images under the \<none\> tag

docker rmi $(docker images | awk '$2=="<none>"' | awk '{print $3}')

#### Removing all images that contain one specific string

docker rmi $(docker images | awk '$1 ~ "string"')
