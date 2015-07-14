""" Add dynamic library to wheel
"""
from __future__ import print_function

USAGE = """\
add_lib_to_wheel <lib_fname> <wheel-fname> <pkg_sdir>
"""

import sys
import os
import shutil

from delocate.wheeltools import InWheel


def main():
    try:
        lib_fname, wheel_fname, pkg_sdir = sys.argv[1:]
    except (IndexError, ValueError):
        print(USAGE)
        sys.exit(-1)
    for fname in (lib_fname, wheel_fname):
        if not os.path.isfile(fname):
            raise RuntimeError(fname, 'is not a file')
    with InWheel(wheel_fname, wheel_fname):
        shutil.copy2(lib_fname, pkg_sdir)


if __name__ == '__main__':
    main()
