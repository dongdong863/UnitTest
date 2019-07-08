#打开百度，搜索糗事百科，断言，生成测试报告


class BaiduIdeTest():

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
        driver.get(self.base_url)#get方式发送一个url站点
        #元素定位，xpath_selenium_
        driver.find_element_by_id('kw').clear#通过Id去定位，并且清除搜索框里面的内容
        driver.find_element_by_id('kw').send_keys("糗事百科")#模拟键盘输入
        driver.find_element_by_id('su').click()#点击百度一下
        time.sleep(3)#时间停顿3s
        self.assertEqual('糗事百科——百度搜索',driver.title)






    def teardown(self):#资源释放工作，--一些临时用例清理等等
        self.driver.quit()

if __name__ == '__main__':#判断文件程序入口
    testsuite = unittest.TestSuite()#构造测试套件
    testsuite.addTest(BaiduIdeTest("test_baidu_ide"))#把测试用例添加进测试套件中
    fp = open('./result.html','wb')#定义测试报告存放的路径
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title='自动化测试报告',
                                            description='用例执行情况:')
    runner.run(testsuite)#运行
    fp.close()#关闭测试报告