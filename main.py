"""
    import 那这个是什么语句呢
    其实啊这个语句就是用来导入第三方库的或者是本的py文件
    并且啊导入库的话也有三种写法。也就是下面的这几种
    1. import 库名
    2. form 库名 import 类/函数/变量
    3. import 库名 as 别名 （之后呢我们也可以用as语句来给这个库取个别名）
    之后呢我们就可以使用库名或者是别名来访问这个库里面的一些函数和变量和类
"""

import requests # 导入http库
import re # 导入正则表达式库
import json # 导入json库
import datetime # 导入时间库
import csv # 导入csv库
import os # 导入系统库

# 导入Qt库
from PyQt6.QtCore import QRect,QSize,Qt # 导入Qt基础库
from PyQt6.QtWidgets import QWidget,QApplication,QPushButton,QFileDialog,QTextEdit,QComboBox,QVBoxLayout,QHBoxLayout,QLabel,QMessageBox # 导入一些常用的Qt类

# 窗口类
class Widget(QWidget):
    def __init__(self,parent = None):
        super().__init__(parent) # 调用基类无参构造函数
        self.setupUi() # 初始化ui

    # 初始化ui
    def setupUi(self):
        # 初始化窗口
        self.setWindowTitle("爬虫小程序")
        self.setGeometry(QRect(100,100,900,500))
        self.setFixedSize(QSize(900,400))

         # 实例化垂直布局对象
        self.qHBoxLayout1 = QHBoxLayout()
        self.qHBoxLayout2 = QHBoxLayout()
        self.qHBoxLayout3 = QHBoxLayout()

        # 实例化水平布局对象
        self.qVBoxLayout = QVBoxLayout()

        # 实例化标签
        self.qLabel1 = QLabel()
        self.qLabel1.setText("请选择平台:")

        # 实例化标签
        self.qLabel2 = QLabel()
        self.qLabel2.setText("请输入url:")

        # 实例化标签
        self.qLabel3 = QLabel()
        self.qLabel3.setText("请选择目录:")
        

        # 实例化下拉框控件
        self.qComboBox = QComboBox(self)
        self.qComboBox.addItems([
            "快手视频",
            "B站视频",
            "豆瓣电影（仅排行榜）",
            "网易云音乐"
        ])
        self.qComboBox.setFixedSize(700,38)
        self.qComboBox.activated.connect(self.on_activated)

        # 实例化行编辑框控件
        self.qTextEdit1 = QTextEdit(self)
        self.qTextEdit1.setFixedSize(700,38)
        self.qTextEdit1.setPlaceholderText("请输入视频的url地址")

        # 实例化行编辑框控件
        self.qTextEdit2 = QTextEdit(self)
        self.qTextEdit2.setReadOnly(True)
        self.qTextEdit2.setFixedSize(597,38)
        self.qTextEdit2.setPlaceholderText("请选择文件的保存位置")

        # 实例化按钮控件
        self.pPushButton1 = QPushButton(self)
        self.pPushButton1.setText("打开文件夹")
        self.pPushButton1.setFixedSize(100,38)
        self.pPushButton1.clicked.connect(self.on_clicked)

        # 实例化按钮控件
        self.pPushButton2 = QPushButton(self)
        self.pPushButton2.setText("START")
        self.pPushButton2.setFixedSize(350,60)
        self.pPushButton2.setStyleSheet("" \
        "QPushButton{" \
        "background-color: rgba(124, 156, 255,1);" \
        "font-size: 30px;" \
        "color: white;" \
        "border: 1px white solid;" \
        "}" \
        "QPushButton:hover{" \
        "background-color: rgba(124, 156, 255,0.5);" \
        "}" \
        "QPushButton:pressed{" \
        "background-color: rgba(124, 156, 255,1);" \
        "}")
        self.pPushButton2.clicked.connect(self.on_clicked1)

        # 设置布局
        self.qHBoxLayout1.addWidget(self.qLabel1)
        self.qHBoxLayout1.addWidget(self.qComboBox)
        self.qHBoxLayout1.setSpacing(3)

        # 设置布局
        self.qHBoxLayout2.addWidget(self.qLabel2)
        self.qHBoxLayout2.addWidget(self.qTextEdit1)
        self.qHBoxLayout2.setSpacing(3)

        # 设置布局
        self.qHBoxLayout3.addWidget(self.qLabel3)
        self.qHBoxLayout3.addWidget(self.qTextEdit2)
        self.qHBoxLayout3.addWidget(self.pPushButton1)
        self.qHBoxLayout3.setSpacing(3)

        # 设置布局
        self.qVBoxLayout.addLayout(self.qHBoxLayout1)
        self.qVBoxLayout.addLayout(self.qHBoxLayout2)
        self.qVBoxLayout.addLayout(self.qHBoxLayout3)
        self.qVBoxLayout.addWidget(self.pPushButton2,alignment = Qt.AlignmentFlag.AlignCenter)
        self.qVBoxLayout.setSpacing(20)

        # 设置布局
        self.setLayout(self.qVBoxLayout)
        
    def on_clicked(self):
        FileDir = QFileDialog.getExistingDirectory(self,"选择文件夹")
        self.qTextEdit2.setText(FileDir)

    def on_clicked1(self):
        Platform = self.qComboBox.currentText()
        Url = self.qTextEdit1.toPlainText()
        Dir = self.qTextEdit2.toPlainText()
        if (Dir == "" and (Platform != "豆瓣电影（仅排行榜）" and Url == "")) or (Platform == "豆瓣电影（仅排行榜）" and Dir == ""):
            QMessageBox.information(self,"错误","目录和url不能为空")
        else:
            if Platform == "快手视频":
                Kuaishou_Video(Url,Dir)
                QMessageBox.information(self,"消息",f"文件以保存到{Dir}目录")
            elif Platform == "B站视频":
                Bilibili_Video(Url,Dir)
                QMessageBox.information(self,"消息",f"文件以保存到{Dir}目录")
            elif Platform == "豆瓣电影（仅排行榜）":
                Douban_Ranking(Dir)
                QMessageBox.information(self,"消息",f"文件以保存到{Dir}目录")
            elif Platform == "网易云音乐":
                QMessageBox.information(self,"消息",f"暂未开放此平台")
    def on_activated(self):
        if self.qComboBox.currentText() == "豆瓣电影（仅排行榜）":
            self.qTextEdit1.setText("")
            self.qTextEdit1.setEnabled(False)
        else:
            self.qTextEdit1.setEnabled(True)

