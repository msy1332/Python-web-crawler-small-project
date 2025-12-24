# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtCore import QTimer,QThread,Slot,QObject,Signal
from PySide6.QtWidgets import QApplication, QWidget, QFileDialog, QMessageBox
from ui_MainWidget import Ui_MainWidget
from ui_Login import Ui_LoginWidget
import requests,pprint,sys,re,os,json,csv,threading # 导入所需的模块
# from datetime import datetime # 用于获取当前时间类导入进来

# 导入微验证多需的库(不是我写的代码是生成的)
import hashlib,random,uuid,time,datetime,struct

def getTimeStr() -> str: # 获取当前时间的字符串
    # 通过 datetime库里面的 datetime这个类的 now方法来获取存储着当前时间的日期对象，之后呢我们就通过这个日期对象的 strftime方法来将日期格式化为字符串并返回
    return datetime.datetime.now().strftime("%y%m%d%H%M%S")

# 定义网络类，来处理网络资源的请求
class http:
    def __init__(self):
        self.url = "" # 请求的url的地址
        self.head = "" # 请求头
    def setUrl(self,url : str) -> None: # 设置请求的url地址
        self.url = url
    def setHead(self,head : str) -> None: # 设置请求的请求头
        self.head= head
    def getUrl(self) -> None: # 获取请求的url地址
        return self.url
    def getHead(self) -> None: # 获取请求的请求头
        return self.head
    def Get(self): # 发送请求并返回获取请求返回的响应对象也就是 response对象返回
        try:
            return requests.get(url = self.url,headers = self.head)
        except: # 使用 except 来捕获所有异常
            #  通过sys模块的 exc_info()方法来获取异常信息，并且啊这个函数的返回值是一个元组，并且啊这个元组的的第一个元素存储着当前的异常类型，第二个元素是存储着异常对象，第三个元素的话是存储着异常的堆栈
            # 并通过 append方法来添加异常信息字符串
            error = sys.exc_info()
            print(f"Line: {"37"}\nType: {error[0]}\nerror:{error[1]}")
            return False

# 定义一个爬虫器类，来处理快手视频的爬取逻辑
class KuaishouCrawler(QObject):
    downloadSignal = Signal(bool) # 定义类属性也就是定义一个信号，用来表示文件下载成功或者是下载失败
    def __init__(self):
        super().__init__() # 初始化 QObject这个基类
        self.VideoInfo = dict() # 定义一个字典来存储视频的相关数据
        self.http = http() # 实例化一个类对象来处理网络的请求
        self.FilePath = "" # 存储视频的保存位置
        self.FileName = "" # 存储保存的视频名字

    def run(self,platformStr : str):
        if platformStr == "快手":
            if self.download() != True: # 下载视频
                self.downloadSignal.emit(False)
            else:
                self.downloadSignal.emit(True)

    def setUrl(self,url : str) -> None: # 定义一个类方法来设置要爬取的视频的url地址
        self.VideoInfo['url'] = url # 使用修改键值的方法来向用于存储视频的相关数据
        self.http.setUrl(url) # 设置请求的地址

    def getUrl(self) -> None: # 获取视频地址
        return self.VideoInfo.get('url',"")

    def setFilePath(self,FilePath : str) -> None: # 设置视频保存位置
        self.FilePath = FilePath

    def getFilePath(self) -> None: # 获取视频的保存位置
        return self.FilePath

    def setFileName(self,FileName : str) -> None: # 设置视频保存名字
        self.FileName = FileName

    def getFileName(self) -> None: # 获取视频保存名字
        return self.FileName

    def setHead(self,head : str) -> None: # 定义类方法来设置请求头
        self.http.setHead(head) # 设置请求头

    def getHead(self,head : str) -> None: # 获取请求的请求头
        return self.http.getHead()

    def GetVideoInfo(self) -> bool: # 定义类方法来获取视频的相关数据
        try:
            # 向服务器发起get请求并获取获取服务器返回的响应对象
            response = self.http.Get()
            if response == False:
                return False

            # with open("kuaishou.html","w",encoding = "utf-8") as file:
            #     file.write(response.text)

            # 解析数据，并获取怎么视频的标题和视频的播放量和视频的爱心的数量，还有视频的真实的链接
            # print(re.search("\"livingId\".*?\"__typename\":\"VisionVideoDetailAuthor\"\},\"VisionVideoDetailPhoto:.*?\":(.*),\"\$VisionVideoDetailPhoto",response.text).groups())
            jsonDataDict = json.loads(re.search(r'\"livingId\".*?\"__typename\":\"VisionVideoDetailAuthor\"\},\"VisionVideoDetailPhoto:.*?\":(.*),\"\$VisionVideoDetailPhoto',response.text).group(1))
            # jsonDataDict = ""
            print(jsonDataDict)
            print("1111111111111111111111111111111111")

            # # 获取视频的标题
            title = jsonDataDict["caption"]
            print("1")

            # # 获取视频的爱心量
            likeCount = jsonDataDict["likeCount"]
            print("2")

            # # 获取视频的播放量
            viewCount = jsonDataDict["viewCount"]
            print("3")

            # # 获取这个视频的真实链接
            Url = jsonDataDict["photoUrl"]
            print("4")

            # # 将获取的视频数据通过修改键值对的方式来向用于存储视频的相关数据的字典里面添加相关的视频数据的键
            self.VideoInfo['标题'] = title
            self.VideoInfo['爱心'] = likeCount
            self.VideoInfo['播放量'] = viewCount
            self.VideoInfo['VideoUrl'] = Url
            print("5")

            print(f"标题：{title}")
            print(f"爱心：{likeCount}")
            print(f"播放量：{viewCount}")
            print(f"链接：{Url}")
            print("6")
            return True
        except: # 使用 except 来捕获所有异常
            #  通过sys模块的 exc_info()方法来获取异常信息，并且啊这个函数的返回值是一个元组，并且啊这个元组的的第一个元素存储着当前的异常类型，第二个元素是存储着异常对象，第三个元素的话是存储着异常的堆栈
            # 并通过 append方法来添加异常信息字符串
            error = sys.exc_info()
            print(f"Line: {"126"}\nType: {error[0]}\nerror:{error[1]}")
            return False

        # except: # 使用 except 来捕获所有异常
        #     #  通过sys模块的 exc_info()方法来获取异常信息，并且啊这个函数的返回值是一个元组，并且啊这个元组的的第一个元素存储着当前的异常类型，第二个元素是存储着异常对象，第三个元素的话是存储着异常的堆栈
        #     # 并通过 append方法来添加异常信息字符串
        #     error = sys.exc_info()
        #     print(f"Line: {"273"}\nType: {error[0]}\nerror:{error[1]}")

        #     return False

    def download(self) -> bool: # 定义类方法来下载视频数据并保存到指定位置
        try:
            # 调用 GetVideoInfo方法来获取相关的视频数据并判断是否获取成功
            if self.GetVideoInfo() != True:
                return False

            self.http.setUrl(self.VideoInfo['VideoUrl']) # 通过用于存储视频的相关数据的字典的 VideoUrl这个键来获取真实的视频的下载地址，并通过 http成员变量的 setUrl方法来设置请求地址
            response = self.http.Get() # 调用 http成员变量的 Get方法来向存储视频数据的url地址里面获取视频数据，并将返回的响应对象保存在 response变量中

            # 通过 open方法来打开一个文件来存储获取的视频的二进制数据
            with open(self.FilePath + "/" + self.FileName + ".mp4","wb") as file:
                file.write(response.content)

            return True
        except: # 使用 except 来捕获所有异常
            #  通过sys模块的 exc_info()方法来获取异常信息，并且啊这个函数的返回值是一个元组，并且啊这个元组的的第一个元素存储着当前的异常类型，第二个元素是存储着异常对象，第三个元素的话是存储着异常的堆栈
            # 并通过 append方法来添加异常信息字符串
            error = sys.exc_info()
            print(f"Line: {"294"}\nType: {error[0]}\nerror:{error[1]}")
            return False

