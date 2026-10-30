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
ADD https://github.com/becarie/MnMS.git#generic_execution_script /app
RUN pip install .

WORKDIR /data

ENTRYPOINT ["python", "/app/script/running/run.py"]

# To be launched with:
#
# docker run -it --rm --volume "$PWD:/data" --user "$(id -u):$(id -g)" <image-name> <args...>
#
