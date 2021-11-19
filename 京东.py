from selenium import webdriver
import time


#创建浏览器
driver = webdriver.Chrome()

#最大化
driver.maximize_window()

#打开网址
driver.get("https://www.jd.com/")


driver.find_element_by_xpath("//*[@id = 'key']").send_keys("手套")

driver.find_element_by_xpath("//*[@class='button']").click()

driver.find_element_by_xpath("//*[@data-sku='100012387864']").click()

driver.switch_to_window(driver.window_handles[1])

driver.find_element_by_xpath("//*[@id = 'InitCartUrl']").click()