# 定义一个爬虫器类，来处理哔哩哔哩视频的爬取逻辑
class BilibiliCrawler(QObject):
    downloadSignal = Signal(bool) # 定义类属性也就是定义一个信号，用来表示文件下载成功或者是下载失败
    supportClaritySignal = Signal(bool) # 定义类属性也就是定义一个信号，用来表示是否成功获取视频的清晰度和获取失败视频清晰度
    def __init__ (self): # 定义一个默认构造函数，来初始化这个类
        super().__init__() # 初始化 QObject这个基类

        # 定义成员变量字典来存储视频的相关的数据
        self.VideoDataDict = dict()

        # 实例化一个对象用来处理网络请求
        self.http = http()

        # 定义两个成员变量来存储视频的保存位置和保存的视频名字
        self.FilePath = ""
        self.FileName = ""
        self.VideoFlag = False # 表示是否成功获取视频支持下载的清晰度
        self.Description = "" # 表示用户想下载的清晰度

    def setDescription(self,Description : str) -> None:
        self.Description = Description

    def getDescription(self) -> None:
        return self.Description

    def run(self,platformStr : str):
        if platformStr == "哔哩哔哩":
            if self.VideoFlag: # 判断是否成功获取视频支持下载的清晰度
                if self.download(self.Description) != True: # 下载视频
                    self.downloadSignal.emit(False)
                else:
                    self.downloadSignal.emit(True)

                self.VideoFlag = False
            else:
                if self.getSupportClarity() != True: # 判断是否获取成功
                    self.supportClaritySignal.emit(False)
                else:
                    self.supportClaritySignal.emit(True)

    def setFilePath(self,FilePath : str) -> None: # 设置视频保存位置
        self.FilePath = FilePath

    def getFilePath(self) -> None: # 获取视频的保存位置
        return self.FilePath

    def setFileName(self,FileName : str) -> None: # 设置视频保存名字
        self.FileName = FileName

    def getFileName(self) -> None: # 获取视频保存名字
        return self.FileName

    def getUrl(self): # 获取视频的url地址的
        return self.VideoDataDict['url']

    def setUrl(self,url : str): # 设置爬取的视频的url地址
        self.VideoDataDict['url'] = url
        self.http.setUrl(url)

    def setHead(self,head : str) -> None: # 定义类方法来设置请求头
        self.http.setHead(head) # 设置请求头

    def getHead(self,head : str) -> None: # 获取请求的请求头
        return self.http.getHead()

    def getTitle(self,Str : str): # 获取视频的标题
        try:
            with open("bilibili.html","w") as file:
                file.write(Str)
                print("保存成功")

            # 通过正则模块的search来获取第一个匹配的字符串，并且啊这个函数的返回值是一个 Match对象 之后呢在用火这个对象的 group(1) 来获取第一个匹配的组
            title = re.search(r'<title>(.*?)<\/title>',Str).group(1)

            # 在通过 self 来访问 VideoDataDict 这个成员属性，然后的话在通过更改键值的方法来增加一个存储视频标题的键
            # self.VideoDataDict['title'] = title
            self.VideoDataDict['标题'] = title


            # 在将视频标题返回
            # return title

            return True
        except: # 使用 except 来捕获所有异常
            #  通过sys模块的 exc_info()方法来获取异常信息，并且啊这个函数的返回值是一个元组，并且啊这个元组的的第一个元素存储着当前的异常类型，第二个元素是存储着异常对象，第三个元素的话是存储着异常的堆栈
            # 并通过 append方法来添加异常信息字符串
            error = sys.exc_info()
            print(f"Line: {"199"}\nType: {error[0]}\nerror:{error[1]}")

            return False

    def getFollow(self,Str : str): # 获取视频作者的关注量
        try:
            # 通过正则模块的 search方法 来第一个匹配的字符串，然后呢在通过 Match对象的 group(1)方法 来获取第一个匹配的组
            follow = re.search(r'<\/svg>\s*关注(.*?)\s*<\/span>\s* <!----><\/div><\/div><\/div><\/div><\/div>',Str).group(1)

            # 在通过修改键值的方法来增加一对用来存储视频的的作者的关注量的键值对
            # self.VideoDataDict['follow'] = follow
            self.VideoDataDict['关注量'] = follow

            # 在将获取视频的关注量返回
            # return follow

            return True
        except: # 使用 except 来捕获所有异常
            #  通过sys模块的 exc_info()方法来获取异常信息，并且啊这个函数的返回值是一个元组，并且啊这个元组的的第一个元素存储着当前的异常类型，第二个元素是存储着异常对象，第三个元素的话是存储着异常的堆栈
            # 并通过 append方法来添加异常信息字符串
            error = sys.exc_info()
            print(f"Line: {"220"}\nType: {error[0]}\nerror:{error[1]}")

            return False

    def getReleaseDate(self,Str : str): # 获取这个视频的发布日期的
        try:
            # 通过正则模块的 search方法 来第一个匹配的字符串，然后呢在通过 Match对象的 group(1)方法 来获取第一个匹配的组
            ReleaseDate = re.search(r'class="pubdate-ip-text".*?>(.*?)<',Str).group(1)

            # 在通过修改键值的方法来增加一对用来存储视频的的发布日期的键值对
            # self.VideoDataDict['ReleaseDate'] = ReleaseDate
            self.VideoDataDict['发布日期'] = ReleaseDate

            # 在将获取视频的发布日期返回
            # return ReleaseDate

            return True
        except: # 使用 except 来捕获所有异常
            #  通过sys模块的 exc_info()方法来获取异常信息，并且啊这个函数的返回值是一个元组，并且啊这个元组的的第一个元素存储着当前的异常类型，第二个元素是存储着异常对象，第三个元素的话是存储着异常的堆栈
            # 并通过 append方法来添加异常信息字符串
            error = sys.exc_info()
            print(f"Line: {"241"}\nType: {error[0]}\nerror:{error[1]}")

            return False

    def getVideoInfo(self,Str : str): # 获取视频点赞量 投币量和收藏转发量相关数据来获取视频播放量、弹幕量、点赞数、投硬币枚数、收藏人数、转发人数、视频作者、作者简介
        try:
            # 通过正则来去获取这些数据的所在的区域
            DataRegion = re.search(r'itemprop="description"\s*.*?content="([\s\S]*?)">',Str).group(1)

            # 在通过获取到的相关数据里面在通过正则来取获取视频点赞量 投币量和收藏转发量相关数据来获取视频播放量、弹幕量、点赞数、投硬币枚数、收藏人数、转发人数、视频作者、作者简介
            Data = re.search(r'视频播放量\s*(.*?)、弹幕量\s*(.*?)、点赞数\s*(.*?)、投硬币枚数\s*(.*?)、收藏人数\s*(.*?)、转发人数\s(.*?),.*视频作者(.*?),.*作者简介([\s\S]*)',DataRegion)

            # 通过修改键值的方法来取增加一些用于存储视频播放量 投币量和收藏转发量相关数据来获取视频播放量、弹幕量、点赞数、投硬币枚数、收藏人数、转发人数、视频作者、作者简介键值对，并添加 用于存储视频的相关数据 VideoDataDict成员变量字典里面
            # self.VideoDataDict['playCount'] =  Data.group(1)
            # self.VideoDataDict['barrageCount'] =  Data.group(2)
            # self.VideoDataDict['giveLike'] =  Data.group(3)
            # self.VideoDataDict['coinInsertionCount'] =  Data.group(4)
            # self.VideoDataDict['collectionNubber'] =  Data.group(5)
            # self.VideoDataDict['forwardNubber'] =  Data.group(6)
            # self.VideoDataDict['videoAuthor'] =  Data.group(7)
            # self.VideoDataDict['authorIntroduction'] =  Data.group(8)

            self.VideoDataDict['视频播放量'] =  Data.group(1)
            self.VideoDataDict['弹幕量'] =  Data.group(2)
            self.VideoDataDict['点赞数'] =  Data.group(3)
            self.VideoDataDict['投硬币枚数'] =  Data.group(4)
            self.VideoDataDict['收藏人数'] =  Data.group(5)
            self.VideoDataDict['转发人数'] =  Data.group(6)
            self.VideoDataDict['视频作者'] =  Data.group(7)
            self.VideoDataDict['作者简介'] =  Data.group(8)

            return True
        except: # 使用 except 来捕获所有异常
            #  通过sys模块的 exc_info()方法来获取异常信息，并且啊这个函数的返回值是一个元组，并且啊这个元组的的第一个元素存储着当前的异常类型，第二个元素是存储着异常对象，第三个元素的话是存储着异常的堆栈
            # 并通过 append方法来添加异常信息字符串
            error = sys.exc_info()
            # self.addError(
            #     str(AbnormalData[0]) +
            #     str(AbnormalData[1])
            # )
            print(f"Line: {"281"}\nType: {error[0]}\nerror:{error[1]}")

            return False

    def getVideoJson(self,Str : str): # 获取视频的下载链接的所在的json数据
        try:
            # 通过正则模块来获取视频的json数据，并且啊这个函数的返回值是一个 Match对象，然后的话就是通过 Match对象的 gorup(1)方法来获取第一个匹配组
            VideoJson = re.search(r'window\.__playinfo__=(.*?)</script><script>',Str).group(1)

            # 在通过 json模块的 loads方法来将字符串类型的json数据转化成键值对形式的json数据
            VideoJsonDict = json.loads(VideoJson)

            # 通过修改键值的方法来添加用于存储着视频下载链接的json数据的键值对
            self.VideoDataDict['VideoJsonDict'] = VideoJsonDict

            return True
        except: # 使用 except 来捕获所有异常
            #  通过sys模块的 exc_info()方法来获取异常信息，并且啊这个函数的返回值是一个元组，并且啊这个元组的的第一个元素存储着当前的异常类型，第二个元素是存储着异常对象，第三个元素的话是存储着异常的堆栈
            # 并通过 append方法来添加异常信息字符串
            error = sys.exc_info()
            print(f"Line: {"300"}\nType: {error[0]}\nerror:{error[1]}")

            return False

    def parsrHTML(self,Str : str): # 解析B站视频html网页
        # 获取视频标题
        if self.getTitle(Str) != True:
            return False

        # 获取视频作者的关注量
        if self.getFollow(Str) != True:
            return False

        # 获取视频的发布日期
        if self.getReleaseDate(Str) != True:
            return False

        # 获取视频播放量、弹幕量、点赞数、投硬币枚数、收藏人数、转发人数、视频作者、作者简介
        if self.getVideoInfo(Str) != True:
            return False

        # 获取视频json数据
        if self.getVideoJson(Str) != True:
            return False

        return True

    def getSupportClarity(self): # 获取这个视频支持下载的清晰度对应的视频数据
        try:
            # 获取当前这个视频的网页源码
            response = self.http.Get()
            if response == False:
                return False
            # print(response.text)

            # 解析网页源码
            if self.parsrHTML(response.text) != True:
                # self.addError("解析网页源码失败")
                return False

            # 获取所有清晰度的视频数据和获取视频的音频数据
            VideoData = self.VideoDataDict['VideoJsonDict']['data']['dash']['video']
            AudioData = self.VideoDataDict['VideoJsonDict']['data']['dash']['audio']

            # 将视频数据和视频的音频数据老通过修改键值对的方法来向用于 存储视频数据的字典添加这个数据
            # self.VideoDataDict['videoData'] = VideoData
            # self.VideoDataDict['audioData'] = AudioData

            self.VideoDataDict['视频数据'] = VideoData
            self.VideoDataDict['音频数据'] = AudioData

            # 获取这个视频支持选择的清晰度和对应清晰度的id和获取这个视频支持选择多少种的清晰度
            Description = self.VideoDataDict['VideoJsonDict']['data']['accept_description']
            DescriptionID = self.VideoDataDict['VideoJsonDict']['data']['accept_quality']
            DescriptionLen = len(Description)

            # 将支持选择的清晰度ID对应的清晰度转化成一个字典
            DescriptionDict = dict() # 存储转化后的数据

            for i in range(DescriptionLen):
                DescriptionDict[DescriptionID[i]] = Description[i]

            # 定义一个列表用来存储对应清晰度的索引
            DescriptionIndexDict = dict()
            for i in range(DescriptionLen):
                DescriptionIndexDict[DescriptionID[i]] = -1


            # 判断视频真正支持下载的清晰度的视频数据并将支持下载的清晰度对应的视频链接存储在一个列表中并添加到用于存储视频数据的字典里面
            DescriptionSet = set() # 视频真正所支持下载的清晰度
            DescriptionIDSet = set() # 视频真正所支持下载的清晰度ID

            for i in range(len(VideoData)):
                if DescriptionDict.get(VideoData[i]['id']) != None:
                    DescriptionSet.add(DescriptionDict.get(VideoData[i]['id']))
                    DescriptionIDSet.add(VideoData[i]['id'])
                    DescriptionIndexDict[VideoData[i]['id']] = i
                    # print(DescriptionDict.get(VideoData[i]['id']))

            # print("支持清晰度：" + str(DescriptionSet))
            # print("支持的清晰度索引" + str(DescriptionIndexDict))

            # 定义一个列表用来存储对应清晰度的索引
            # DescriptionIDict = dict()
            # for i in range(DescriptionLen):
                # DescriptionIDict[DescriptionID[i]] = -1

            # for i in range(len(VideoData)):
                # if DescriptionDict.get(VideoData[i]['id'] != None): # 判断这个当前清晰度的id是否在支持选择的最清晰度的列表中
                    # DescriptionSet.add(DescriptionDict.get(VideoData[i]['id']))
                    # DescriptionIDSet.add(VideoData[i]['id'])
                    # DescriptionIDict[VideoData[i]['id']] = i

            # # 在将视频支持下载的清晰度也添加到 用于存储视频数据的字典中
            self.VideoDataDict["支持的清晰度"] = DescriptionSet

            # # # 获取真正能下载的清晰度清晰度的id和清晰度和视频和视频的音频的下载链接
            DescriptionVideoDict = dict() # 存储能下载的清晰度的视频的清晰度的id和清晰度和视频和视频的音频的下载链接

            for i in DescriptionIDSet:
                DescriptionVideoDict[DescriptionDict[i]]= {
                    "DescriptionID" : i,
                    "Description" : DescriptionDict[i],
                    "VideoBaseurl" : VideoData[DescriptionIndexDict[i]]['baseUrl'],
                    "AudioBaseurl" : AudioData[0]['baseUrl']
                }

            # print("DescriptionList: " + str(DescriptionList))

            # # 在将支持下载的清晰度的对应的视频和视频的音频数据添加到 用于存储视频数据的字典里面
            # # self.VideoDataDict['DescriptionList'] = DescriptionList
            self.VideoDataDict['所有清晰度视频数据'] = DescriptionVideoDict

            return True
        except: # 使用 except 来捕获所有异常
            #  通过sys模块的 exc_info()方法来获取异常信息，并且啊这个函数的返回值是一个元组，并且啊这个元组的的第一个元素存储着当前的异常类型，第二个元素是存储着异常对象，第三个元素的话是存储着异常的堆栈
            # 并通过 append方法来添加异常信息字符串
            error = sys.exc_info()
            print(f"Line: {"651"}\nType: {error[0]}\nerror:{error[1]}")

            return False

    def download(self,Description : str): # 下载对应清晰度的视频
        try:

            # 判断要下载的这个清晰度支不支持下载
            if not(Description in self.VideoDataDict['支持的清晰度']):
                print(f"self.VideoDataDict['支持的清晰度'] : {self.VideoDataDict['支持的清晰度']}\nDescription：{Description}")
                return False

            # 使用 os模块的 environ属性，并且啊这个属性是一个存储着所有环节变量的字典，之后呢我们就可以通过这个字典来获取到临时目录路径
            tempPath = os.environ["TEMP"]

            # 获取视频的二进制数据
            self.http.setUrl(self.VideoDataDict['所有清晰度视频数据'][Description]['VideoBaseurl'])
            VideoResponse = self.http.Get()
            if VideoResponse == False:
                return False
            else:
                with open(f"{tempPath}/1.mp4","wb") as file:
                    file.write(VideoResponse.content)

            # 获取视频的音频的二进制数据
            self.http.setUrl(self.VideoDataDict['所有清晰度视频数据'][Description]['AudioBaseurl'])
            AudioResponse = self.http.Get()
            if AudioResponse == False:
                return False
            else:
                with open(f"{tempPath}/1.mp3","wb") as file:
                    file.write(AudioResponse.content)

            # 调用 cmd命令工具来将B站的视频和音频合并
            os.system(f".\\bin\\ffmpeg.exe -y -i {tempPath}/1.mp4 -i {tempPath}/1.mp3 -c:v copy -c:a aac -map 0:v:0 -map 1:a:0 {self.FilePath + "/" + self.FileName}.mp4")


            return True
        except: # 使用 except 来捕获所有异常
            #  通过sys模块的 exc_info()方法来获取异常信息，并且啊这个函数的返回值是一个元组，并且啊这个元组的的第一个元素存储着当前的异常类型，第二个元素是存储着异常对象，第三个元素的话是存储着异常的堆栈
            # 并通过 append方法来添加异常信息字符串
            error = sys.exc_info()
            print(f"Line: {"686"}\nType: {error[0]}\nerror:{error[1]}")

            return False

