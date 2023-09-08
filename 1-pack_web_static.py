#!/usr/bin/python3
"""compress html files"""

from fabric.api import local
from datetime import datetime

def do_pack():
	"""
	do_pack: generates .tgz file archive
	"""
	time = datetime.now().strftime('%Y%m%d%H%M%S')
	archive_name = "web_static_{}.tgz".format(time)
	try:
	    local("mkdir -p ./versions")
	    local("tar -cvzf versions/{} web_static".format(archive_name))
	    return "versions/{}".format(archive_name)
	except:
	    return None
