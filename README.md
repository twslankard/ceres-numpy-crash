ceres-numpy-crash
=================

Tom Slankard <tomslankard.dugout268@passmail.net>

This repository contains an example Python module with a native extension linked to ceres-solver (provided as a Debian package.)

For some reason, when used in conjunction with numpy, the script `ceres_repro.py` crashes with SIGSEGV. What's more, if the order of imports are swapped in the script, the problem goes away. The reasons are beyond my meager knowledge.

The notable factors appear to be

1. Numpy 1.26.4 (which uses a particular version of https://github.com/intel/x86-simd-sort). Upgrading numpy seems to resolve the problem.
2. Ceres (provided by apt.) Building Ceres using another source (e.g. vcpkg) seems to resolve the problem.
3. A native extension built with pybind11 that throws an exception from C++.

Building
========

    $ docker build . -t ceres-numpy-crash

Running
=======

The behavior is nondeterministic. Most of the time, the script terminates with SIGSEGV - other times it exits normally.

    $ docker run --rm -i -t ceres-numpy-crash /bin/bash
    # cd /mnt
    # python3 ceres_repro.py
    # python3 ceres_repro.py
    # python3 ceres_repro.py
    # python3 ceres_repro.py