# 定义一个爬虫器类，来处理豆瓣电影排行榜的爬取
class DoubanCrawler(QObject):
    downloadSignal = Signal(bool) # 定义类属性也就是定义一个信号，用来表示文件下载成功或者是下载失败
    def __init__(self):
        super().__init__() # 初始化 QObject这个基类
        self.FilePath = "" # 存储爬取到的排行榜数据文件的保存位置
        self.FileName = "" # 存储爬取到的排行榜数据文件的名字
        self.http = http() # 实例化一个用于处理网络请求的类对象
        self.FilmListData = [] # 定义一个列表来存储爬取到的电影数据

    def run(self,platformStr : str) -> None:
        if platformStr == "豆瓣":
            if self.download() != True: # 下载视频
                self.downloadSignal.emit(False)
            else:
                self.downloadSignal.emit(True)
    # @Slot()
    # def networkDownload(self) -> None: # 定义槽函数来处理爬取豆瓣电影排行榜的爬取
    #     # 通过爬取豆瓣电影排行榜的这个爬虫器的 download方法就可以下载豆瓣电影排行榜
    #     if self.download()!= True:
    #         # QMessageBox.information(self.Parent,"提示","下载失败")
    #         # self.ui.logTextEdit3.append("下载失败，请重新检查网络连接是否正常！！,正常后,请重新点击下载按钮！！")
    #         self.downloadSignal.emit(False)
    #     else:
    #         # self.Time.start(10000) # 启动定时器来模拟下载进度条
    #         # self.ui.progressBar.setValue(100)
    #         # self.ui.logTextEdit3.append(f"下载成功,文件已保存在: {self.doubanCrawler.getFilePath()}/{self.doubanCrawler.getFileName()}.csv")
    #         # QMessageBox.information(self.Parent,"提示",f"下载成功,文件已保存在: {self.doubanCrawler.getFilePath()}/{self.doubanCrawler.getFileName()}.csv")
    #         self.downloadSignal.emit(True)

    # @Slot()
    # def inputDownloadSuccessfulMessage(self,parent : QWidget = None) -> None: # 打印下载成功消息

    def setFilePath(self,FilePath : str) -> None: # 设置视频保存位置
        self.FilePath = FilePath

    def getFilePath(self) -> None: # 获取视频的保存位置
        return self.FilePath

    def setFileName(self,FileName : str) -> None: # 设置视频保存名字
        self.FileName = FileName

    def getFileName(self) -> None: # 获取视频保存名字
        return self.FileName

    def setHead(self,Head : str) -> None: # 设置请求的请求头
        self.http.setHead(head = Head)

    def getHead(self) -> None: # 获取请求的请求头
        return self.http.getHead()

    def download(self): # 下载前250个电影的排行榜
        try:
            # print("1")
            with open(self.FilePath + "/" + self.FileName + ".csv","w",encoding = "utf-8",newline = "") as file:
                writer = csv.writer(file)

                # print("2")
                i = 1
                while i <= 10:

                    # 设置豆瓣电影排行版url
                    # print("3")
                    self.http.setUrl(f"https://movie.douban.com/top250?start={(i - 1) * 25}&filter=0")

                    # print("4")
                    # 向豆瓣服务器发送get请求，并拿到源码
                    response = self.http.Get()
                    if response == False:
                        return False

                    # with open("douban.html","w",encoding = "utf-8") as file:
                    #     file.write(response.text)

                    # print("5")
                    FilmData = re.findall("<a\shref=\"(.*)\">\s*.*title\">(.*)<\/span>\s*.*\s*.*\s*.*\s*.*\s*.*\s*.*\s*.*\s*(.*)<br>\s*(.*)\s*.*\s*.*\s*.*\s*.*\s*.*\s*<span>(.*)<\/span>",response.text)
                    # print(FilmData)

                    # print(f"FilmData: {FilmData}")
                    size = len(FilmData)
                    print(f"size: {size}")
                    for j in range(size):
                        print("6")
                        list1 = [FilmData[j][0],FilmData[j][1],re.sub("&nbsp;","",FilmData[j][2]),re.sub("&nbsp;/&nbsp;","",FilmData[j][3]),FilmData[j][4]]
                        print(list1)
                        self.FilmListData.append(list1)
                        writer.writerow(list1)
                    i += 1
            return True
        except: # 使用 except 来捕获所有异常
            #  通过sys模块的 exc_info()方法来获取异常信息，并且啊这个函数的返回值是一个元组，并且啊这个元组的的第一个元素存储着当前的异常类型，第二个元素是存储着异常对象，第三个元素的话是存储着异常的堆栈
            # 并通过 append方法来添加异常信息字符串
            error = sys.exc_info()
            print(f"Line: {"686"}\nType: {error[0]}\nerror:{error[1]}")

            return False


