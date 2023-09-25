#!/usr/bin/python3
"""functions to upload to web sever"""

from fabric.api import *
import os


env.hosts = ['100.26.10.68', '34.232.52.36']
env.user = 'ubuntu'

def do_deploy(archive_path):
	"""
	do_deploy: distibue archive to
	web_servers
	archive_path: path to arhives
	"""
	if not os.path.exists(archive_path):
	    return False

	try:
	    file_name = os.path.basename(archive_path)
	    no_ext = file_name.split('.')[0]
	    put(archive_path, '/tmp/')
	    run("mkdir -p /data/web_static/releases/{}/".format(no_ext))
	    run("tar -xzvf /tmp/{} -C /data/web_static/releases/{}".format(file_name, no_ext))
	    run("rm /tmp/{}".format(file_name))
	    run("mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/".format(no_ext, no_ext))
	    run("rm -rf /data/web_static/releases/{}/web_static".format(no_ext))
	    run("rm /data/web_static/current")
	    run("ln -s /data/web_static/releases/{}/ /data/web_static/current".format(no_ext))
	    print("new version deployed")
	    return True
	except Exception as e:
	    print(e)
	    return False

