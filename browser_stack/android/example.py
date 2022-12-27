from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import time
import os

desired_caps = {
    # Set your access credentials
    # "browserstack.user": "oytizzo_OeMpca",
    # "browserstack.key": "iBCGGxGkwmC8p28wcgnV",

    # Set URL of the application under test
    "app": "bs://c700ce60cf13ae8ed97705a55b8e022f13c5827c",

    # Specify device and os_version for testing
    "platformName": "android",
    "deviceName": "Google Pixel 3",
    "platformVersion": "9.0",

    # Set other BrowserStack capabilities
    "project": "project appium 2.5.0",
    "build": "build appium 2.5.0",
    "name": "TC appium 2.5.0"
}

driver = webdriver.Remote(
    # command_executor="http://localhost:4444/wd/hub/",
    command_executor=f"http://{os.environ.get('browser_stack_user')}:{os.environ.get('browser_stack_key')}@hub-cloud.browserstack.com/wd/hub/",
    desired_capabilities=desired_caps,

)

time.sleep(3)
el = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")

el.click()

el_input = driver.find_element(AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")

el_input.click()

el_input.send_keys("Hello world")

time.sleep(3)

print("================================execution done==========================")

driver.quit()
