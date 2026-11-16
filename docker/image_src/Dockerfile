# syntax=docker/dockerfile:1

FROM python:3.14-slim

# Environment variables:
# - PIP_NO_CACHE_DIR: don't keep pip's cache in the image
# - PIP_DISABLE_PIP_VERSION_CHECK: silence the warning issued if a newer pip is available online
# - PIP_ROOT_USER_ACTION: silence the warning about running pip as root
ENV \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_ROOT_USER_ACTION=ignore

WORKDIR /app

# FIXME To be installed from PyPI instead
ADD https://github.com/EMob-Lab/MnMS.git /app
RUN pip install .

COPY docker-entrypoint.sh docker-entrypoint-usage.txt /app

WORKDIR /data

ENTRYPOINT ["/app/docker-entrypoint.sh"]

# To be launched with:
#
# docker run -it --rm --volume "$PWD:/data" --user "$(id -u):$(id -g)" -e HOME=/tmp <image-name> <args...>
#