num = 0 # 用户选择的菜单选项
filename = "" # 文件名

"""配置请求头"""
head = {
    # 那这个是什么头呢，其实啊这个头的作用就是用来维护登录状态，会话的保持，个性化推荐和反爬虫机制，也就是说他还用这个反爬虫机制来验证请求的合法性
    "cookie" : "kpf=PC_WEB; clientid=3; did=web_fa9f0387cc1909c63e25cc1409f946f3; kwpsecproductname=kuaishou-vision; kwpsecproductname=kuaishou-vision; ktrace-context=1|MS44Nzg0NzI0NTc4Nzk2ODY5LjI0ODE4NTIzLjE3NjIxNTQzMjUxODAuMjcxMTYyOTEz|MS44Nzg0NzI0NTc4Nzk2ODY5Ljk4OTk5MzY0LjE3NjIxNTQzMjUxODAuMjcxMTYyOTE0|0|webservice-user-growth-node|webservice|true|src-Js; kpn=KUAISHOU_VISION; kwssectoken=YDwjq+fiA1HZUWc8p9q5/j6wQ+nX0B5jYrq+p6pjs5pG5rAiPMgzrtY3pDNPketW/eMGSrPAktkAJATIYaO8Sw==; kwscode=1dc1737b22e8c2004d63385ab54d1899dcef8852af36206501063e713e9d2d6c; kwssectoken=jaNcNZUHtEUoBpW6Xu7wa2SWLZD6QXY5DunQxTYCgfxscho5mlHenISoa0Q13Da/vlbqzaK4jGD60gGsoxq21g==; kwscode=354b5936cfd5c804230b90d77cc8c055f465a21f420b2a616f6e96fcf718f5a0; kwfv1=PnGU+9+Y8008S+nH0U+0mjPf8fP08f+98f+nLlwnrIP9+Sw/ZFGfzY+eGlGf+f+e4SGfbYP0QfGnLFwBLU80mYG9P7GAGE+ASDwemj+/QYwBHE8nr7GAWl80z0GfLh+/mYG/H78frMw/4S8eQSwn+0PnGEPeDh+npj+fLh+/DIw/PI+9HhGnpDG/4jw/8Dw/PIwBpY+BQfP0LAPfHh+9GEGc==",

    # 客户端头，用来伪造成浏览器来给服务器发送Get请求
    "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36"
}

