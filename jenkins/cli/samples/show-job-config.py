#!/usr/bin/env python3
import os

from dotenv import load_dotenv

import jenkins

load_dotenv()

JENKINS_HOST = os.getenv("JENKINS_HOST")
JENKINS_USER = os.getenv("JENKINS_USER")
JENKINS_PASSWORD = os.getenv("JENKINS_PASSWORD")

server = jenkins.Jenkins(JENKINS_HOST, username=JENKINS_USER, password=JENKINS_PASSWORD)

# 登録されている全ジョブの一覧を取得
jobs = server.get_jobs()
if len(jobs) > 0:
    # 先頭のジョブの情報を取得する
    j = jobs[0]
    # ジョブ名からジョブの設定情報を取得
    config = server.get_job_config(j["name"])
    print(config)
