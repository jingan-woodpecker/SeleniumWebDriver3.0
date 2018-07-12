```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>操作复选框</title>
</head>
<body>
    <form action="">
        <input type="checkbox" name="film" value="Infernal">无间道<br>
        <input type="checkbox" name="film" value="Medicine">我不是药神<br>
        <input type="checkbox" name="film" value="Timeout">超时空同居<br>
    </form>
</body>
</html>
```

![复选框](./picture/checkBox.png)

```py
from selenium import webdriver
import unittest, time

class CheckManyBoxByChrome(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        #隐式等待
        self.driver.implicitly_wait(10)

    def test_operateCheckBox(self):
        url = "D:\pycharm\API-Exercise\webDriverApi\Selection.html"
        self.driver.get(url)
        self.driver.maximize_window()
        #通过属性值定位“无间道”选项
        infernalRadio = self.driver.find_element_by_xpath("//input[@value='Infernal']")
        #单击“无间道”选项
        infernalRadio.click()
        #断言“无间道”选项被选中
        self.assertTrue(infernalRadio.is_selected(), "无间道复选框未被选中")
        time.sleep(2)
        if infernalRadio.is_selected():
            #如果“无间道”复选框被选中，再次单击取消选中
            infernalRadio.click()
            #断言“无间道”复选框处于未选择状态
            self.assertFalse(infernalRadio.is_selected())
            time.sleep(2)
        #查找所有name属性值为“film”的复选框元素对象，并存放在checkBoxList列表中
        checkBoxList = self.driver.find_elements_by_xpath("//input[@name='film']")
        #循环遍历列表所有复选框，让全部复选框被选中
        for check in checkBoxList:
            if not check.is_selected():
                check.click()
                time.sleep(3)
        print("测试通过")

    def tearDown(self):
        # 退出浏览器
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
  ```
	注意：断言复选框处于未选择状态的方法self.assertFalse()
