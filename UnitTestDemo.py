#打开百度，搜索糗事百科，断言，生成测试报告



from selenium import webdriver#导入webdriver包
import HTMLTestRunner #生成测试报告
import unittest,time#导入单元测试框架，是时间的包

#思路：进入网址页面，在百度输入框输入内容进行搜索
'''
打开网址
如果定位这个输入框，然后进行搜索
对这个输入的文字进行一个断言的设计
是在这个UniTest单元测试框架中间的，
通过断言之后再生成一份测试报告
'''
class BaiduIdeTest():
    def setup(self):#资源准备工作
        self.driver = webdriver.Chrmoe()
        self.driver.imlicitly_wait(30)#打开网址确保节点完全加载出来，可写可不写
        self.base_url = 'https://www.baidu.com'
    def test_baidu_ide(self):#测试用例
        driver = self.driver
        driver.get(self.base_url)#ger方式发送一个url站点
        #元素定位，xpath_selenium_


        pass
    def teardown(self):#资源释放工作，--一些临时用例清理等等
        pass
        pass
