import json
from pathlib import Path
import os
import time


class CommonUtils:
    def readfromjson( key,filename):
        try:
            filename = filename + ".json"
            path = Path(__file__).parent.parent
            path =os.path.join(path,"Resources\\JSON")
            os.chdir(path)
            with open(filename,'r+')as f:
                jso = json.load(f)
            return jso[key]
        except FileNotFoundError:
            print(filename + " Not found")
            return None

    def Click(Element):
        Element.click()

    def isDisplayed(Element):
        try:
            if Element != None:
                Flag = Element.is_displayed()
                if Flag == True:
                    return True
                else:
                    return False
            else:
                return False
        except Exception as e:
            print(e.message)

    def wait():
        time.sleep(1)