""" 获取时间和日期的 """
def GetTime():
    # 使用datetime库里面的datetime类里面的now方法来获取当前的时间和日期，并且啊这个now这个方法他的返回值是datetime类对象，之后呢在通过这个对象的strftime方法来将时间和日期格式化成字符串 """
    return datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

""" 打印菜单 """
def PutMenu():
    print("=" * 4," 欢迎进入到爬虫小程序 ","=" * 4)
    print("1. 快手视频")
    print("2. B站视频")
    print("3. 豆瓣电影（仅排行版）")
    print("4. 酷狗音乐")
    print("5. 退出")
    print("=" * 30)

""" 函数：用户发送get请求的 """
def GetHttp(url : str,head : str):
    """ 调用requests库的get方法来向服务器发起get请求，并设置请求头,之后呢服务器就会返回一个http响应，也就是对应到在Python中Response这个类的对象，也就是说他还返回一个Response对象，之后如果我们要获取http响应里面的字符串的话那就通过这个类的text属性就可以获取到了，如果我们要获取Json数据的话那就通过这个类的json这个属性就可以获取到，如果我们要获取二进制数据的话我们就可以通过这个类的content这个属性就可以获取到了 """
    response = requests.get(url = url,headers = head)
    return response

""" 函数：处理快手这个平台的视频的爬取 """
def Kuaishou_Video(Url :str,Dir :str):
    # 获取时间和日期，并将这个作为视频文件的文件名
    filename = GetTime()

    # 获取用户输入的视频的url地址
    # url = input("请输入视频的url地址：")

    # 向服务器发起get请求
    response = GetHttp(Url,head)

    # 解析数据，并获取怎么视频的标题和视频的播放量和视频的爱心的数量，还有视频的真实的链接
    JsonList = re.findall("\"livingId\":null,\"iconType\":0\}\},\"__typename\":\"VisionVideoDetailAuthor\"\},\"VisionVideoDetailPhoto:.*?\":(.*),\"\$VisionVideoDetailPhoto",response.text)
    JsonStr = JsonList[0]
    # with open(f"{Dir}/KG.html","w",encoding = "utf-8") as file:
    #     file.write(response.text)
    # with open(f"{Dir}/KG.json","w",encoding = "utf-8") as file:
    #     file.write(JsonStr)
    jsonDataDict = json.loads(JsonStr)
    # VideoJson = jsonDataDict["VisionVideoDetailPhoto:3xaxtmmgv6gy2fg"]
    # VisionVideoDetailPhoto:3xhy2tz63eskvr2
    # print(VideoJson)

    # 获取视频的标题
    title = jsonDataDict["caption"]

    # 获取视频的爱心量
    likeCount = jsonDataDict["likeCount"]

    # 获取视频的播放量
    viewCount = jsonDataDict["viewCount"]
    
    # 获取这个视频的真实链接
    Url = jsonDataDict["photoUrl"]

    print(f"标题：{title}")
    print(f"爱心：{likeCount}")
    print(f"播放量：{viewCount}")
    print(f"链接：{Url}")

    # 获取视频
    with open(f"{Dir}/{filename}.mp4","wb") as file:
        response = GetHttp(Url,head)
        file.write(response.content)

    """ 通过Python内置的函数，也就是用于文件操作的函数，也就是这个open函数，并且啊这个函数他的返回值是一个用户这个文件操作的文件对象之后呢我们就可以通过这个对象来对这个文件进行一些操作 """
    """ 如果这个遇到了编码的问题的话我们就要通过这个函数的encoding这个参数来设置用什么样的编码来打开这个文件 """
    # file = open("html/kuaishou.html","w",encoding = "utf-8")

    """之后呢在通过这个文件对象的write方法来将获取到的数据写入到文件里面来"""
    # file.write(response1.text)

    """  获取这个视频的网页 """
    # html = response1.text
    # print(html)

    """ 然后的话就通过正则表达式库里面的finfall这个方法，这个方法的话是查找在一个字符串中所有匹配正则表达式的所以子串，然后的话就是这个函数的返回值是一个列表"""
    # URLList = re.findall(r"\"photoUrl\":\"(.*)\",\"liked\":false,", html)
    # url = str(URLList[0])

    # """ 又因为获取的这个字符串是一个json数据，所以的话我们就可以使用json库里面的loads方法就可以将字符串类型的json数据转发成字典 """
    # # JsonStr = Strlist[0]
    # # DictDate = json.loads(JsonStr)


    # """ 之后呢我们就可以通过键值对来获取到视频的链接 """
    # # Video = DictDate["defaultClient"]["VisionVideoDetailPhoto:3xrmjt3hi8sp6i9"]["photoUrl"]
    # # print(f"DictDate: {DictDate}")

    """ 之后呢我们就可以使用正则表达式里面的sub方法，这个方法的话它可以替换所有匹配这个正则表达式的字串，去掉这个链接中的u002F """
    # Url = re.sub(r"\\u002F",r"/",url)
    # Url = url.replace("\\u002F","\\")

    # print(f"url: {Url}")

    """" 之后呢在将我们获取到的真正的视频链接打印出来 """
    # print(f"URL: {Url}")

    # response1 = GetHtpp(Url,head)
    # file2 = open(f"./video/{filename}.mp4","wb")
    # file2.write(response1.content)
    # file2.close()


    """如何呢在文件操作结束时一定要调用这个文件对象的close方法来关闭文件，不然的话你写的数据可能不会真正的保存"""
    # file.close()

