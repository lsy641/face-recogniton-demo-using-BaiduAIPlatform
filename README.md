# face-recogniton-demo-using-BaiduAIPlatform
It is a demo imitating Unmanned supermarket ，including face detection ,face register, face searching, and voice controlling is added to improve its robustness so that users can talk to have a communication with program . 

python version：3.6

about dependence libs:

关于依赖库：




if you know how to use virtualenv, you can easily run project in a virtual environment.

如果你会使用virtualenv，你可以用virtualenv在虚拟环境下运行项目。




if you want to run in your local environment,the following libraries you must install:

如果你想在本地环境顺利运行，必须安装以下依赖库：




pillow

opencv-python

baidu-aip 

matplotlib

pydub

pyaudio(安装它之前要用brew 安装portaudio，brew怎么安装看3条)

mac上必须安装的一些工具

下载brew，只需复制以下代码在终端运行：

/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)

安装好后，用brew命令安装需要的app，如下：

brew install app名




how to use demo ：

怎么运行demo：

face-register:

人脸注册：

在当前目录下（bd-face-api）运行

python rigist.py




face-searching(authentication)

人脸搜索（认证）：

在当前目录下（bd-face-api）运行

python check.py



