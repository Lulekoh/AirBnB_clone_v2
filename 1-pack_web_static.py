#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive
"""
from datetime import datetime
from fabric.api import *


def do_pack():
    """
    Return archive path or None
    """
    time = datetime.now()
    archive_path = "web_static_{}.tgz".format(
            time.strftime("%Y%m%d%H%M%S"))
    local('mkdir -p versions')
    create = local('tar -cvzf versions/{} web_static'.format(
        archive_path))
    if create is not None:
        return archive_path
    else:
        return None