# 定义一个总的爬虫器类
class Crawler(QObject):
    DownloadTaskSignal = Signal(str) # 定义一个类属性来表示下载任务信号，俨然就是当有下载任务是就会触发此信号
    def __init__(self):
        super().__init__() # 初始化 QObject这个基类
        self.DownloadTask = False # 表示是否有下载任务
        self.Platform = "" # 表示用户下载的平台

    def setPlatform(self,Platform : str) -> None:
        self.Platform = Platform

    def getPlatform(self):
        return self.Platform

    def run(self):
        while True:
            if self.DownloadTask:
                if self.Platform == "快手":
                    self.DownloadTaskSignal.emit("快手")
                elif self.Platform == "哔哩哔哩":
                    self.DownloadTaskSignal.emit("哔哩哔哩")
                else:
                    self.DownloadTaskSignal.emit("豆瓣")
                self.DownloadTask = False

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi() # 初始化ui

        # 实例化这三个平台的爬虫器类对象
        self.kuaishouCrawler = KuaishouCrawler()
        self.bilibiliCrawler = BilibiliCrawler()
        self.doubanCrawler = DoubanCrawler()

        # 实例化一个总的爬虫器类，来管理这些爬虫器类
        self.crawler = Crawler()

        # 实例化三个平台的爬虫器的线程对象
        self.CrawlerThread = QThread()
        # self.kuaishouThread = QThread()
        # self.bilibiliThread = QThread()
        # self.doubanThread = QThread()

        # 初始化这些线程对象
        self.kuaishouCrawler.moveToThread(self.CrawlerThread)
        self.bilibiliCrawler.moveToThread(self.CrawlerThread)
        self.doubanCrawler.moveToThread(self.CrawlerThread)
        self.crawler.moveToThread(self.CrawlerThread)

        # 初始化这三个平台的爬虫器
        ## 设置快手平台的爬虫器的请求头
        self.kuaishouCrawler.setHead(
            {
                # 那这个是什么头呢，其实啊这个头的作用就是用来维护登录状态，会话的保持，个性化推荐和反爬虫机制，也就是说他还用这个反爬虫机制来验证请求的合法性
                "cookie" : "kpf=PC_WEB; clientid=3; did=web_ba2c60632dedf0935195232b7db4b2a8; kwpsecproductname=kuaishou-vision; kwpsecproductname=kuaishou-vision; kpn=KUAISHOU_VISION; kwssectoken=q5axuZyCNMVwLvYUaVyi6Wq0TGiAHLjGJVuo3Azc4MDbqxmcDJH9vSMSGGSbjVyMuItpeYUOXS7E/GGzsc/TFw==; kwscode=354b5936cfd5c804230b90d77cc8c055f465a21f420b2a616f6e96fcf718f5a0; kwfv1=PnGU+9+Y8008S+nH0U+0mjPf8fP08f+98f+nLlwnrIP9+Sw/ZFGfzY+eGlGf+f+e4SGfbYP0QfGnLFwBLU80mYGAWU8ezDGAqM+BHlPAmS8BcM8/SD+nGEP0G98nGEPePMwer7P0L7G/q98nP7G/LlwnPU+0cU+0Zh80PUPfHI8ezY8nP7P/SjwBPF8e8j+nrIw/LU8ezf+Aq7GAZ7+0HMGI=",

                # 客户端头，用来伪造成浏览器来给服务器发送Get请求
                "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36"
            }
        )

        ## 设置哔哩哔哩视频平台爬虫器的请求头
        self.bilibiliCrawler.setHead(
            {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'zh-CN,zh;q=0.9',
                'cache-control': 'no-cache',
                'pragma': 'no-cache',
                'priority': 'u=0, i',
                'referer': 'https://www.bilibili.com/',
                'sec-ch-ua': '"Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36',
                'cookie': 'buvid3=F5DB3826-EB7C-9FE3-8689-E64BC837541118896infoc; b_nut=1764416318; _uuid=2C8BE1038-2852-13108-3FF6-F42E10FE4CA7E18465infoc; buvid_fp=43bb63268f82f41ec6083c2c31e4c6f3; buvid4=23D35477-904E-F4D8-215F-CDA3CD08092B85883-025112810-8KqNphARiaWkEGV+jsOQFw%3D%3D; DedeUserID=1295174516; DedeUserID__ckMd5=ae95adbdc2cb2112; theme-tip-show=SHOWED; theme-avatar-tip-show=SHOWED; theme-switch-show=SHOWED; theme_style=dark; CURRENT_QUALITY=0; rpdid=|(u|Jk)llmRk0J\'u~YRRkuu|J; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NjYxNTYyODMsImlhdCI6MTc2NTg5NzAyMywicGx0IjotMX0.8fuPquT4hckajhgNXUm6eqS5do_HEr-36aIO8cWNeYE; bili_ticket_expires=1766156223; SESSDATA=24231f71%2C1781449084%2C6d049%2Ac1CjB0-fSW1MvED9duLKYI9xpCG7YafLS6w5Ma1yWw1su72gUGu50LCq815xsUp7rjO_MSVm5pY3V6ckVVODVBUkRVa1paQjJRZnBKU3U0a2l4VDR2RllmdmNNanZ0aElVTzI4R3dVeDZHVDRoWHVQejFyZ1NPMmFPWE5FcnlabkZkMWJLWXotT0pBIIEC; bili_jct=7c911969e384c779e146d5bc5fb83d1f; b_lsid=6CED2C73_19B31D863A7; home_feed_column=4; browser_resolution=1348-769; bmg_af_switch=1; bmg_src_def_domain=i2.hdslb.com; sid=51m4no4u; bp_t_offset_1295174516=1147741816997543936; CURRENT_FNVAL=4048'
            }
        )

        ## 设置豆瓣电影平台的爬虫器的请求头
        self.doubanCrawler.setHead(
            {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'zh-CN,zh;q=0.9',
                'cache-control': 'max-age=0',
                'priority': 'u=0, i',
                'sec-ch-ua': '"Google Chrome";v="141", "Not?A_Brand";v="8", "Chromium";v="141"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'none',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36',
                'cookie': 'bid=AjPPnn35s1k; ll="118281"; _gid=GA1.2.1077361642.1761372037; _pk_id.100001.4cf6=25909e4422a51d06.1761372043.; __utmc=30149280; __utmz=30149280.1761372043.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmc=223695111; __utmz=223695111.1761372043.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __yadk_uid=UrexyLQL0i6xqgiHcHJyIvuRh4wz3mhp; _vwo_uuid_v2=DF4EBB163C098DAC0A38656A0BBEAE5BF|a6243cd81a469555e742e3d4a1f40420; ap_v=0,6.0; __utma=30149280.8795309.1761372037.1761386545.1761399392.4; __utmb=30149280.0.10.1761399392; __utma=223695111.8795309.1761372037.1761386545.1761399392.4; __utmb=223695111.0.10.1761399392; _pk_ses.100001.4cf6=1; _ga=GA1.2.8795309.1761372037; _ga_Y4GN1R87RG=GS2.1.s1761399352$o2$g1$t1761399402$j10$l0$h0; Hm_lvt_19fc7b106453f97b6a84d64302f21a04=1761399425; Hm_lpvt_19fc7b106453f97b6a84d64302f21a04=1761399425; HMACCOUNT=28F4477526AC5B39; _ga_393BJ2KFRB=GS2.2.s1761399425$o1$g0$t1761399425$j60$l0$h0; _ga_PRH9EWN86K=GS2.2.s1761399427$o1$g0$t1761399427$j60$l0$h0',
            }
        )

        self.crawler.setPlatform("快手")

        self.FilePath = "" # 用户选择的文件夹目录
        self.FlagDescription = False

        # 初始化信号和槽`
        self.ui.NavListWidget.currentRowChanged.connect(self.currentRowChanged1)
        self.ui.platformComboBox.currentIndexChanged.connect(self.currentIndexChanged1)
        self.ui.ClarityComboBox.currentIndexChanged.connect(self.currentIndexChanged2)
        self.ui.startPushButton.clicked.connect(self.startPushButtonClick)
        self.ui.morePushButton.clicked.connect(self.onMorePushButtonClick)

        # self.kuaishouThread.started.connect(self.kuaishouCrawler.run)
        # self.bilibiliThread.started.connect(self.bilibiliCrawler.run)
        # self.doubanThread.started.connect(self.doubanCrawler.run)
        self.CrawlerThread.started.connect(self.crawler.run)

        self.kuaishouCrawler.downloadSignal.connect(self.downloadSolt)
        self.bilibiliCrawler.downloadSignal.connect(self.downloadSolt)
        self.doubanCrawler.downloadSignal.connect(self.downloadSolt)

        self.crawler.DownloadTaskSignal.connect(self.kuaishouCrawler.run)
        self.crawler.DownloadTaskSignal.connect(self.bilibiliCrawler.run)
        self.crawler.DownloadTaskSignal.connect(self.doubanCrawler.run)

        self.bilibiliCrawler.supportClaritySignal.connect(self.supportClaritySolt)

        # 启动线程
        self.CrawlerThread.start()

    def __del__(delf) -> None:
        ...

    # def runDownloadTaskSolt(self,platformStr : str) -> None:


    def supportClaritySolt(self,Flag : bool) ->None:
        if Flag:
            self.bilibiliCrawler.VideoFlag  = True
            Description = self.bilibiliCrawler.VideoDataDict['支持的清晰度']

            # 通过 QCombobox这个控件的 addItems方法来将这个视频支持的清晰度添加到选择清晰度的组合框控件中
            self.ui.ClarityComboBox.addItems(Description)
            self.bilibiliCrawler.setDescription(self.ui.ClarityComboBox.currentText())

            # 调用 用于爬取哔哩哔哩视频的这个爬虫器对象的 setDescription方法来设置用户想下载的清晰度
            self.bilibiliCrawler.setDescription(self.ui.ClarityComboBox.currentText())

            # 将获取到的视频的相关信息显示到下面的用于显示下载日志的日志显示框中
            self.ui.functionLogTextEdit2.append(f"视频标题：{self.bilibiliCrawler.VideoDataDict['标题']}")
            self.ui.functionLogTextEdit2.append(f"视频的发布日期：{self.bilibiliCrawler.VideoDataDict['发布日期']}")
            self.ui.functionLogTextEdit2.append(f"视频的关注量：{self.bilibiliCrawler.VideoDataDict['关注量']}")
            self.ui.functionLogTextEdit2.append(f"视频播放量：{self.bilibiliCrawler.VideoDataDict['视频播放量']}")
            self.ui.functionLogTextEdit2.append(f"弹幕量：{self.bilibiliCrawler.VideoDataDict['弹幕量']}")
            self.ui.functionLogTextEdit2.append(f"点赞数：{self.bilibiliCrawler.VideoDataDict['点赞数']}")
            self.ui.functionLogTextEdit2.append(f"投硬币枚数：{self.bilibiliCrawler.VideoDataDict['投硬币枚数']}")
            self.ui.functionLogTextEdit2.append(f"收藏人数：{self.bilibiliCrawler.VideoDataDict['收藏人数']}")
            self.ui.functionLogTextEdit2.append(f"转发人数：{self.bilibiliCrawler.VideoDataDict['转发人数']}")
            self.ui.functionLogTextEdit2.append(f"视频作者：{self.bilibiliCrawler.VideoDataDict['视频作者']}")
            self.ui.functionLogTextEdit2.append(f"作者简介：{self.bilibiliCrawler.VideoDataDict['作者简介']}")
            self.ui.functionLogTextEdit2.append(f"视频支持下载的清晰度：{self.bilibiliCrawler.VideoDataDict['支持的清晰度']}")
            self.ui.functionLogTextEdit2.append(f"视频的url地址：{self.bilibiliCrawler.VideoDataDict['url']}")
            self.ui.functionLogTextEdit2.append("获取成功，请选择你要下载的清晰度")
            QMessageBox.information(self,"提示","获取成功,请选择你要下载的清晰度")
            print("获取成功")
        else:
            self.bilibiliCrawler.VideoFlag  = False

    def downloadSolt(self,Flag : bool) -> None:
        # 获取用户选择的平台
        platformStr = self.ui.platformComboBox.currentText()

        if platformStr == "快手":
            if Flag: # 判断是否下载成功
                # 没有假的下载进度条
                for i in range(100):
                    for i in range(100000):
                        pass
                    self.ui.progressBar.setValue(self.ui.progressBar.value() + 1)

                self.ui.functionLogTextEdit1.append(f"爱心：{self.kuaishouCrawler.VideoInfo['爱心']}")
                self.ui.functionLogTextEdit1.append(f"播放量：{self.kuaishouCrawler.VideoInfo['播放量']}")
                self.ui.functionLogTextEdit1.append(f"原本视频的url地址：{self.kuaishouCrawler.VideoInfo['url']}")
                self.ui.functionLogTextEdit1.append(f"解析出来的视频的url地址：{self.kuaishouCrawler.VideoInfo['VideoUrl']}")
                self.ui.functionLogTextEdit1.append(f"下载成功,文件已保存在: {self.kuaishouCrawler.getFilePath()}/{self.kuaishouCrawler.getFileName()}.mp4")
                QMessageBox.information(self,"提示",f"Line: 751,下载成功,文件已保存在: {self.kuaishouCrawler.getFilePath()}/{self.kuaishouCrawler.getFileName()}.mp4")
                print("Line: 739,成功")
            else:
                self.ui.functionLogTextEdit1.append("获取失败，请重新检查输入的url地址是否正确获取是网络连接是否正常！！,正常后,请重新点击下载按钮！！")
                self.ui.functionLogTextEdit1.append("视频下载失败")
                QMessageBox.information(self,"错误","Line: 755，下载失败")
                print("Line: 750,失败")
        elif platformStr == "哔哩哔哩":
            if Flag:
                # 没有假的下载进度条
                for i in range(100):
                    for i in range(100000):
                        pass
                    self.ui.progressBar.setValue(self.ui.progressBar.value() + 1)

                self.ui.functionLogTextEdit2.append(f"下载成功,文件已保存在:  {self.bilibiliCrawler.getFilePath()}/{self.bilibiliCrawler.getFileName()}.mp4")
                QMessageBox.information(self,"提示",f"下载成功,文件已保存在: {self.bilibiliCrawler.getFilePath()}/{self.bilibiliCrawler.getFileName()}.mp4")

                # 要将哔哩哔哩这个平台下面的动态表单下面的下载视频清晰度清空
                self.ui.ClarityComboBox.clear()
            else:
                QMessageBox.information(self,"错误","下载失败")
                self.ui.functionLogTextEdit2.append("视频下载失败！！")

                # 要将哔哩哔哩这个平台下面的动态表单下面的下载视频清晰度清空
                self.ui.ClarityComboBox.clear()
        else:
            if Flag:
                # 没有假的下载进度条
                for i in range(100):
                    for i in range(100000):
                        pass
                    self.ui.progressBar.setValue(self.ui.progressBar.value() + 1)

                self.ui.functionLogTextEdit3.append(f"下载成功,文件已保存在: {self.doubanCrawler.getFilePath()}/{self.doubanCrawler.getFileName()}.csv")
                QMessageBox.information(self,"提示",f"下载成功,文件已保存在: {self.doubanCrawler.getFilePath()}/{self.doubanCrawler.getFileName()}.csv")
            else:
                QMessageBox.information(self,"提示","下载失败")
                self.ui.functionLogTextEdit3.append("下载失败，请重新检查网络连接是否正常！！,正常后,请重新点击下载按钮！！")

        self.crawler.DownloadTask = False

        self.ui.platformComboBox.setEnabled(True)
        self.ui.ClarityComboBox.setEnabled(True)
        self.ui.videoLineEdit1.setEnabled(True)
        self.ui.videoLineEdit2.setEnabled(True)
        self.ui.startPushButton.setEnabled(True)
        self.ui.morePushButton.setEnabled(True)
        print("11111111111111111111111111111111111111111111111111111111")

    def setupUi(self) -> None:
        self.ui = Ui_MainWidget() # 实例化一个我们设计的窗口类对象
        self.ui.setupUi(self) # 调用窗口类的 setupUi方法来初始化ui
        self.ui.NavListWidget.setCurrentRow(0) # 设置窗口左侧的导航栏菜单的默认选择菜单
        self.ui.mainStackedWidget.setCurrentIndex(0) # 设置窗口右侧的堆叠控件的默认显示的子界面
        self.ui.platformComboBox.setCurrentIndex(0) # 设置选择平台的组合框控件默认选择的项目
        self.ui.formStackedWidget.setCurrentIndex(0) # 设置动态表单默认显示的表单界面
        self.ui.progressBar.setValue(0) # 初始化进度条

    def currentRowChanged1(self,currentRow) -> None:
        # 通过 QStackedWidget控件的类对象的 setCurrentIndex方法来切换到对应菜单的子页面
        self.ui.mainStackedWidget.setCurrentIndex(currentRow)

    def currentIndexChanged1(self,index) -> None:
        # print("index：" + str(index))
        # 通过 QStackedWidget控件的类对象的 setCurrentIndex方法来切换到对应的动态表单
        self.ui.formStackedWidget.setCurrentIndex(index)
        self.crawler.setPlatform(self.ui.platformComboBox.currentText())

        # 重新初始化动态表单
        ## 初始化快手这个平台下面的动态表单
        self.ui.videoLineEdit1.clear()
        self.ui.functionLogTextEdit1.clear()

        ## 初始化哔哩哔哩这个平台下面的动态表单
        self.ui.videoLineEdit2.clear()
        self.ui.ClarityComboBox.clear()
        self.ui.functionLogTextEdit2.clear()

        ## 初始化豆瓣这个平台下面的动态表单
        self.ui.functionLogTextEdit3.clear()

        # 初始化下载进度条
        self.ui.progressBar.setValue(0)

    def currentIndexChanged2(self,index) -> None:
        self.bilibiliCrawler.setDescription(self.ui.ClarityComboBox.currentText())

    def startPushButtonClick(self) -> None:
        # 初始化下载进度条
        self.ui.progressBar.setValue(0)

        # 获取用户选择的平台
        platformStr = self.ui.platformComboBox.currentText()

        # 判断用户是否选择了保存位置
        if self.FilePath == "":
            QMessageBox.information(self,"提示","请选择文件夹")
        else:
            if platformStr == "快手": # 判断用户选择的平台是不是快手，如果是的话就进入到爬取快手平台的视频的处理逻辑
                # 获取用户输入的视频的url地址
                url = self.ui.videoLineEdit1.text()

                # 判断用户是否输入了视频的url地址，如果用户没有输入的额话就弹出一个消息提示框，如何用户输入的话就通过爬取快手视频的这个爬虫器来将这个视频爬取下来并保存到指定位置
                if url == "":
                    QMessageBox.information(self,"提示","请输入视频的url地址")
                    self.ui.functionLogTextEdit1.append("请输入视频的url地址")
                else:

                    # 通过爬取快手视频的这个爬虫器的 setUrl方法来设置要爬取的视频
                    self.kuaishouCrawler.setUrl(url)

                    # 通过这个爬虫器的 setFilePath方法和 setFileName方法来设置我觉得额保存位置和保存的文件名
                    self.kuaishouCrawler.setFilePath(self.FilePath)
                    self.kuaishouCrawler.setFileName(getTimeStr())

                    # 更新标记
                    # self.kuaishouCrawler.DownloadTask = True
                    self.crawler.DownloadTask = True

                    # 添加日志
                    self.ui.functionLogTextEdit1.append("正在下载.....")
                    self.ui.platformComboBox.setEnabled(False)
                    self.ui.videoLineEdit1.setEnabled(False)
                    self.ui.startPushButton.setEnabled(False)
                    self.ui.morePushButton.setEnabled(False)

            elif platformStr == "哔哩哔哩": # 判断用户选择的平台是不是哔哩哔哩，如果是那就进入到爬取哔哩哔哩平台的视频的处理逻辑
                # 获取用户输入的视频的url地址
                url = self.ui.videoLineEdit2.text()
                # 判断用户输入的url地址是否为空
                if url == "":
                    QMessageBox.information(self,"提示","请输入视频的url地址")
                else:
                    # 通过爬取哔哩哔哩视频的这个爬虫器的 setUrl方法来设置要爬取的视频
                    self.bilibiliCrawler.setUrl(url)
                    # 通过这个爬虫器的 setFilePath方法和 setFileName方法来设置我觉得额保存位置和保存的文件名
                    self.bilibiliCrawler.setFilePath(self.FilePath)
                    self.bilibiliCrawler.setFileName(getTimeStr())

                    if self.bilibiliCrawler.VideoFlag != True:
                        self.ui.functionLogTextEdit2.append("正在获取视频支持下载的清晰度及视频的相关信息...")
                    else:
                        self.ui.functionLogTextEdit2.append("正在下载....")
                        self.ui.platformComboBox.setEnabled(False)
                        self.ui.ClarityComboBox.setEnabled(False)
                        self.ui.videoLineEdit2.setEnabled(False)
                        self.ui.startPushButton.setEnabled(False)
                        self.ui.morePushButton.setEnabled(False)

                    # 更新标记
                    # self.doubanCrawler.DownloadTask = True
                    self.crawler.DownloadTask = True

            else: # 如果用户选择的不是快手和哔哩哔哩的话就进入到爬取豆瓣电影排行榜这个平台的处理逻辑
                # 通过这个爬虫器的 setFilePath方法和 setFileName方法来设置我觉得额保存位置和保存的文件名
                self.doubanCrawler.setFilePath(self.FilePath)
                self.doubanCrawler.setFileName("豆瓣电影排行榜")

                self.ui.functionLogTextEdit3.append("正在下载...")

                # 更新标记
                # self.doubanCrawler.DownloadTask = True
                self.crawler.DownloadTask = True

                self.ui.platformComboBox.setEnabled(False)
                self.ui.startPushButton.setEnabled(False)
                self.ui.morePushButton.setEnabled(False)

    def onMorePushButtonClick(self) -> None:
        # 通过 QFileDialog类的 getExistingDirectory静态方法来弹出选择文件夹的选择框，并且啊 getExistingDirectory方法返回的就是用户选择的文件夹，如果用户没有选择文件夹的话就返回一个空的字符串
        self.FilePath = QFileDialog.getExistingDirectory(self,"选择文件夹")
        self.ui.fileLineEdit.setText(self.FilePath)


