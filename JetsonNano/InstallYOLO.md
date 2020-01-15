# [Install YOLO](https://j-remind.tistory.com/60?category=693866)

### Install Darknet
~~~
$ git clone https://github.com/pjreddie/darknet
~~~
- Change Makefile
~~~
$ cd darknet
$ sudo vi Makefile
~~~
![ChangeMakefile](https://t1.daumcdn.net/cfile/tistory/99839C405C4C614C27)
- Compile
  ~~~
  $ make
  ~~~
### Download trained files from YOLO Darknet.
~~~
$ wget https://pjreddie.com/media/files/yolov3.weights
~~~

### Run image example
~~~
$ ./darknet detect cfg/yolov3.cfg yolov3.weights data/dog.jpg
~~~
![RunImageExample](https://t1.daumcdn.net/cfile/tistory/9990124F5C4AC6CE16)
