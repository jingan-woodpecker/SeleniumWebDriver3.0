```py
from selenium.common.exceptions import WebDriverException
from selenium import webdriver
import traceback
import unittest, time

class OperateJSByChrome(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def test_setExecuteScipt(self):
        url = "http://www.baidu.com"
        self.driver.get(url)
        self.driver.maximize_window()
        #构造JS查找百度首页的搜索输入框的代码字符串
        searchInputBoxJS = "document.getElementById('kw').value='自动化';"
        #构造JS查找百度首页的搜索按钮的代码字符串
        searchButtonJS = "document.getElementById('su').click()"
        try:
            #通过JS代码在百度首页搜索输入框输入“自动化”
            self.driver.execute_script(searchInputBoxJS)
            time.sleep(2)
            #通过JS代码单击百度首页上的搜索按钮
            self.driver.execute_script(searchButtonJS)
            time.sleep(2)
            self.assertTrue("百度百科" in self.driver.page_source)
        except WebDriverException as e:
            print("页面中没有找到要操作的元素", traceback.print_exc())
        except Exception as e:
            print(traceback.print_exc())

    def tearDown(self):
        # 退出浏览器
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
 ```
 
	注意：此方法主要用于解决页面元素的.click()方法无效等问题