""" 函数：处理哔哩哔哩这个平台的视频的爬取 """
def Bilibili_Video(Url :str,Dir :str):
    # 获取时间和日期，并将这个作为视频文件的文件名
    filename = GetTime()

    head = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'max-age=0',
        'priority': 'u=0, i',
        'referer': 'https://www.bilibili.com/?from=xpage',
        'sec-ch-ua': '"Google Chrome";v="141", "Not?A_Brand";v="8", "Chromium";v="141"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36',
        'cookie': "buvid3=71D4B25D-132C-E14F-6D9F-01A330E9FD9760082infoc; b_nut=1759545860; _uuid=714FD46A-C5A9-EE7C-5C39-43B3B5F478FE60181infoc; enable_web_push=DISABLE; buvid_fp=d7c1c034023a721f31decc605032d71d; buvid4=20CC8A0C-56E1-10BA-5B94-595E0046CD1C64196-025100410-c9KIX/dzR/rdblaq0K0xYg%3D%3D; DedeUserID=1295174516; DedeUserID__ckMd5=ae95adbdc2cb2112; theme-tip-show=SHOWED; theme-avatar-tip-show=SHOWED; theme-switch-show=SHOWED; theme_style=dark; rpdid=|(kR))Ru~~)0J'u~lmlRlm~l; CURRENT_QUALITY=80; SESSDATA=4f921c32%2C1776676099%2C61d41%2Aa1CjArn3d_oi3wMdkezsg2-3VgH8S06N8npO6Ko7kYSDFI1IqVUw50e8BNHQ2gmkump3sSVlBZbVl3WUZYVDRHdDQydndyYVNiRm9rQ1hmOTYtZkM0eUs5enc0SEh1aUFkcmtlZkJiMXBNT3BxNWtzZTV1ek9LTG1ZdXpOX09rN3JSUmI3b1pOSi1BIIEC; bili_jct=986264294f7592d22f7bafe2d647b264; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NjE0MDAzMDAsImlhdCI6MTc2MTE0MTA0MCwicGx0IjotMX0.IEYRtHu4cnUkd_WqmcaHSUKE-cwsYcLf8lug4Qyy33I; bili_ticket_expires=1761400240; home_feed_column=5; browser_resolution=2560-1321; bmg_af_switch=1; bmg_src_def_domain=i1.hdslb.com; bp_t_offset_1295174516=1127534970827440128; b_lsid=D105110878_19A197C49CE; sid=8lsk97jo; CURRENT_FNVAL=4048",
    }

    # 获取用户输入的视频的url地址
    # url = input("请输入视频的url地址：")

    # 向服务器发起get请求，并设置这个get请求的请求头
    response = GetHttp(Url,head)
    list = re.findall("<\/style><script>window\.__playinfo__=(.*?)<\/script><script>",response.text)
    AudioVedioData = json.loads(list[0])
    VideoUrl = AudioVedioData["data"]["dash"]["video"][0]["baseUrl"]
    AudioUrl = AudioVedioData["data"]["dash"]["audio"][0]["baseUrl"]
    # print(f"VideoUrl：{VideoUrl}")
    # print(f"AudioUrl：{AudioUrl}")

    # 获取视频，并将视频保存起来
    with open(f"{Dir}/1.mp4","wb") as file:
        # 向服务器发送请求来拿到真实的视频数据
        response1 = GetHttp(VideoUrl,head)
        # print(response1.content)

        # 将获取到的视频的二进制数据保存到文件中
        file.write(response1.content)

        # 获取视频，并将视频保存起来
    with open(f"{Dir}/1.mp3","wb") as file:
        # 向服务器发送请求来拿到真实的音频数据
        response1 = GetHttp(AudioUrl,head)
        # print(response1.content)

        # 将获取到的音频数据的二进制数据保存到文件中
        file.write(response1.content)

    # 使用系统库的system方法来执行cmd命令，来将视频和音频合并成一个文件
    cmdList = [f"ffmpeg -i {Dir}/1.mp4 -i {Dir}/1.mp3 -c:v copy -c:a aac -map 0:v:0 -map 1:a:0 {Dir}/{filename}.mp4",f"rm {Dir}/1.mp3 {Dir}/1.mp4"]
    for cmd in cmdList:
        os.system(cmd)

