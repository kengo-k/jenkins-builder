#!/usr/bin/env python3
import os

from dotenv import load_dotenv

import jenkins

load_dotenv()

JENKINS_HOST = os.getenv("JENKINS_HOST")
JENKINS_USER = os.getenv("JENKINS_USER")
JENKINS_PASSWORD = os.getenv("JENKINS_PASSWORD")

server = jenkins.Jenkins(JENKINS_HOST, username=JENKINS_USER, password=JENKINS_PASSWORD)

user = server.get_whoami()
full_name = user["fullName"]
id = user["id"]

print(full_name)
print(id)
