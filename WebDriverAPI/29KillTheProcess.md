```py
from selenium import webdriver
import unittest,os

class EndProcessByChrome(unittest.TestCase):

    def setUp(self):
        #启动谷歌浏览器
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def test_killTheProcess(self):
        #结束谷歌浏览器进程
        returnCode = os.system("TASKKILL /F /IM chrome.exe")
        if returnCode == 0:
            print("结束进程成功")
        else:
            print("结束进程失败")

    def tearDown(self):
        # 退出浏览器
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
   ```
   
	代码说明：将Windows上的DOS命令的字符串类型数据作为参数值传递给Python语言的os.system(command)函数，
	然后函数执行该DOS命令，并返回执行结果，以此来结束Windows中的谷歌浏览器进程。
	
	注意：os模块调用cmd命令有两种方法：os.popen()、os.system()都是用当前进程来调用；
	其中os.system()是无法获取返回值的，当运行结束后就接着执行下面的程序，但os.popen();
	是带返回值的.
	
```py	
	import os

	ret = os.popen("ipconfig")
	print(ret.read())
```
