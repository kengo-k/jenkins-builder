#!/usr/bin/env python3
import datetime
import os
from string import Template

from dotenv import load_dotenv

import jenkins

load_dotenv()

JENKINS_HOST = os.getenv("JENKINS_HOST")
JENKINS_USER = os.getenv("JENKINS_USER")
JENKINS_PASSWORD = os.getenv("JENKINS_PASSWORD")

server = jenkins.Jenkins(JENKINS_HOST, username=JENKINS_USER, password=JENKINS_PASSWORD)

f = open("../../template/pipeline.xml", "r")
xml = f.read()
f.close()

tpl = Template(xml)
xml = tpl.substitute(
    repository_path="https://github.com/kengo-k/jenkins-builder.git",
    script_path="jenkins/pipelines/samples/Jenkinsfile",
)

now = datetime.datetime.today()
strnow = now.strftime("%Y%m%d%H%M%S")

server.create_job(f"Test_{strnow}", xml)
