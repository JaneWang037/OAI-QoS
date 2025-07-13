# Use the OAI NR UE base image as the starting point
FROM ueransim:v3.2.7-ubuntu

# Set environment variables for ROS 2 installation
ENV DEBIAN_FRONTEND=noninteractive
ENV ROS_DISTRO=humble

# Update package list and install dependencies
RUN apt-get update && \
    apt-get install -y \
    sudo \
    curl \
    gnupg2 \
    lsb-release \
    locales \
    build-essential \
    git \
    wget \
    software-properties-common \
    && rm -rf /var/lib/apt/lists/*

# Set up locale
RUN sudo locale-gen en_US.UTF-8 && \
    sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8

ENV LANG=en_US.UTF-8 \
    LC_ALL=en_US.UTF-8

RUN add-apt-repository universe && \
    curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg && \
    echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" |sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null

# Install ROS 2 and other dependencies
RUN apt-get update && \
    apt upgrade -y && \
    apt-get install -y \
    ros-${ROS_DISTRO}-desktop \
    ros-dev-tools



WORKDIR /app   


COPY dds.xml .
# Source the ROS setup file
RUN echo "source /opt/ros/${ROS_DISTRO}/setup.bash" >> ~/.bashrc
RUN echo "export FASTRTPS_DEFAULT_PROFILES_FILE=/app/dds.xml" >> ~/.bashrc
RUN echo "export RMW_IMPLEMENTATION=rmw_fastrtps_cpp" >> ~/.bashrc