""" 函数：处理豆瓣电影排行版的爬取 """
def Douban_Ranking(Dir :str):
    head = {
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

    FilmListData = []
    file1 = open(f"{Dir}/top250.csv","w",encoding = "utf-8",newline = "")
    writer = csv.writer(file1)

    i = 1
    while i <= 10:

        # 设置豆瓣电影排行版url
        url = f"https://movie.douban.com/top250?start={(i - 1) * 25}&filter=0"
        # print(f"i: {i}")
        print(f"URL: {url}")

        # 向豆瓣服务器发送get请求，并拿到源码
        response = GetHttp(url,head)

        with open("douban.html","w",encoding = "utf-8") as file:
            file.write(response.text)

        FilmData = re.findall("<a\shref=\"(.*)\">\s*.*title\">(.*)<\/span>\s*.*\s*.*\s*.*\s*.*\s*.*\s*.*\s*.*\s*(.*)<br>\s*(.*)\s*.*\s*.*\s*.*\s*.*\s*.*\s*<span>(.*)<\/span>",response.text)

        # print(f"FilmData: {FilmData}")
        size = len(FilmData)
        print(f"size: {size}")
        for j in range(size):
            list1 = [FilmData[j][0],FilmData[j][1],re.sub("&nbsp;","",FilmData[j][2]),re.sub("&nbsp;/&nbsp;","",FilmData[j][3]),FilmData[j][4]]
            print(list1)
            FilmListData.append(list1)
            writer.writerow(list1)
        i += 1
    file.close()

""" 程序的入口 """
if __name__ == "__main__":
    qApplication = QApplication([]) # 实例化Qt应用程序对象
    widget = Widget() # 实例化一个窗口对象
    widget.show()
    exit(qApplication.exec())