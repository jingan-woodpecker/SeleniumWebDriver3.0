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
