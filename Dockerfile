# 1. Install Ubuntu
FROM        ubuntu:18.04
MAINTAINER  hyeon95y@gmail.com
RUN         apt-get -y update

# 2. Install pip3, Jupyter, unzip, kaggle
RUN         apt-get -y install python3-pip
RUN         apt-get -y install unzip
RUN         apt-get -y install git
RUN         apt-get -y install screen
RUN         apt-get -y install htop
RUN         pip3 install kaggle
RUN         pip3 install jupyterlab
RUN         pip3 install jupyter

# 3. Install Packages for Data Science
RUN         pip3 install numpy
RUN         pip3 install pandas
RUN         pip3 install pandas_datareader
RUN         pip3 install statsmodels
RUN         pip3 install sklearn
RUN         pip3 install matplotlib
RUN         pip3 install seaborn
RUN         pip3 install GPyOpt

# 4. Install Packages (CPU Build)
RUN         pip3 install xgboost
RUN         pip3 install catboost
RUN         pip3 install lightgbm
RUN         pip3 install torch==1.2.0+cpu torchvision==0.4.0+cpu -f https://download.pytorch.org/whl/torch_stable.html

# 5. Install Packages (GPU Build)

# 6. Copy Source
COPY . /usr/src/kubig
