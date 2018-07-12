```py
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import unittest, time

class OperateButtonByChrome(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        #隐式等待
        self.driver.implicitly_wait(10)

    def test_simulationCombinationKeys(self):
        url = "http://www.baidu.com"
        self.driver.get(url)
        self.driver.maximize_window()
        input = self.driver.find_element_by_id("kw")
        input.click()
        input.send_keys("自动化测试")
        ActionChains(self.driver).key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
        ActionChains(self.driver).key_down(Keys.CONTROL).send_keys('x').key_up(Keys.CONTROL).perform()
        self.driver.get(url)
        self.driver.find_element_by_id("kw").click()
        #模拟Ctrl+V组合键，将从剪贴板中获取到的内容粘贴到搜索输入框中
        ActionChains(self.driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
        time.sleep(3)
        #单击搜索按钮
        self.driver.find_element_by_id("su").click()
        time.sleep(3)
        print("测试通过")

    def tearDown(self):
        # 退出浏览器
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
  ```

	注意：
	key_down(Keys.CONTROL)表示按下Ctrl键；
	.send_keys('v')表示模拟按下 V 键；
	key_up(Keys.CONTROL).perform()表示释放Ctrl键。	
  
  
