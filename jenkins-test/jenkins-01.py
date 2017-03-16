#!/usr/bin/env python
#coding = utf-8

import jenkins

def Create_Node
server = jenkins.Jenkins(url="http://xxxx", username='xxxxx', password='XXX')
user = server.get_whoami()


# create node with parameters
params = {'port': '22','username': 'root','credentialsId': 'xxxxxxx','host': '127.0.0.1'}
server.create_node(
    name='AAAAA',
    nodeDescription='dep-test',
    remoteFS='/home/',
    labels='precise',
    exclusive=True,
    launcher=jenkins.LAUNCHER_SSH,
    launcher_params=params)

nodes = server.get_nodes()
print nodes