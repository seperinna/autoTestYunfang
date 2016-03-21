#coding=utf-8
class Page(object):
    """
    页面基础类，用于所有页面的继承
    """
    yunfang_url='http://testcloud.qfang.com:8080/qfang-dictionary'

    def __init__(self,selenium_driver,base_url=yunfang_url,parent=None):
        self.base_url=base_url
        self.driver=selenium_driver
        self.timeout=30
        self.parent=parent
    #验证是否进入访问页面url函数
    def _open(self,url):
        url=self.base_url+url
        self.driver.get(url)
        assert self.on_page(),'Did not land on %s' %url
    #查找元素函数
    def find_element(self,*loc):
        return self.driver.find_element(*loc)

    def find_elements(self,*loc):
        return self.driver.find_elements(*loc)

    def open(self):
        self._open(self.url)

    def on_page(self):
        return self.driver.current_url==(self.base_url+self.url)

    def script(self,src):
        return self.driver.excute_script(src)

    def switch_window(self):
        #获得当前窗口
        nowhandle=self.driver.current_window_handle
        #获得所有窗口
        allhandles=self.driver.window_handles
        #循环判断窗口是否为当前窗口
        for handle in allhandles:
            if handle != nowhandle:
                self.driver.switch_to_window(handle)
                print 'now welcome to yunfang main window!'


