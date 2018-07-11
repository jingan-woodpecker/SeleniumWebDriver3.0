from selenium import webdriver
import unittest

class SwitchingWindowByChrome(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        #隐式等待
        self.driver.implicitly_wait(10)

    def test_operateWindowHandle(self):
        url = "http://www.baidu.com"
        self.driver.get(url)
        self.driver.maximize_window()
        #获取当前窗口句柄
        currentWindow = self.driver.current_window_handle
        print(currentWindow)
        #点击百度页面“登录”链接文本
        self.driver.find_element_by_link_text("登录").click()
        #点击弹窗中的“立即注册”链接文本
        self.driver.find_element_by_link_text("立即注册").click()
        #获取所有窗口的句柄
        allHandles = self.driver.window_handles
        #判断此页面不是百度首页窗口，并进入到注册窗口
        for handle in allHandles:
            if handle != currentWindow:
                self.driver.switch_to.window(handle)
                print("Registration window")
                #判断页面中存在关键字“用户名”
                assert "用户名" in self.driver.page_source, "不存在该关键字"

        #判断是百度首页并使用访问列表方式进入
        for handle in allHandles:
            if handle == currentWindow:
                self.driver.switch_to.window(allHandles[0])
                print("Current window")
                self.driver.find_element_by_id("TANGRAM__PSP_4__closeBtn").click()
                #判断页面存在关键字“新闻”
                assert "地图" in self.driver.page_source, "不存在该关键字"

    def tearDown(self):
		#退出浏览器
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()