FROM centos:7

RUN yum -y update && yum clean all

RUN yum install -y https://dl.google.com/linux/direct/google-chrome-stable_current_x86_64.rpm && \
    yum install -y https://repo.ius.io/ius-release-el7.rpm && \
    yum install -y python36u python36u-libs python36u-devel python36u-pip

CMD ["/sbin/init"]
