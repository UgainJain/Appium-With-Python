from Common import common
from PageObjectRepo import PageLogic
from Base import Drivers


def verifyShowHideTitle():
    try:
        App = PageLogic.getAppBtn()
        if common.CommonUtils.isDisplayed(App):
            common.CommonUtils.Click(App)
            ActionBar = PageLogic.getActionBarBtn()
            if common.CommonUtils.isDisplayed(ActionBar):
                common.CommonUtils.Click(ActionBar)
                DisplayOpt = PageLogic.getDisplayOptionBtn()
                if common.CommonUtils.isDisplayed(DisplayOpt):
                    common.CommonUtils.Click(DisplayOpt)
                    ShowTitle = PageLogic.getShowTtlBtn()
                    if common.CommonUtils.isDisplayed(ShowTitle):
                        common.CommonUtils.Click(PageLogic.getShowTtlBtn())
                        if not common.CommonUtils.isDisplayed(PageLogic.getTitle()):
                            common.CommonUtils.Click(PageLogic.getShowTtlBtn())
                            if common.CommonUtils.isDisplayed(PageLogic.getTitle()):
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
        else:
            return False
    except Exception as e:
        print("Exception Found " +str(e))
        return False

def exit():
    Drivers.driver.close_app()

