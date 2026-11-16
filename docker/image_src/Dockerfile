# syntax=docker/dockerfile:1

FROM python:3.14-slim

# Image metadata (title, description...) is defined in labels.txt,
# and applied by the publishing workflow.

# Environment variables:
# - PIP_NO_CACHE_DIR: don't keep pip's cache in the image
# - PIP_DISABLE_PIP_VERSION_CHECK: silence the warning issued if a newer pip is available online
# - PIP_ROOT_USER_ACTION: silence the warning about running pip as root
ENV \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_ROOT_USER_ACTION=ignore

# App installation
WORKDIR /app
# TODO To be installed from PyPI instead + make the MnMS version explicit
ADD https://github.com/EMob-Lab/MnMS.git /app
RUN pip install .
COPY entrypoint.sh entrypoint-usage.txt /app

# Runtime configuration
WORKDIR /data
ENTRYPOINT ["/app/entrypoint.sh"]

# To be launched with:
#
# docker run -it --rm --volume "$PWD:/data" <image-name> <args...>
#
# ... or if the docker engine runs as root:
#
# docker run -it --rm --volume "$PWD:/data" --user "$(id -u):$(id -g)" -e HOME=/tmp <image-name> <args...>
#
# Use the launchers scripts to avoid typing this command line manually:
# - for MacOS/Linux: https://raw.githubusercontent.com/EMob-Lab/MnMS/refs/heads/main/docker/launchers/mnms-docker
# - for Windows: TODO add launcher
