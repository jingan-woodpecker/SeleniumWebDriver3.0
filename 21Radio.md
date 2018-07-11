```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>操作单选框</title>
</head>
<body>
    <form action="">
        <input type="radio" name="film" value="Infernal">无间道<br>
        <input type="radio" name="film" value="Medicine">我不是药神<br>
        <input type="radio" name="film" value="Timeout">超时空同居<br>
    </form>
</body>
</html>
```
![单选框](./picture/Radio.png)

```py
from selenium import webdriver
import unittest, time

class RadioByChrome(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def test_operateRadioList(self):
        url = "D:\pycharm\API-Exercise\webDriverApi\Selection.html"
        self.driver.get(url)
        self.driver.maximize_window()
        #通过属性值定位“无间道”选项
        infernalRadio = self.driver.find_element_by_xpath("//input[@value='Infernal']")
        #单击“无间道”选项
        infernalRadio.click()
        #断言“无间道”选项被选中
        self.assertTrue(infernalRadio.is_selected(), "无间道单选框未被选中")
        print("无间道单选框被选中")
        if infernalRadio.is_selected():
            #如果“无间道”单选框被选中，重新选择“我不是药神”单选框
            medicineGodRadio = self.driver.find_element_by_xpath("//input[@value='Medicine']")
            medicineGodRadio.click()
            #选择“我不是药神”单选框后，断言“无间道”处于未被选中状态
            self.assertFalse(infernalRadio.is_selected())
            print("我不是药神单选框被选中")
        #查找所有name属性值为“the-film”的单选框元素对象，并存放在radioList列表中
        radioList = self.driver.find_elements_by_xpath("//input[@name='film']")
        #循环遍历列表查找到value的属性值为"Timeout"如果未被选中状态，则调用方法选中
        for radio in radioList:
            if radio.get_attribute("value") == "Timeout":
                if not radio.is_selected():
                    radio.click()
                    self.assertEqual(radio.get_attribute("value"), "Timeout")
                    print("超时空同居单选框被选中")
                    time.sleep(3)

    def tearDown(self):
        # 退出浏览器
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
 ```
	特别注意的是:
	
	查找所有name属性值为“the-film”的单选框元素对象，并存放在radioList列表中
	 radioList = self.driver.find_elements_by_xpath("//input[@name='film']")
	 其中element后面一定要添加"s"否则会报下面的错误
	 TypeError: 'WebElement' object is not iterable
	 