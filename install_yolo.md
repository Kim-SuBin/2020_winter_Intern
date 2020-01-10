# Install Yolo

- install python

- install opencv
https://webnautes.tistory.com/1030

- Install git
  ~~~
  sudo apt install git
  ~~~

- Install darknet
  ~~~
  git clone https://github.com/pjreddie/darknet
  cd darknet
  make
  ~~~

- already install yolo config file. install yolo weight file
  ~~~
  wget https://pjreddie.com/media/files/yolov3.weights
  ~~~

- run darknet
  ~~~
  ./darknet detect cfg/yolov3.cfg yolov3.weights data/dog.jpg
  ~~~
