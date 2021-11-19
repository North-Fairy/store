from  selenium import webdriver
import time


driver = webdriver.Chrome()

driver.get("https://www.suning.com/")

driver.maximize_window()

driver.find_element_by_xpath("//*[@id = 'searchKeywords']").send_keys("iphone13")

driver.find_element_by_xpath("//*[@id = 'searchSubmit']").click()

driver.find_element_by_xpath("//*[@id = '0000000000-12314319135']").click()

driver.switch_to_window(driver.window_handles[1])

driver.find_element_by_xpath("//*[@name = 'item_12314319135_gmq_buy01']").click()





