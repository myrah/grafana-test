#!/usr/bin/python

import requests, sys, os, json, glob


access_token = 'eyJrIjoiWFA2MzFSZjZLRG5SZjFHRDNsNlROQktwWjd3Q2YyRkoiLCJuIjoiYWRtaW5rZXkiLCJpZCI6MX0='
headers={
    'Authorization': 'Bearer ' + 'eyJrIjoiWFA2MzFSZjZLRG5SZjFHRDNsNlROQktwWjd3Q2YyRkoiLCJuIjoiYWRtaW5rZXkiLCJpZCI6MX0=',
    'content-type': 'application/json',
    'Accept': 'application/json'
    }
dsurl = 'http://0.0.0.0:3000/api/datasources'

dburl = 'http://0.0.0.0:3000/api/dashboards/db'

db_list = glob.glob("/var/jenkins_home/workspace/grafana-test/dashboards/dev/*.json")
print(db_list)
for db in db_list:
    contentdb = open(db, 'rb').read()
    response = requests.post(dburl, data=contentdb, headers=headers)
    print(response.text)

ds_list = glob.glob("/var/jenkins_home/workspace/grafana-test/datasources/dev/*.json")
print(ds_list)
for ds in ds_list:
    contentds = open(ds, 'rb').read()
    response = requests.post(dsurl, data=contentds, headers=headers)
    print(response.text)
