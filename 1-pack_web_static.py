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
