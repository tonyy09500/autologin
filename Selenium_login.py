# 載入Selenium相關模組
from selenium import webdriver
from selenium.webdriver.common.keys import Keys #Keys套件用於模擬鍵盤操作
from selenium.webdriver.common.by import By #By套件用於協助定位元素，讓我們可以在頁面中找到想要的操作元素
from selenium.webdriver.chrome.options import Options #chrome options為啟動chrome屬性, 可以為chrome配置一些參數
import time

#設定Chrome Driver執行檔案路徑
options=Options()
#直接指定exe檔案路徑
options.chrome_executable_path="/Users/lhtony/Desktop/Python/chromedriver" 
#可讓視窗不會自動關閉
options.add_experimental_option("detach", True) 

#建立Driver物件實體 用程式操作瀏覽器運作
driver=webdriver.Chrome(options=options)

#連線到Leetcode登入頁面
driver.get("https://leetcode.com/accounts/login/")

#輸入帳號密碼, 按下登入按鈕
#定義一個usernameInput用來抓取標籤ID #根據標籤ID搜尋
usernameInput = driver.find_element(By.ID, "id_login")
passwordInput = driver.find_element(By.ID, "id_password")
#模擬使用者輸入文字
usernameInput.send_keys("xxx") 
passwordInput.send_keys("xxx")
signinButton = driver.find_element(By.CSS_SELECTOR,  "#signin_btn")
#模擬使用者按下特定按鍵
signinButton.click()  
#等待登入完成
time.sleep(3) 
 
#連線到登入後才能取得資料的頁面, 並取得想要的資料
driver.get("https://leetcode.com/problemset/")
time.sleep(3) 
statElement = driver.find_element(By.CSS_SELECTOR, "[data-difficulty=TOTAL]") 
#根據標籤任意屬性搜尋-CSS搜尋器
print(statElement.text)
colums = statElement.text.split("\n") #抓取資料切割
print("已完成刷題資料", colums[1]) #印出資料第二筆資料
driver.close()


