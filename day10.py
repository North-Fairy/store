

class WaterCup:
    __high = 0.0      #高度
    __volume = 0      #容积
    __color = ""      #颜色
    __texture = ""    #材质

    #高度
    def setHigh(self,high):
        if high > 50 or high < 5:
            print("你确定这个高度是个水杯吗？")
        else:
            self.__high = high
    def getHigh(self):
        return self.__high

    #容积
    def setVolume(self,volume):
        if volume > 3000:
            print("你确定是水杯不是水桶？")
        elif volume < 0:
            print("请拿真实的水杯来测")
        else:
            self.__volume = volume
    def getVolume(self):
        return self.__volume

    #颜色
    def setColor(self,color):
        self.__color = color
    def getColor(self):
        return self.__color

    #材质
    def setTexture(self,texture):
        self.__texture = texture
    def getTexture(self):
        return self.__texture

    #功能
    def water(self,num):
        if num > self.__volume:
            print("你水倒多了吧")
        else:
            print("容积为", self.__volume, "ml 的", self.__color, self.__texture, "水杯放了", num, "ml 水")


wc = WaterCup()

wc.setHigh(int(input("请输入水杯的高度，单位是厘米：")))
wc.setVolume(int(input("请输入水杯的容量，单位是毫升：")))
wc.setColor(input("请输入水杯的颜色："))
wc.setTexture(input("请输入水杯的材质："))


wc.water(int(input("你要倒多少水，单位是毫升：")))






class Notebook:
#屏幕
    __screen = 0
#价格
    __Price = 0
#cpu型号
    __model = ""
#内存
    __Memory = ""
#待机
    __Standby = ""

    def setScreen(self,screen):
        if screen <= 17 and screen >=10:
            self.__screen = screen
        else:
            print("你的电脑还真少见")
    def getScreen(self):
        return self.__screen


    def setModel(self,model):
        self.__model = model
    def getModel(self):
        return self.__model


    def setPrice(self,price):
        if price < 0:
            print("你的电脑是大风刮来的啊")
        elif price > 10000:
            print("你的电脑好贵啊")
            self.__Price = price
        else:
            self.__Price = price

    def getPrice(self):
        return self.__Price


    def setMemory(self,memory):
        if memory == "16G" or memory == "8G" or memory == "12G":
            self.__Memory = memory
        else:
            print("你的电脑过时了")
    def getMemory(self):
        return self.__Memory


    def setStandby(self,standby):
        self.__Standby = standby
    def getStandby(self):
        return self.__Standby


#打字
    def Typing(self,typing):
        if typing > 0:
            print("您一共打了",typing,"个字")
        else:
            print("请输入正确的数值")

#打游戏
    def PlayGames(self,Gamename,hour):
        if hour > 0:
            print("你玩",Gamename,"玩了",hour,"小时")

#看视频
    def Videos(self,Videosname,hour):
        if hour > 0:
            print("你看",Videosname,"看了", hour, "小时")




nb = Notebook()



nb.setStandby(input("请输入你的待机时长："))
nb.setMemory(input("请输入你的内存大小："))
nb.setPrice(int(input("请输入你电脑的价格：")))
nb.setModel(input("请输入你的CPU型号："))
nb.setScreen(int(input("请输入你的屏幕大小,单位是英寸：")))


nb.Typing(123)
nb.PlayGames("绝地求生",3)
nb.Videos("小猪佩奇",3)































