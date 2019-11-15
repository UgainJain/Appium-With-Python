from BusinessLogic import ApiDemosBLHideShowBtns
from BusinessLogic import APiDemosBLTitleVerification
import pytest

@pytest.mark.first
def test_LaunchApp():
    assert ApiDemosBLHideShowBtns.LaunchApp() == True


@pytest.mark.second
def test_verify_hiding_btns():
    assert ApiDemosBLHideShowBtns.check_for_hiding_feature() == True



@pytest.mark.third
def test_verify_show_btns():
    assert ApiDemosBLHideShowBtns.showBtns() == True


@pytest.mark.fourth
def test_navigate_back_to_main_menu():
    assert ApiDemosBLHideShowBtns.navigateBack() == True


@pytest.mark.fifth
def test_verify_working_of_show_title():
    assert APiDemosBLTitleVerification.verifyShowHideTitle() == True

@pytest.mark.last
def test_close():
    APiDemosBLTitleVerification.exit()