# syntax=docker/dockerfile:1


FROM python:3.14-slim

ENV PATH="/app/venv/bin:$PATH"

WORKDIR /app

RUN python -m venv /app/venv

# FIXME To be installed from PyPI instead
ADD https://github.com/becarie/MnMS.git#generic_execution_script /app
RUN pip install .

WORKDIR /data

ENTRYPOINT ["python", "/app/script/running/run.py"]

# To be launched with:
#
# docker run -it --rm --volume "$PWD:/data" --user "$(id -u):$(id -g)" <image-name> <args...>
#
