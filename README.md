## Install python3

Ships with Ubuntu 16.04.  Make sure it's up to date (`python3 -V` should give `Python 3.5.2` or higher)

If not:

```bash
sudo apt-get update && sudo apt-get -y upgrade
```

https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-local-programming-environment-on-windows-10

## Install pip3

```bash
sudo apt-get install -y python3-pip
```

## Useful python packages

```bash
sudo apt-get install -y --fix-missing \
    build-essential \
    cmake \
    gfortran \
    git \
    wget \
    curl \
    graphicsmagick \
    libgraphicsmagick1-dev \
    libatlas-dev \
    libavcodec-dev \
    libavformat-dev \
    libffi-dev \
    libgtk2.0-dev \
    libjpeg-dev \
    liblapack-dev \
    libssl-dev \
    libswscale-dev \
    pkg-config \
    python3-dev \
    python3-numpy \
    python3-venv \
    software-properties-common \
    zip
```

## Setup Python Virtual Environments (one time)

Just create a directory to hold the virtual environments in...

```bash
mkdir ~/.python3-venvs
```

## Create virtual environment (per project)

PROJECT_NAME=face_recognition
python3 -m venv ~/.python3-venvs/${PROJECT_NAME}
mkdir -p ~/git/python3/${PROJECT_NAME}
cd ~/git/python3/${PROJECT_NAME}
git init .

## Activate environment

```bash
. ~/.python3-venvs/${PROJECT_NAME}/bin/activate
```

## Build dlib

```bash
git clone https://github.com/davisking/dlib.git ~/git/dlib
cd ~/git/dlib
python setup.py install --yes USE_AVX_INSTRUCTIONS --no DLIB_USE_CUDA
```

https://github.com/charlielito/install-dlib-python-windows

## Install Python face_recognition module

```bash
pip install face_recognition
```

## Install Python cv2 module (for video capture)

```bash
pip install opencv-python
```


## k-nearest-neighbors (KNN)

https://github.com/ageitgey/face_recognition/blob/master/examples/face_recognition_knn.py

