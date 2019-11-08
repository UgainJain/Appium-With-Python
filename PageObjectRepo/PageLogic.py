from Base import Drivers
from selenium.common.exceptions import NoSuchElementException
from Common import common


def getAnimationBtn():
    try:
        return Drivers.driver.find_element_by_xpath(common.CommonUtils.readfromjson("Animation","LocatorsTestCase1"))
    except NoSuchElementException:
        print("Animation Btn not Located")
        return None

def getHideShowBtn():
    try:
        return Drivers.driver.find_element_by_xpath(common.CommonUtils.readfromjson("Hide/show","LocatorsTestCase1"))
    except NoSuchElementException:
        print("HideShow Btn not Located")
        return None

def getHideBtn():
    try:
        return Drivers.driver.find_element_by_id(common.CommonUtils.readfromjson("HideBtn","LocatorsTestCase1"))
    except NoSuchElementException:
        print("Hide Btn not Located")
        return None

def get0Btn():
    try:
        return Drivers.driver.find_element_by_xpath(common.CommonUtils.readfromjson("0","LocatorsTestCase1"))
    except NoSuchElementException:
        print("0 Btn not Located")
        return None

def get1Btn():
    try:
        return Drivers.driver.find_element_by_xpath(common.CommonUtils.readfromjson("1","LocatorsTestCase1"))
    except NoSuchElementException:
        print("1 Btn not Located")
        return None

def get2Btn():
    try:
        return Drivers.driver.find_element_by_xpath(common.CommonUtils.readfromjson("2","LocatorsTestCase1"))
    except NoSuchElementException:
        print("2 Btn not Located")
        return None

def get3Btn():
    try:
        return Drivers.driver.find_element_by_xpath(common.CommonUtils.readfromjson("3","LocatorsTestCase1"))
    except NoSuchElementException:
        print("3 Btn not Located")
        return None


def getShowBtn():
    try:
        return Drivers.driver.find_element_by_id(common.CommonUtils.readfromjson("ShowBtn","LocatorsTestCase1"))
    except NoSuchElementException:
        print("Show Btn not Located")
        return None


def getAppBtn():
    try:
        return Drivers.driver.find_element_by_xpath(common.CommonUtils.readfromjson("App","LocatorsTestCase2"))
    except NoSuchElementException:
        print("App Btn not Located")
        return None

def getActionBarBtn():
    try:
        return Drivers.driver.find_element_by_xpath(common.CommonUtils.readfromjson("ActionBar","LocatorsTestCase2"))
    except NoSuchElementException:
        print("Action Bar Btn not Located")
        return None

def getDisplayOptionBtn():
    try:
        return Drivers.driver.find_element_by_xpath(common.CommonUtils.readfromjson("Displayopt","LocatorsTestCase2"))
    except NoSuchElementException:
        print("Display Option Btn not Located")
        return None

def getShowTtlBtn():
    try:
        return Drivers.driver.find_element_by_id(common.CommonUtils.readfromjson("ShowTtlBtn","LocatorsTestCase2"))
    except NoSuchElementException:
        print("Show Title Btn not Located")
        return None

def getTitle():
    try:
        return  Drivers.driver.find_element_by_xpath(common.CommonUtils.readfromjson("Title","LocatorsTestCase2"))
    except NoSuchElementException:
        return None
