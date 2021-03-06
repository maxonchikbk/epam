#!/bin/bash
yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo && \
yum install -y docker-ce docker-ce-cli containerd.io && systemctl enable --now docker && \
usermod -aG docker $(whoami) && usermod -aG docker vagrant && \
newgrp docker && ln -sf /usr/bin/python3 /usr/bin/python && pip3 install docker-compose && setenforce 0