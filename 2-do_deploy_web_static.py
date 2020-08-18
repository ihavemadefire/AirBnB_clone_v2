#!/usr/bin/python3
# This is a Fabfile that will scp the static files
# to the remote servers
from fabric.api import put
from fabric.api import run
import os.path
from fabric.api import env

env.hosts = ["35.237.36.104", "34.74.62.199"]


def do_deploy(archive_path):
    """This does deploy"""

    # check that passed file exists
    if os.path.isfile(archive_path) is False:
        return False

    # get file name from file path
    file_name = archive_path.split("/")[-1]
    # remove file extension
    no_ext = file_name.split(".")[0]

    # put the file on the server
    if put(archive_path, "/tmp/{}".format(file_name)).failed is True:
        return False
    # mkdir for new release
    if run("mkdir -p /data/web_static/releases/{}/".
           format(no_ext)).failed is True:
        return False
    # decompress file in tmp but move it to releases folder
    if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".
           format(file_name, no_ext)).failed is True:
        return False
    # remove archive file
    if run("rm /tmp/{}".format(file_name)).failed is True:
        return False
    # Move the contents of the folder up one folder
    if run("mv /data/web_static/releases/{}/web_static/* \
           /data/web_static/releases/{}/"
           .format(no_ext)).failed is True:
        return False
    # kill empty folder
    if run("rm -fr /data/web_static/releases/{}/web_static".
           format(no_ext)).failed is True:
        return False
    # delete symbolic link
    if run("rm -fr /data/web_static/current").failed is True:
        return False
    # create new symbolic link
    if run("ln -s /data/web_static/releases/{}/ /data/web_static/current".
           format(no_ext)).failed is True:
        return False
    return True
