cmake_minimum_required(VERSION 3.24)

project(ceres-numpy-crash)
add_subdirectory(pybind11)
find_package(Ceres REQUIRED)

# CMAKE_LIBRARY_OUTPUT_DIRECTORY is set in setup.py to the root of the `ouster`
# namespace, but we have to provide per-target packages directories for each
# extension module here.
set(EXT_DIR ${CMAKE_LIBRARY_OUTPUT_DIRECTORY}/sdk)

# Note: With multi-configuration generators (like for VS), CMake automatically
# appends build-configuration suffix to *_OUTPUT_DIRECTORY properties *unless*
# they contain a generator expression, so we use a noop: $<0:>
# https://cmake.org/cmake/help/latest/prop_tgt/LIBRARY_OUTPUT_DIRECTORY.html
pybind11_add_module(_bindings src/cpp/main.cpp)

target_link_libraries(_bindings
  PRIVATE
    Ceres::ceres
  )
  
set_target_properties(_bindings PROPERTIES
  LIBRARY_OUTPUT_DIRECTORY ${EXT_DIR}/$<0:>)
