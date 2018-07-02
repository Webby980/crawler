## Python Crawler

A program which will crawl an application and detect SQL injection vulnerabilities.

## Introduction

This demo is a dockerised application that can check for SQL injection vulnerabilities and exploit these in the DVWA (http://www.dvwa.co.uk/)

## Prerequisites

For MacOS users:
* Docker for Mac v 17.06 - 17.12

For linux distributions (untested):
* A recent Docker installation


## Run the demo

```
./run.sh app <dnvw_username> <dnvw_password> <dnvw_base_url>
```

The application will be available on [localhost:8080](http://localhost:8080) and supports three endpoints:

## API endpoints

Note: All endpoints will return JSON

`/check-vulnerability`

This endpoint will check an application for SQL injection vulnerabilities. A list of vulnerable
pages will be returned. The format of the vulnerable pages will be `<site>-<endpoint>-<test_purpose>`.

Example response:

```
{"vulnerable": "[\"dvwa-sqli-check-vulnerability.\"]"}
```

`/get-db-users`

This endpoint will exploit an application to retrieve a list of its database users.

Example response:

```
{"/crawler_outputs/dvwa-sqli-get-db-users.html": ["Gordon, Brown", "Pablo, Picasso", "Bob, Smith"]}
```

`/get-db-version`

This endpoint will exploit an application to retrieve its database version.

Example response:

```
{"db_version": "5.0.0"}
```


## Teardown
Once you're finished with the demo there are some cleanup functions to clear away unwanted images and containers:
```
./run.sh clearIntermediateImages
./run.sh clearAllContainers
```