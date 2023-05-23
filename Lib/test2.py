import unittest

from main import *
import unittest
from selenium import webdriver
from appium.webdriver.common.touch_action import TouchAction
class MyTestCase(unittest.TestCase):

    def test_case01(self):#登录注册模块

        driver.find_element(By.ID, "com.zmsoft.forwatch:id/btn_ok").click()
        # 利用 "swipe" 实现滑动, 屏幕从右向左滑动
        driver.swipe(width * 0.9, height * 0.5, width * 0.1, height * 0.5, 500)
        driver.swipe(width * 0.9, height * 0.5, width * 0.1, height * 0.5, 500)
        driver.swipe(width * 0.9, height * 0.5, width * 0.1, height * 0.5, 500)
        driver.swipe(width * 0.9, height * 0.5, width * 0.1, height * 0.5, 500)
        #screen = driver.get_window_size()
        #print(screen)
        #driver.swipe(width * 0.9, height * 0.5, width * 0.3, height * 0.2, 1600)
        #sleep(1)
        driver.find_element(By.ID, "com.zmsoft.forwatch:id/btn_startup").click()
        driver.find_element(By.ID, "com.zmsoft.forwatch:id/et_number").send_keys("17329943155")  # 填入用户名
        driver.find_element(By.ID, "com.zmsoft.forwatch:id/password").send_keys("124263192")  # 填入用户名+
        driver.find_element(By.ID, "com.zmsoft.forwatch:id/checkbox").click()
        driver.find_element(By.ID, "com.zmsoft.forwatch:id/btn_login").click()
        driver.find_element(By.ID, "com.zmsoft.forwatch:id/btn_right").click()
        sleep(1)

    def test_case02(self):
        #定位
        #driver.find_element(By.ID, "com.zmsoft.forwatch:id/cancel").click()
        #driver.find_element(By.ID, "com.zmsoft.forwatch:id/btn_right").click()
        #driver.find_element(By.ID, "com.zmsoft.forwatch:id/update_id_ignore").click()
        driver.find_element(By.ID, "com.zmsoft.forwatch:id/image").click()
        driver.find_element(By.ID, "com.zmsoft.forwatch:id/refresh").click()
        sleep(20)
        driver.find_element(By.ID, "com.zmsoft.forwatch:id/switch_map").click()
        driver.find_element(By.ID, "com.zmsoft.forwatch:id/iv_back").click()
    def test_case03(self):#微聊
        #定位
        sleep(20)
        TouchAction(driver).tap(x=412, y=498).perform()
        sleep(20)
        TouchAction(driver).tap(x=698, y=1073).perform()
        driver.find_element(By.ID, "com.zmsoft.forwatch:id/chat_edit_box").send_keys("123a、@")
        driver.find_element(By.ID, "com.zmsoft.forwatch:id/send_btn").click()
        sleep(3)
        driver.find_element(By.ID, "com.zmsoft.forwatch:id/chat_express").click()
        driver.find_element(By.ID, "com.zmsoft.forwatch:id/iv_face").click()
        driver.swipe(width * 0.9, height * 0.5, width * 0.1, height * 0.5, 50)

        sleep(3)


if __name__ == '__main__':
    #unittest.main()
    suite = unittest.TestSuite()
    #suite.addTest(MyTestCase("test_case00"))
    suite.addTest(MyTestCase("test_case01"))
    suite.addTest(MyTestCase("test_case02"))
    suite.addTest(MyTestCase("test_case03"))
    #suite.addTest(MyTestCase("test_case03"))
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)