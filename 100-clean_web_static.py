#!/usr/bin/python3
"""deletes out-of-date archives"""

from fabric.api import env, run, local
from datetime import datetime
from os.path import exists

env.hosts = ['100.26.10.68', '34.232.52.36']
env.user = 'ubuntu'

def do_clean(number=0):
    """deletes out of date archive
    """
    number = int(number)
    if number < 1:
        number = 1

    try:
        archives = local("ls -lt versions", capture=True).split("\n")
        archives = ["versions/" + archive for archive in archives]

        for archive in archives[number:]:
            local("rm -rf {}".format(archive))

        releases = run("ls -lt /data/web_static/releases").split("\n")
        for release in releases[number:]:
            run("rm -rf /data/web_static/releases/{}".format(release))
    except:
        pass
