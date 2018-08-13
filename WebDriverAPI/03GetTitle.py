from selenium import webdriver
import unittest

class GetTitleByChrome(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_getTitle(self):
        url = "http://www.baidu.com"
        self.driver.get(url)
        self.driver.maximize_window()
        #获取页面的title属性值
        title = self.driver.title
        print("当前网页的title属性值为：",title)
        #断言页面中title属性值是否是"百度一下，你就知道"
        self.assertEqual(title, "百度一下，你就知道", "页面title属性值不正确")

    def tearDown(self):
		#退出浏览器
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
    
    # 注意：断言的时候最好选择复制文本的方法，防止出错