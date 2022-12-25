FROM python:3

RUN apt-get -qq update \
    && apt-get -qq install --no-install-recommends openssh-server \
    && apt-get -qq install --no-install-recommends sudo \
    && apt-get -qq install --no-install-recommends rsync \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# setup ssh for user 'ubuntu', password '1234'
RUN useradd -rm -d /home/ubuntu -s /bin/bash -g root -G sudo -u 1000 ubuntu 
RUN  echo 'ubuntu:1234' | chpasswd
RUN service ssh start
EXPOSE 22

# build the project
WORKDIR /usr/src/app
COPY . .
# RUN pip install --no-cache-dir -r requirements.txt

# CMD ["/usr/sbin/sshd","-D"]
CMD [ "python", "src/unit_test.py" ]