sot-openhrp
===========

This packages provides an OpenHRP plug-in which allows a dynamic graph
evaluation to be used inside the OpenHRP framework.  Robot state is
pushed as an input of the data-flow and its state is used as the
data-flow output.

Setup
-----

To compile this package, it is recommended to create a separate build
directory:

    mkdir _build
    cd _build
    cmake [OPTIONS] ..
    make install

Please note that CMake produces a `CMakeCache.txt` file which should
be deleted to reconfigure a package from scratch.
