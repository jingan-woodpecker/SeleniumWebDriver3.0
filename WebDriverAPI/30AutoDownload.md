```py
from selenium import webdriver
import unittest, time

class DownloadByChrome(unittest.TestCase):

    def setUp(self):
        #创建FirefoxProfile实例，用于存放自定义配置
        profile = webdriver.FirefoxProfile()
        #指定下载后存放文件的位置，如果指定了多级不存在的目录，将会下载到默认路径
        profile.set_preference("browser.download.dir", 'D:\\autodownload')
        #将browser.download.folderList设置为2，表示将文件下载到指定路径
        #设置成0表示下载到桌面；设置成1表示下载到默认路径
        profile.set_preference('browser.download.folderList', 2)
        #browser.helperApps.alwaysAsk.force对于未知的MIME类型文件会弹出窗口
        #让用户处理，默认值为True,设定为False表示不会记录打开未知MIME类型
        profile.set_preference("browser.helperApps.alwaysAsk.force", False)
        #在开始下载时是否显示下载管理器
        profile.set_preference('browser.download.manager.showWhenStarting', False)
        #设定为False会将下载框隐藏
        profile.set_preference("browser.download.manager.useWindow", False)
        # 默认值为True设定为False表示不获取焦点
        profile.set_preference('browser.download.manager.focusWhenStarting', False)
        #下载.exe文件弹出警告，默认值是True,设定为False则不会弹出警告框
        profile.set_preference("browser.download.manager.alertOnEXEOpen", False)
        #browser.helperApps.neverAsk.openFile表示直接打开下载文件，不显示确认框，默认值为空字符串，
        #下行代码设定了多种文件的MIME类型，例如application/exe,表示.exe类型的文件，
        #application/excel表示Excel类型文件
        profile.set_preference("browser.helperApps.neverAsk.openFile", "application/pdf")
        #对所给出的文件类型不再弹出提示框进行询问，直接保存到本地磁盘
        profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'application/zip, application/octet-stream')
        #browser.download.manager.showAlertOnComplete设定下载文件结束后是否显示下载完成提示框，
        # 默认为True,设定为False表示下载完成后不显示下载完成提示框
        profile.set_preference("browser.download.manager.showAlertOnComplete", False)
        #browser.download.manager.closeWhenDone设定下载结束后是否自动关闭
        #下载框，默认值为True,设定为False表示不关闭下载管理器
        profile.set_preference("browser.download.manager.closeWhenDone", False)
        #启动火狐浏览器时，通过firefox_profile参数将自动配置添加到FirefoxProfile对象中
        self.driver = webdriver.Firefox(executable_path=r"D:\pycharm\geckodriver.exe", firefox_profile = profile)
    def test_dataPicker(self):
        url = "https://github.com/mozilla/geckodriver/releases"
        self.driver.get(url)
        self.driver.maximize_window()
        #选择下载zip文件，使用application/zip指代此类型文件
        self.driver.find_element_by_xpath("//strong[.='geckodriver-v0.21.0-win64.zip']").click()
        time.sleep(10)

    def tearDown(self):
        # 退出浏览器
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
   ```
	注意：通过profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'application/zip, application/octet-stream')
	这种方式添加需要屏蔽下载询问弹出的文件类型，如果要同时添加多种文件类型，文件类型间用逗号隔开，例如上面的
	'application/zip, application/octet-stream'
