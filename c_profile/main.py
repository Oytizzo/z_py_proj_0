import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


options = Options()
# options = webdriver.ChromeOptions()

# options.add_argument(r"user-data-dir=C:\Users\User\AppData\Local\Google\Chrome\User Data\Profile 11")

# options.add_argument(r"--user-data-dir=C:\path\to\chrome\user\data") #e.g. C:\Users\You\AppData\Local\Google\Chrome\User Data
options.add_argument(r"user-data-dir=C:\Users\User\AppData\Local\Google\Chrome\User Data")

# options.add_argument(r'--profile-directory=YourProfileDir') #e.g. Profile 3
options.add_argument(r"--profile-directory=Profile 11")

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
# driver = webdriver.Chrome(executable_path=r'C:\path\to\chromedriver.exe', chrome_options=options)
driver.get("https://www.google.com")

driver.get("https://facebook.com")
time.sleep(15)
print("waited for 15 secs now exiting")
