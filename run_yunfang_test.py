#coding=utf-8
from HTMLTestRunner import HTMLTestRunner
from email.mime.text import MIMEText
from email.header import Header
import smtplib
import unittest
import time
import os

#定义发送邮件
def send_mail(file_new):
    f=open(file_new,'rb')
    mail_body=f.read()
    f.close()

    msg=MIMEText(mail_body,'html','utf-8')
    msg['Subject']=Header('云房源大数据平台自动化测试报告','utf-8')

    smtp=smtplib.SMTP()
    smtp.connect("smtp.126.com")
    smtp.login('seperinna@126.com','520167')
    smtp.sendmail('seperinna@126.com','609901782@qq.com',msg.as_string())
    smtp.quit()
    print('email has sent out!')

#查找测试报告目录，找到最新生成的测试报告文件
def new_report(testreport):
    lists=os.listdir(testreport)
    list.sort(key=lambda fn: os.path.getmtime(testreport+"\\"+fn))
    file_new=os.path.join(testreport,lists[-1])
    print(file_new)
    return file_new

if __name__=='__main__':
    now=time.strftime('%Y-%m-%d %H_%M_%S')
    filename='./yunfang/report/'+ now +' result.html'
    fp=open(filename,'wb')
    runner=HTMLTestRunner(stream=fp,title='云房源大数据平台自动化测试报告',
                          description='环境：windows 7 浏览器：firefox')
    discover=unittest.defaultTestLoader.discover('./yunfang/test_case',pattern='*_sta.py')
    runner.run(discover)
    fp.close() #关闭新生成的报告
    file_path=new_report('./yunfang/report/') #查找新生成的报告
    send_mail(file_path)  #调用发邮件模块

