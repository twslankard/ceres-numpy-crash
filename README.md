libunwind-crash
=================

Tom Slankard <tomslankard.dugout268@passmail.net>

This repository contains an example Python module with a native extension linked to libunwind (provided by the `libunwind8` Debian package.)

For some reason, when used in conjunction with numpy, the script `repro.py` crashes with SIGSEGV or abort. What's more, if the order of imports are swapped in the script, the problem goes away. The reasons are beyond my meager knowledge.

The notable factors appear to be

1. Numpy 1.26.4 (which uses a particular version of https://github.com/intel/x86-simd-sort). Upgrading numpy seems to resolve the problem. The submodule commit `3dd2d13e7ad7bd0285a58bf7162bb01748ca2017` also seems to resolve the issue.
2. `libunwind8` the Debian package provided by apt. Building libunwind from source and replacing the one provided by this package fixes the problem, evidently.
3. A native extension built with pybind11 that throws an exception from C++.

Building
========

    $ docker build . -t libunwind-crash

Running
=======

The behavior is nondeterministic. Most of the time, the script terminates with SIGSEGV - other times it exits normally.

    $ docker run --rm -i -t libunwind-crash /bin/bash
    # cd /mnt
    # python3 repro.py
    hello
    Segmentation fault (core dumped)
    # python3 repro.py
    hello
    Aborted (core dumped)

    ... etc
