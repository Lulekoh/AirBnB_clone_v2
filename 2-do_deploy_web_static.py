#!/usr/bin/python3
"""
Fabric script based on previous task that distributes .tgz archive
"""
from fabric.api import put, run, env
from datetime import datetime
from os import path

env.hosts = ['35.153.98.141', '3.85.168.83']
env.user = 'ubuntu'
env.key_file = '~/.ssh/school'


def do_depoy(archive_path):
    """
    Distribute files to web server and deploy
    """
    try:
        if not (path.exists(archive_path)):
            return False
        put(archive_path, '/tmp/')
        timestamp = archive_path[-18:-4]
        path_n = '/data/web_static/releases/web_static'
        run(
                'sudo mkdir -p {}_{}/'.format(path_n, timestamp))
        run('sudo tar -xzf /tmp/web_static_{}.tgz -C {}_{}/'.format(
            timestamp, path_n, timestamp))
        run(
                'sudo rm -rf {}_{}/web-static'.format(
                    path_n,
                    timestamp))
        run('sudo ln -s {}_{}/ /data/web_static/current'.format(
            path_n, timestamp))
    except Exception as err:
        print(err)
        return False
    return True
