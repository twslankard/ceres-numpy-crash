import os
import sys
import subprocess

from setuptools import setup, find_namespace_packages, Extension
from setuptools.command.build_ext import build_ext


class CMakeExtension(Extension):
    def __init__(self, name, sourcedir=''):
        Extension.__init__(self, name, sources=[])
        self.sourcedir = os.path.abspath(sourcedir)


class CMakeBuild(build_ext):
    def run(self):
        for ext in self.extensions:
            self.build_extension(ext)

    def build_extension(self, ext):
        extdir = os.path.abspath(
            os.path.dirname(self.get_ext_fullpath(ext.name)))
        # required for auto-detection of auxiliary "native" libs
        if not extdir.endswith(os.path.sep):
            extdir += os.path.sep

        cmake_args = [
            '-DCMAKE_BUILD_TYPE=Release',
            '-DCMAKE_LIBRARY_OUTPUT_DIRECTORY=' + extdir,
            '-DPYTHON_EXECUTABLE=' + sys.executable,
            '-DBUILD_SHARED_LIBS:BOOL=OFF'
        ]

        if not os.path.exists(self.build_temp):
            os.makedirs(self.build_temp)

        subprocess.run(
            ['cmake', ext.sourcedir, *cmake_args],
            check=True,
            cwd=self.build_temp,
        )

        subprocess.run(
            ['cmake', '--build', '.', '--config', 'Release'],
            check=True,
            cwd=self.build_temp,
        )


if __name__ == "__main__":
    setup(
        name='ceres-numpy-crash',
        version='0.0.1',
        package_dir={'': 'src'},
        packages=find_namespace_packages(where='src', include='ouster.*'),
        ext_modules=[
            CMakeExtension('ouster.*'),
        ],
        cmdclass={
            'build_ext': CMakeBuild,
        },
        zip_safe=False,
        python_requires='>=3.8, <4',
        install_requires=['numpy==1.26.4']
    )
