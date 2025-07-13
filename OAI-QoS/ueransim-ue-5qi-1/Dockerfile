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

# Generate locale
RUN apt-get update && \
    apt-get install -y locales && \
    locale-gen en_US.UTF-8

# Set environment variables
ENV LANG=en_US.UTF-8
ENV LANGUAGE=en_US:en
ENV LC_ALL=en_US.UTF-8

RUN apt-get update && apt-get install -y curl gnupg lsb-release && \
    curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key | gpg --dearmor -o /usr/share/keyrings/ros-archive-keyring.gpg && \
    echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(lsb_release -cs) main" > /etc/apt/sources.list.d/ros2.list

# Install ROS 2 and other dependencies
RUN apt-get update && \
    apt upgrade -y && \
    apt-get install -y \
    ros-${ROS_DISTRO}-desktop \
    python3-colcon-common-extensions \
    python3-argcomplete \
    ros-dev-tools


WORKDIR /app   

COPY src nodes_4dock/src
COPY dds.xml .
# Source the ROS setup file
RUN echo "source /opt/ros/${ROS_DISTRO}/setup.bash" >> ~/.bashrc
RUN echo "export FASTRTPS_DEFAULT_PROFILES_FILE=/app/dds.xml" >> ~/.bashrc
RUN echo "export RMW_IMPLEMENTATION=rmw_fastrtps_cpp" >> ~/.bashrc
RUN echo "export export ROS_DISCOVERY_SERVER="12.1.1.9:11811"" >> ~/.bashrc
RUN cd nodes_4dock && \
    colcon build 

RUN echo "source /app/nodes_4dock/install/setup.bash" >> ~/.bashrc

