FROM python:3.7

ENV DEBIAN_FRONTEND=noninteractive

# Or your actual UID, GID on Linux if not the default 1000
ARG USERNAME=davidfrancoeur
ARG GROUPNAME=staff
ARG USER_UID=501
ARG USER_GID=20

ENV SHELL /bin/bash
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

RUN apt-get update \
    && apt-get install -y sudo \
    && if [ "$USER_UID" != "1000" ]; then echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME; fi \
    && echo node ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/node \
    && chmod 0440 /etc/sudoers.d/$USERNAME \
    && apt-get autoremove -y \
    && apt-get clean -y

RUN groupdel dialout && groupmod --gid $USER_GID $GROUPNAME && useradd -s /bin/bash --uid $USER_UID --gid $USER_GID -m $USERNAME

RUN pip install pipenv
