from  selenium import webdriver
import time
#创建浏览器
driver = webdriver.Chrome()

#访问网址
driver.get("https://www.bilibili.com/")

#最大化
driver.maximize_window()

# #检测class
try:
    driver.find_element_by_xpath("//*[@class='unlogin-avatar']").click()
except Exception:
    driver.find_element_by_xpath("//*[@class='header-login-entry']").click()

#跳转页面
driver.switch_to_window(driver.window_handles[1])

#登录账号
driver.find_element_by_xpath('//*[@id="login-username"]').send_keys("13082377710")

#登录密码
driver.find_element_by_xpath('//*[@id="login-passwd"]').send_keys("Zhaojingyao123")

#登录按钮
driver.find_element_by_xpath("//*[@class='btn btn-login']").click()

time.sleep(3)

driver.switch_to_window(driver.window_handles[1])


# #登录后
# driver.get("https://www.bilibili.com/?spm_id_from=333.794.b_696e7465726e6174696f6e616c486561646572.1")
#
# #最大化
# driver.maximize_window()
#
# #搜索
# driver.find_element_by_xpath("//*[@class = 'nav-search-keyword']").send_keys("鬼畜")
#
# #点击视频
# driver.find_element_by_xpath("//*[@title = '买 瓜 大 队']").click()
#
# #切换页面
# time.sleep(3)
# driver.switch_to_window(driver.window_handles[1])
#
# #点赞
# driver.find_element_by_xpath("//*[@class = 'van-icon-videodetails_like']").click()
#
# #退出
# driver.quit()






