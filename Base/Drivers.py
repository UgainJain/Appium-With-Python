from appium import webdriver
from Common import common
driver = None
desired_Caps = {}
def setcapability():
    desired_Caps["platformName"] = common.CommonUtils.readfromjson("PlatformName","config")
    desired_Caps["platformVersion"] = common.CommonUtils.readfromjson("PlatformVer","config")
    desired_Caps["deviceName"] = common.CommonUtils.readfromjson("DeviceName","config")
    desired_Caps["appPackage"] = common.CommonUtils.readfromjson("AppPackage","config")
    desired_Caps["appActivity"] = common.CommonUtils.readfromjson("AppMainAct","config")


def invokeDriver():
    global driver
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_Caps)
    driver.implicitly_wait(3)