class LoginWidget(QWidget):
    def __init__(self,parent = None):
        super().__init__(parent)
        self.setupUi() # 初始化ui
        self.Key = "" # 存储用户输入的密钥
        self.WEIURL = "http://wy.llua.cn/v2/"
        self.currentVersion = "3.0" #当前版本，用于检查更新
        self.window = Widget() # 实例化窗口类对象
        # 初始化信号和槽
        self.ui.loginPushButton.clicked.connect(self.loginClicked)

    def setupUi(self): # 初始化ui
        self.ui = Ui_LoginWidget() # 实例化一个我们通过ui设计师界面设计的窗口类对象
        self.ui.setupUi(self) # 初始化ui
    def loginClicked(self):
        self.Key = self.ui.keyLineEdit.text() # 来获取当前用户输入的密钥
        print(f"key: {self.Key}")
        print("\n")
        print("\n")
        te02855f5c31d32b228a89d4a0a6b2be4 = self.Key
        f8bcf60fd4d46227c628aa2bc648515e0 = self.get_device_id()
        c4b9d0acbab128d81dd48ce1d31d898d6 = int(time.time())
        qd40200d3f1e647d59d28ab920328aaad = random.randint(100000, 999999)
        nf934dc39e1e2a2ce47388c453f532723 = self.v0934358e3fdb59d81517ba7c0cdd647b("kami=" + te02855f5c31d32b228a89d4a0a6b2be4 + "&markcode=" + f8bcf60fd4d46227c628aa2bc648515e0 + "&t=" + str(c4b9d0acbab128d81dd48ce1d31d898d6) + "&p1f01235dc00997f3fca1b8")
        r90be8041c7eef78a96c4b81441db8d02 = requests.post(self.WEIURL + "543ebab21c7c7265e25002a331ec744e",self.g142e45e32797c1ad51be14b778d0c19b(self.u1bddec7bff7ca9b7c7c9ffd7be69c157(self.g142e45e32797c1ad51be14b778d0c19b(self.m169a58ff81a2b2f4c0b1378d0d37e903(self.dc7d60c1a48261ed1c5a4ac563337aad2(self.u1bddec7bff7ca9b7c7c9ffd7be69c157(self.g142e45e32797c1ad51be14b778d0c19b(self.m169a58ff81a2b2f4c0b1378d0d37e903(self.dc7d60c1a48261ed1c5a4ac563337aad2("id=B4qgMxE0S2d&kami=" + te02855f5c31d32b228a89d4a0a6b2be4 + "&markcode=" + f8bcf60fd4d46227c628aa2bc648515e0 + "&t=" + str(c4b9d0acbab128d81dd48ce1d31d898d6) + "&sign=" + nf934dc39e1e2a2ce47388c453f532723 + "&value=" + str(qd40200d3f1e647d59d28ab920328aaad) +""),"v37866858a23385237abf945a22")),"ihSPMbUG/kDcmWK51dleQjanA0Tfq26y7vJYt+LxsZOXwRp4H9C8I3zgVBoFruEN")),"de541e9bbf0ae9babe5a31b")),"3uOlNXZFnvtjSmAJWRrL0qKhxVBfCYz+7yPbG98sa4Me1Hc5EwUQk/6TDiI2pogd")))
        if r90be8041c7eef78a96c4b81441db8d02.status_code == 200:
            u7cb6eb27df4a8cec2e8fef36383ea7a2 = json.loads(self.pba8bf0298e82598e96574620bd3861cb(self.j1731d4f0efc97ca1c2319cf5a024b1d9(self.q0d746f8e6955ecf9af7cb94287881b1a(self.q0d746f8e6955ecf9af7cb94287881b1a(self.g4c63cd147c11cafb7468f58696a77a83(self.g4c63cd147c11cafb7468f58696a77a83(self.pba8bf0298e82598e96574620bd3861cb(self.j1731d4f0efc97ca1c2319cf5a024b1d9(r90be8041c7eef78a96c4b81441db8d02.text),"l9d46086281d70d2fa86b76492816a48e451bc7"),"xt/iDmdBn9VOhPpbZXKFfuUACrY72kgH0w51eMSoqTyIW8zQRavjL6clsN+3GJE4"),"E8Z1WtvyRlUq7M03aGJPcOL6KFomrwfIHNehAjCD+k4zTYQbBXspxin5S9uV2d/g")))),"s376ae87c90d81221bb3479ecaec8cd"))
            if u7cb6eb27df4a8cec2e8fef36383ea7a2["xa790e86a909ab7a82aa122d2437ed17c"]==83830 and u7cb6eb27df4a8cec2e8fef36383ea7a2["p7927ae6c208f493597b4d8010d17f881"]["w0cf085fae3fdfa57a551f93292f2d6fd"]=="1ebfcfa6b706b5beacc378d155c299cf":
                if u7cb6eb27df4a8cec2e8fef36383ea7a2["nd24058201fd279b48888502eb53faf82"]-c4b9d0acbab128d81dd48ce1d31d898d6>30 or u7cb6eb27df4a8cec2e8fef36383ea7a2["nd24058201fd279b48888502eb53faf82"]-c4b9d0acbab128d81dd48ce1d31d898d6<-30:
                    print("设备时间不准")
                    QMessageBox.information(self,"错误","设备时间不准")
                    sys.exit()
                else:
                    if u7cb6eb27df4a8cec2e8fef36383ea7a2["p7927ae6c208f493597b4d8010d17f881"]["t271b27a22e0f3611"] != self.u97175417f4909295ea98cdbc4fa99df5(self.v0934358e3fdb59d81517ba7c0cdd647b(self.pb708254367a7ef59438e57fbb6a94d4f(""+str(c4b9d0acbab128d81dd48ce1d31d898d6)+""+nf934dc39e1e2a2ce47388c453f532723+""+str(c4b9d0acbab128d81dd48ce1d31d898d6)+""))) or u7cb6eb27df4a8cec2e8fef36383ea7a2["p7927ae6c208f493597b4d8010d17f881"]["vb655d5bee4"] != self.pb708254367a7ef59438e57fbb6a94d4f(self.u97175417f4909295ea98cdbc4fa99df5(""+nf934dc39e1e2a2ce47388c453f532723+""+str(qd40200d3f1e647d59d28ab920328aaad)+""+"p1f01235dc00997f3fca1b8"+""+str(u7cb6eb27df4a8cec2e8fef36383ea7a2["xa790e86a909ab7a82aa122d2437ed17c"])+"")) or u7cb6eb27df4a8cec2e8fef36383ea7a2["p7927ae6c208f493597b4d8010d17f881"]["v9b649048"] != self.v0934358e3fdb59d81517ba7c0cdd647b(self.u97175417f4909295ea98cdbc4fa99df5(""+str(u7cb6eb27df4a8cec2e8fef36383ea7a2["p7927ae6c208f493597b4d8010d17f881"]["r36b999cb83d3c506379fd741727b651e"])+""+str(u7cb6eb27df4a8cec2e8fef36383ea7a2["p7927ae6c208f493597b4d8010d17f881"]["r36b999cb83d3c506379fd741727b651e"])+""+str(u7cb6eb27df4a8cec2e8fef36383ea7a2["xa790e86a909ab7a82aa122d2437ed17c"])+"")):
                        print("校验失败")
                        QMessageBox.information(self,"错误","校验失败")
                        sys.exit()
                    else:
                        if u7cb6eb27df4a8cec2e8fef36383ea7a2["p7927ae6c208f493597b4d8010d17f881"]["t45625b2115629c98645ca4aebf33fb65"] == "single":
                            print("登录成功\n剩余登录次数:" + u7cb6eb27df4a8cec2e8fef36383ea7a2["p7927ae6c208f493597b4d8010d17f881"]["f03b32acce7db770eaba264b4fd6a5267"])
                            QMessageBox.information(self,"消息","登录成功\n剩余登录次数:" + u7cb6eb27df4a8cec2e8fef36383ea7a2["p7927ae6c208f493597b4d8010d17f881"]["f03b32acce7db770eaba264b4fd6a5267"])
                            # self.loginBool = True
                            self.hide() # 将当前这个登录窗口隐藏
                            self.window.show() # 显示窗口
                        else:
                            print("登录成功\n到期时间:" + datetime.datetime.fromtimestamp(u7cb6eb27df4a8cec2e8fef36383ea7a2["p7927ae6c208f493597b4d8010d17f881"]["bffc7c7fc7cf63ca1bb9138e74b517e49"]).strftime('%Y-%m-%d %H:%M:%S'))
                            QMessageBox.information(self,"消息","登录成功\n到期时间:" + datetime.datetime.fromtimestamp(u7cb6eb27df4a8cec2e8fef36383ea7a2["p7927ae6c208f493597b4d8010d17f881"]["bffc7c7fc7cf63ca1bb9138e74b517e49"]).strftime('%Y-%m-%d %H:%M:%S'))
                            # self.loginBool = True
                            self.hide() # 将当前这个登录窗口隐藏
                            self.window.show() # 显示窗口
            else:
                print(u7cb6eb27df4a8cec2e8fef36383ea7a2["p7927ae6c208f493597b4d8010d17f881"])
                QMessageBox.information(self,"消息",u7cb6eb27df4a8cec2e8fef36383ea7a2["p7927ae6c208f493597b4d8010d17f881"])
        else:
            print("网络异常")
            QMessageBox.information(self,"错误","网络异常")
            sys.exit()



    def update(self):
        print(self,"正在检查更新...")
        try:
            ini_data = requests.post(self.WEIURL + "543ebab21c7c7265e25002a331ec744e",self.g142e45e32797c1ad51be14b778d0c19b(self.u1bddec7bff7ca9b7c7c9ffd7be69c157(self.g142e45e32797c1ad51be14b778d0c19b(self.m169a58ff81a2b2f4c0b1378d0d37e903(self.dc7d60c1a48261ed1c5a4ac563337aad2(self.u1bddec7bff7ca9b7c7c9ffd7be69c157(self.g142e45e32797c1ad51be14b778d0c19b(self.m169a58ff81a2b2f4c0b1378d0d37e903(self.dc7d60c1a48261ed1c5a4ac563337aad2("id=5slLGHlHLhg"),"v37866858a23385237abf945a22")),"ihSPMbUG/kDcmWK51dleQjanA0Tfq26y7vJYt+LxsZOXwRp4H9C8I3zgVBoFruEN")),"de541e9bbf0ae9babe5a31b")),"3uOlNXZFnvtjSmAJWRrL0qKhxVBfCYz+7yPbG98sa4Me1Hc5EwUQk/6TDiI2pogd")))
            if ini_data.status_code == 200:
                ini_json = json.loads(self.pba8bf0298e82598e96574620bd3861cb(self.j1731d4f0efc97ca1c2319cf5a024b1d9(ini_data.text),"v5a18fbbefdbbad14ee363c46f0be28352e"))
                if ini_json["code"] == 87132:
                    if ini_json["msg"]["version"] == self.currentVersion:
                        print("已是最新版本")
                        QMessageBox.information(self,"消息","已是最新版本")
                    else:
                        print("有新版本")
                        print("当前版本:" + self.currentVersion)
                        print("最新版本:" + ini_json["msg"]["version"])
                        print("更新内容:" + ini_json["msg"]["updateshow"])
                        print("更新地址:" + ini_json["msg"]["updateurl"])
                        if ini_json["msg"]["updatemust"] == "y":
                            print("本次更新为强制更新，请更新后使用！")
                            QMessageBox.information(self,"消息",f'本次更新为强制更新，请更新后使用！更新地址为：<a href="{ini_json["msg"]["updateurl"]}">{ini_json["msg"]["updateurl"]}</a>')
                            sys.exit()
                else:
                    print(ini_json["msg"])
                    QMessageBox.information(self,"消息",ini_json["msg"])
            else:
                QMessageBox.information(self,"错误","网络异常")
                sys.exit()
        except: # 使用 except 来捕获所有异常
            #  通过sys模块的 exc_info()方法来获取异常信息，并且啊这个函数的返回值是一个元组，并且啊这个元组的的第一个元素存储着当前的异常类型，第二个元素是存储着异常对象，第三个元素的话是存储着异常的堆栈
            # 并通过 append方法来添加异常信息字符串
            error = sys.exc_info()
            print(f"Line: {"37"}\nType: {error[0]}\nerror:{error[1]}")
            QMessageBox.information(self,"错误","网络异常")
            sys.exit()
    def Notice(self):
        try:
            notice_data = requests.post(self.WEIURL + "543ebab21c7c7265e25002a331ec744e",self.g142e45e32797c1ad51be14b778d0c19b(self.u1bddec7bff7ca9b7c7c9ffd7be69c157(self.g142e45e32797c1ad51be14b778d0c19b(self.m169a58ff81a2b2f4c0b1378d0d37e903(self.dc7d60c1a48261ed1c5a4ac563337aad2(self.u1bddec7bff7ca9b7c7c9ffd7be69c157(self.g142e45e32797c1ad51be14b778d0c19b(self.m169a58ff81a2b2f4c0b1378d0d37e903(self.dc7d60c1a48261ed1c5a4ac563337aad2("id=joOAMK0B55B"),"v37866858a23385237abf945a22")),"ihSPMbUG/kDcmWK51dleQjanA0Tfq26y7vJYt+LxsZOXwRp4H9C8I3zgVBoFruEN")),"de541e9bbf0ae9babe5a31b")),"3uOlNXZFnvtjSmAJWRrL0qKhxVBfCYz+7yPbG98sa4Me1Hc5EwUQk/6TDiI2pogd")))
            if notice_data.status_code == 200:
                notice_json = json.loads(self.pba8bf0298e82598e96574620bd3861cb(self.j1731d4f0efc97ca1c2319cf5a024b1d9(notice_data.text),"v5a18fbbefdbbad14ee363c46f0be28352e"))
                if notice_json["code"] == 18932:
                    print("系统公告:")
                    notice = notice_json["msg"]["app_gg"]
                    print(notice)
                    if notice != "":
                        QMessageBox.information(self,"公告",str(notice_json["msg"]["app_gg"]))
                else:
                    print(notice_json["msg"])
                    QMessageBox.information(self,"错误",str(notice_json["msg"]))
                    sys.exit()
            else:
                print("网络异常")
                QMessageBox.information(self,"错误","网络异常")
                sys.exit()
        except: # 使用 except 来捕获所有异常
            #  通过sys模块的 exc_info()方法来获取异常信息，并且啊这个函数的返回值是一个元组，并且啊这个元组的的第一个元素存储着当前的异常类型，第二个元素是存储着异常对象，第三个元素的话是存储着异常的堆栈
            # 并通过 append方法来添加异常信息字符串
            error = sys.exc_info()
            print(f"Line: {"37"}\nType: {error[0]}\nerror:{error[1]}")
            QMessageBox.information(self,"错误","网络异常")
            sys.exit()
    def get_device_id(self,file_path=".imei"):
        if os.path.exists(file_path):
            with open(file_path, "r") as f:
                device_id = f.read().strip()
        else:
            device_id = str(uuid.uuid1())
            with open(file_path, "w") as f:
                f.write(device_id)
        return device_id
    def sha1_rotate_left(self,n, b):
        """循环左移"""
        return ((n << b) | (n >> (32 - b))) & 0xffffffff
    def sha1_pad_message(self,message):
        """对消息进行填充"""
        if isinstance(message, str):
            message = message.encode('utf-8')
        length = len(message)
        message += b'\x80'
        message += b'\x00' * ((56 - (length + 1) % 64) % 64)
        message += struct.pack('>Q', length * 8)
        return message
    def pb708254367a7ef59438e57fbb6a94d4f(self,message):
        """计算 SHA-1 哈希值"""
        # 初始化哈希值
        h0 = 0x67452301
        h1 = 0xEFCDAB89
        h2 = 0x98BADCFE
        h3 = 0x10325476
        h4 = 0xC3D2E1F0
        # 填充消息
        message = self.sha1_pad_message(message)
        # 处理消息块
        for i in range(0, len(message), 64):
            chunk = message[i:i+64]
            w = [0] * 80
            # 将块分解为16个32位字
            for j in range(16):
                w[j] = struct.unpack('>I', chunk[j*4:j*4+4])[0]
            # 扩展16个字为80个字
            for j in range(16, 80):
                w[j] = self.sha1_rotate_left(w[j-3] ^ w[j-8] ^ w[j-14] ^ w[j-16], 1)
            # 初始化工作变量
            a, b, c, d, e = h0, h1, h2, h3, h4
            # 主循环
            for j in range(80):
                if 0 <= j <= 19:
                    f = (b & c) | ((~b) & d)
                    k = 0x5A827999
                elif 20 <= j <= 39:
                    f = b ^ c ^ d
                    k = 0x6ED9EBA1
                elif 40 <= j <= 59:
                    f = (b & c) | (b & d) | (c & d)
                    k = 0x8F1BBCDC
                else:  # 60-79
                    f = b ^ c ^ d
                    k = 0xCA62C1D6
                temp = (self.sha1_rotate_left(a, 5) + f + e + k + w[j]) & 0xffffffff
                e = d
                d = c
                c = self.sha1_rotate_left(b, 30)
                b = a
                a = temp
            # 更新哈希值
            h0 = (h0 + a) & 0xffffffff
            h1 = (h1 + b) & 0xffffffff
            h2 = (h2 + c) & 0xffffffff
            h3 = (h3 + d) & 0xffffffff
            h4 = (h4 + e) & 0xffffffff
        # 生成最终哈希值
        return '%08x%08x%08x%08x%08x' % (h0, h1, h2, h3, h4)
    # ==================== SHA-256 实现 ====================
    def sha256_rotate_right(self,n, b):
        """循环右移"""
        return ((n >> b) | (n << (32 - b))) & 0xffffffff
    def sha256_pad_message(self,message):
        """对消息进行填充"""
        if isinstance(message, str):
            message = message.encode('utf-8')
        length = len(message)
        message += b'\x80'
        message += b'\x00' * ((64 - (length + 9) % 64) % 64)
        message += struct.pack('>Q', length * 8)
        return message
    def u97175417f4909295ea98cdbc4fa99df5(self,message):
        """计算 SHA-256 哈希值"""
        # 初始化哈希值（前8个质数的平方根的小数部分的前32位）
        h = [
            0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a,
            0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19
        ]
        # 初始化常数（前64个质数的立方根的小数部分的前32位）
        k = [
            0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
            0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
            0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
            0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
            0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
            0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
            0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
            0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2
        ]
        # 填充消息
        message = self.sha256_pad_message(message)
        # 处理消息块
        for i in range(0, len(message), 64):
            chunk = message[i:i+64]
            w = [0] * 64
            # 将块分解为16个32位字
            for j in range(16):
                w[j] = struct.unpack('>I', chunk[j*4:j*4+4])[0]
            # 扩展16个字为64个字
            for j in range(16, 64):
                s0 = self.sha256_rotate_right(w[j-15], 7) ^ self.sha256_rotate_right(w[j-15], 18) ^ (w[j-15] >> 3)
                s1 = self.sha256_rotate_right(w[j-2], 17) ^ self.sha256_rotate_right(w[j-2], 19) ^ (w[j-2] >> 10)
                w[j] = (w[j-16] + s0 + w[j-7] + s1) & 0xffffffff
            # 初始化工作变量
            a, b, c, d, e, f, g, h_temp = h
            # 主循环
            for j in range(64):
                S1 = self.sha256_rotate_right(e, 6) ^ self.sha256_rotate_right(e, 11) ^ self.sha256_rotate_right(e, 25)
                ch = (e & f) ^ ((~e) & g)
                temp1 = (h_temp + S1 + ch + k[j] + w[j]) & 0xffffffff
                S0 = self.sha256_rotate_right(a, 2) ^ self.sha256_rotate_right(a, 13) ^ self.sha256_rotate_right(a, 22)
                maj = (a & b) ^ (a & c) ^ (b & c)
                temp2 = (S0 + maj) & 0xffffffff
                h_temp = g
                g = f
                f = e
                e = (d + temp1) & 0xffffffff
                d = c
                c = b
                b = a
                a = (temp1 + temp2) & 0xffffffff
            # 更新哈希值
            h[0] = (h[0] + a) & 0xffffffff
            h[1] = (h[1] + b) & 0xffffffff
            h[2] = (h[2] + c) & 0xffffffff
            h[3] = (h[3] + d) & 0xffffffff
            h[4] = (h[4] + e) & 0xffffffff
            h[5] = (h[5] + f) & 0xffffffff
            h[6] = (h[6] + g) & 0xffffffff
            h[7] = (h[7] + h_temp) & 0xffffffff
        # 生成最终哈希值
        return ''.join(format(x, '08x') for x in h)
    def v0934358e3fdb59d81517ba7c0cdd647b(self,data: str) -> str:
        m = hashlib.md5()
        m.update(data.encode('utf-8'))
        return m.hexdigest()
    def pba8bf0298e82598e96574620bd3861cb(self,data, key):
        def ksa(key):
            key_len = len(key)
            schedule = list(range(256))
            j = 0
            for i in range(256):
                j = (j + schedule[i] + key[i % key_len]) % 256
                schedule[i], schedule[j] = schedule[j], schedule[i]
            return schedule
        def prga(schedule, data_len):
            i = j = 0
            stream = []
            for _ in range(data_len):
                i = (i + 1) % 256
                j = (j + schedule[i]) % 256
                schedule[i], schedule[j] = schedule[j], schedule[i]
                stream.append(schedule[(schedule[i] + schedule[j]) % 256])
            return stream
        def process(data, key):
            schedule = ksa(key)
            stream = prga(schedule, len(data))
            return bytes([d ^ s for d, s in zip(data, stream)])
        if isinstance(key, str):
            key = key.encode('utf-8')
        if isinstance(data, str):
            data = data.encode('utf-8')
        return process(data, key).decode('utf-8')
    def m169a58ff81a2b2f4c0b1378d0d37e903(self,data, key):
        def ksa(key):
            key_len = len(key)
            schedule = list(range(256))
            j = 0
            for i in range(256):
                j = (j + schedule[i] + key[i % key_len]) % 256
                schedule[i], schedule[j] = schedule[j], schedule[i]
            return schedule
        def prga(schedule, data_len):
            i = j = 0
            stream = []
            for _ in range(data_len):
                i = (i + 1) % 256
                j = (j + schedule[i]) % 256
                schedule[i], schedule[j] = schedule[j], schedule[i]
                stream.append(schedule[(schedule[i] + schedule[j]) % 256])
            return stream
        def process(data, key):
            schedule = ksa(key)
            stream = prga(schedule, len(data))
            return bytes([d ^ s for d, s in zip(data, stream)])
        if isinstance(key, str):
            key = key.encode('utf-8')
        if isinstance(data, str):
            data = data.encode('utf-8')
        return process(data, key)
    def g142e45e32797c1ad51be14b778d0c19b(self,data):
        if isinstance(data, str):
            data = data.encode('utf-8')
        elif not isinstance(data, bytes):
            raise ValueError("Input must be of type str or bytes")
        return ''.join(f'{byte:02x}' for byte in data)
    def j1731d4f0efc97ca1c2319cf5a024b1d9(self,hex_str):
        return bytes.fromhex(hex_str)
    def dc7d60c1a48261ed1c5a4ac563337aad2(self,data: str) -> str:
        base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
        byte_data = data.encode('utf-8')
        binary_data = ''.join(f'{byte:08b}' for byte in byte_data)
        base64_str = ""
        for i in range(0, len(binary_data), 6):
            chunk = binary_data[i:i+6]
            chunk = chunk.ljust(6, '0')
            index = int(chunk, 2)
            base64_str += base64_chars[index]
        while len(base64_str) % 4 != 0:
            base64_str += '='
        return base64_str
    def q0d746f8e6955ecf9af7cb94287881b1a(self,data: str) -> str:
        base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
        binary_data = ""
        data = data.rstrip('=')
        for c in data:
            index = base64_chars.index(c)
            binary_data += f'{index:06b}'
        byte_array = bytearray()
        for i in range(0, len(binary_data), 8):
            byte = binary_data[i:i+8]
            if len(byte) == 8:
                byte_array.append(int(byte, 2))
        return byte_array.decode('utf-8')
    def u1bddec7bff7ca9b7c7c9ffd7be69c157(self,data: str, base64_chars: str) -> str:
        byte_data = data.encode('utf-8')
        binary_data = ''.join(f'{byte:08b}' for byte in byte_data)
        base64_str = ""
        for i in range(0, len(binary_data), 6):
            chunk = binary_data[i:i+6]
            chunk = chunk.ljust(6, '0')
            index = int(chunk, 2)
            base64_str += base64_chars[index]
        while len(base64_str) % 4 != 0:
            base64_str += '='
        return base64_str
    def g4c63cd147c11cafb7468f58696a77a83(self,data: str, base64_chars: str) -> str:
        binary_data = ""
        data = data.rstrip('=')
        for c in data:
            index = base64_chars.index(c)
            binary_data += f'{index:06b}'
        byte_array = bytearray()
        for i in range(0, len(binary_data), 8):
            byte = binary_data[i:i+8]
            if len(byte) == 8:
                byte_array.append(int(byte, 2))
        return byte_array.decode('utf-8')


if __name__ == "__main__":
    # print(sys.stdout.encoding)
    # sys.stdout.reconfigure(encoding="utf-8") # 通过 sys模块的的 reconfigure方法来更改标准输出的文本的编码格式为 utf-8
    # print(sys.stdout.encoding)
    app = QApplication([])
    loginWidget = LoginWidget()
    loginWidget.show()
    loginWidget.Notice() # 调用函数来获取公告
    loginWidget.update() # 判断软件是否为最新版
    sys.exit(app.exec())
