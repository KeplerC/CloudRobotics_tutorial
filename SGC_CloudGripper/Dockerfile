FROM osrf/ros:humble-desktop 
RUN apt update && apt install -y build-essential curl pkg-config libssl-dev protobuf-compiler clang python3-pip
RUN curl https://sh.rustup.rs -sSf | bash -s -- -y
ENV PATH="/root/.cargo/bin:${PATH}"
RUN pip install requests
WORKDIR /fog_ws 
# changed to .
# COPY ./rt-fogros2 /fog_ws/src/rt-fogros2
WORKDIR /fog_ws/src
RUN git clone https://github.com/cloudgripper/cloudgripper-ros.git
RUN git clone https://github.com/KeplerC/fogros2-ls.git 
COPY ./fogros_camp ./fogros_camp
RUN cd fogros2-ls && git pull 


# generate crypto 
WORKDIR /fog_ws/src/fogros_camp/configs
RUN ./generate_crypto.sh

WORKDIR /fog_ws 
RUN . /opt/ros/humble/setup.sh && colcon build 
RUN . ./install/setup.sh &&  cargo build --release --manifest-path ./src/fogros2-ls/Cargo.toml

ENV CLOUDGRIPPER_API_KEY=DQmR5EwuT4275TaXGT8yb9Eq942aILk5


# RUN ls /fog_ws/install/../src/rt-fogros2/target/release/gdp-router
CMD . ./install/setup.sh && ros2 run sgc_launch sgc_router --ros-args -p config_file_name:=service-client.yaml -p whoami:=service_server -p release_mode:=True