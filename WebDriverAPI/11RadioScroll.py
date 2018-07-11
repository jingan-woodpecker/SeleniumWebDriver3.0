from selenium import webdriver
import unittest
import traceback, time

class PageScrollByChrome(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def test_radioScroll(self):
        url = "http://www.seleniumhq.org/"
        try:
            #使用js的scrollTo函数和document.body.scrollHeight参数
            #将页面的滚动条滑动到页面最下方
            self.driver.get(url)
            self.driver.maximize_window()
            self.driver.execute_script("window.scrollTo(100, document.body.scrollHeight);")
            time.sleep(3)

            #使用JS的scrollIntoView函数操作滚动条
            #scrollIntoView(true)表示将元素滚动到屏幕中间
            #scrollIntoView(false)表示将元素滚动到屏幕底部
            self.driver.execute_script\
                ("document.getElementById('choice').scrollIntoView(true);")
            time.sleep(3)

            #使用JS的scrollBy方法，操作滚动条横纵坐标（x,y)
            self.driver.execute_script("window.scrollBy(0,400);")
            time.sleep(3)
        except Exception as e:
            #打印异常堆栈信息
            print (traceback.print_exc())

    def tearDown(self):
		#退出浏览器
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()


