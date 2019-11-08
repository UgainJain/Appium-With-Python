from PageObjectRepo import PageLogic
from Base import Drivers
from Common import common

# Points(Dictionary) to store the location of the element i.e. Previous and updated location after pressing ShowBtn
point_0 = None
point_1_pre = None
point_2_pre = None
point_3_pre = None
point_0_upd = None
point_1_upd = None
point_2_upd = None
point_3_upd = None

def check_for_hiding_feature():
    Animation = PageLogic.getAnimationBtn()   # Getting
    if common.CommonUtils.isDisplayed(Animation):
        common.CommonUtils.Click(Animation)
        HideShowBtn = PageLogic.getHideShowBtn()
        if common.CommonUtils.isDisplayed(HideShowBtn):
            common.CommonUtils.Click(HideShowBtn)
            Hide = PageLogic.getHideBtn()
            if common.CommonUtils.isDisplayed(Hide):
                common.CommonUtils.Click(Hide)
                global point_0
                point_0 = PageLogic.get0Btn().location
                global point_1_pre
                point_1_pre = PageLogic.get1Btn().location
                global point_2_pre
                point_2_pre = PageLogic.get2Btn().location
                global point_3_pre
                point_3_pre = PageLogic.get3Btn().location
                common.CommonUtils.Click(PageLogic.get0Btn())
                common.CommonUtils.wait()
                Btn1 = PageLogic.get1Btn()
                point_1 = Btn1.location
                common.CommonUtils.Click(Btn1)
                common.CommonUtils.wait()
                if point_1 == point_0:
                    Btn2 = PageLogic.get2Btn()
                    point_2 = Btn2.location
                    common.CommonUtils.Click(Btn2)
                    common.CommonUtils.wait()
                    if point_2==point_0:
                        Btn3 = PageLogic.get3Btn()
                        point_3 = Btn3.location
                        common.CommonUtils.Click(Btn3)
                        common.CommonUtils.wait()
                        if point_3==point_0:
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False

def showBtns():
    try:
        ShowBtn = PageLogic.getShowBtn()
        if common.CommonUtils.isDisplayed(ShowBtn):
            common.CommonUtils.Click(ShowBtn)
            Btn0 = PageLogic.get0Btn();
            global point_0_upd
            point_0_upd = Btn0.location
            if point_0_upd==point_0:
                global point_1_upd
                point_1_upd = PageLogic.get1Btn().location
                if point_1_upd==point_1_pre:
                    global point_2_upd
                    point_2_upd = PageLogic.get2Btn().location
                    if point_2_upd==point_2_pre:
                        global point_3_upd
                        point_3_upd = PageLogic.get3Btn().location
                        if point_3_upd==point_3_pre:
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    except Exception as e:
        print(e.message)
        return False


def LaunchApp():
    Drivers.setcapability()
    Drivers.invokeDriver()
    return True


def navigateBack():
    Drivers.driver.back()
    Drivers.driver.back()
    return True













