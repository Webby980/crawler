#!/usr/bin/env bash
#set -e

function app() {
    local dvwaUsername=$1
    local dvwaPassword=$2
    local dvwaBaseUrl=$3

    docker build . -t dvwa-crawler
    docker rm -f dvwa-crawler
    docker run -it -e "DVWA_USERNAME=${dvwaUsername}" -e "DVWA_PASSWORD=${dvwaPassword}" -e "DVWA_BASE_URL=${dvwaBaseUrl}" --publish 8080:8080 --name dvwa-crawler dvwa-crawler
}

function clearIntermediateImages() {
    docker rmi $(docker images | grep "^<none>" | awk "{print $3}")
}

function clearAllContainers() {
    docker stop $(docker ps -a -q)
    docker rm $(docker ps -a -q)
}

$@