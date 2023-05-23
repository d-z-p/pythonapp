#导入time模块
import time
#导入webdriver包
from selenium import webdriver
#创建Chrome实例 。
driver = webdriver.Chrome()
from selenium import webdriver


driver=webdriver.Chrome() #获取谷歌

# driver=webdriver.Ie() #获取ie


# driver.get方法将定位在给定的URL的网页，get接受url可以是任何网址，此处以百度为例
driver.get("https://www.baidu.com/")
#定位元素
   # 1、用id定位输入框对象，
#driver.find_element_by_id("kw").he("python")
   # 2、用id定位点击对象，用click()触发点击事件
#driver.find_element_by_id('su').click()
#显示源码
print(driver.page_source)
#显示响应对应的url
#print(driver.current_url)
#显示浏览器标题
#print(driver.title)
#显示浏览器名称
#print(driver.name)
#浏览器最大化
#driver.maximize_window()
# 延迟3秒
#time.sleep(3)
#前进
#driver.forward()
#后退
#driver.back()
#刷新
#driver.refresh()
#driver.save_screenshot('screen.png')

# 1根据xpath进行定位
#search_obj = driver.find_element_by_xpath("//form")
#2通过链接文本定位元素
#link = driver.find_element_by_link_text('学术').get_property('href')
#3根据元素的标签名称进行定位
#driver.find_element_by_tag_name('textarea')
#4根据元素的类名进行定位
#driver.find_element_by_class_name('s_ipt').send_keys('python')
#5根据Css元素选择器定位
#driver.find_element_by_css_selector('#form .s_ipt').send_keys('python')
#6根据元素ID 进行定位
#driver.find_element_by_id('kw').send_keys('python')
#根据元素的name值进行定位
#driver.find_element_by_name('wd').send_keys('python')

#保存截图
#driver.save_screenshot('screen.png')

#退出访问的实例网站。
driver.quit()
