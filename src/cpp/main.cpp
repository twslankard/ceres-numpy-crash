#include <iostream>
#include <pybind11/pybind11.h>

namespace py = pybind11;

PYBIND11_MODULE(_bindings, m) {
    m.def("foo", []{
        std::cerr << "hello" << std::endl;
        throw std::runtime_error("whoopsie!");
    });
}
