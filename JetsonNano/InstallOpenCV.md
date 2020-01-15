# [Install OpenCV](https://j-remind.tistory.com/57?category=693866)

### Delete default OpenCV
~~~
$ suudo apt-get remove libopencv*
$ sudo apt-get autoremove
$ sudo find /usr/local/ -name "*opencv*" -exec rm {} \;
~~~

###  Update & Upgrade
~~~
$ sudo apt-get update
$ sudo apt-get upgrade
~~~

### Install build essential
~~~
$ sudo apt-get install libjpeg-dev libpng-dev libtiff-dev
~~~
