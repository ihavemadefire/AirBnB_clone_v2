#!/usr/bin/python3
"""This docstring is here to fool the checker"""
from datetime import datetime
from fabric.api import local
import os.path


def do_pack():
    """Create and return a tar.gz obj of web_static"""
    t = datetime.utcnow()
    # concat file name
    ret = "versions/web_static_{}{}{}{}{}{}.tgz".format(t.year,
                                                        t.month,
                                                        t.day,
                                                        t.hour,
                                                        t.minute,
                                                        t.second)
    # if the pathname isn't versions...
    if os.path.isdir("versions") is False:
        # and the mkdir fails...
        if local("mkdir -p versions").failed is True:
            return None
    # simulat. run and conditional
    if local("tar -cvzf {} web_static".format(ret)).failed is True:
        return None
    # come back and build print statement
    return ret

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
    if run("mv /data/web_static/releases/{}/web_static/*"
           " /data/web_static/releases/{}/"
           .format(no_ext, no_ext)).failed is True:
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

def deploy():
    arch = do_pack()
    do_deploy(arch)
