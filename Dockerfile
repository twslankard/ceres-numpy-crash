FROM ubuntu:22.04
ENV DEBIAN_FRONTEND=noninteractive

# Install build dependencies
RUN set -xe \
&& apt-get update \
&& apt-get install -y --no-install-recommends \
    git-core build-essential libceres-dev python3-dev python3-pip
    
COPY pyproject.toml setup.py CMakeLists.txt ceres_repro.py /mnt/
COPY src /mnt/src
RUN cd /mnt && git clone https://github.com/pybind/pybind11.git
RUN pip3 install cmake
RUN cd /mnt && pip3 install .

