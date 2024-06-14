#pip install --upgrade BingImageCreator
from os import system , listdir
from PIL import Image

# C = "1X_C5aBDjtwFhrHKzgczZpt3DJM6D8dA4UJ0J7fVzK3pFDPtizKuJunDW4j0IBqcm6nUKcI7QbaaFgrPz__Bd_5agQeb4juSRxQso6ANqS0aVRNqgk6E_oxV-zEW22WJR4bPWJUlw0qqhbINpzBjDCf3vFkq7PjDU3q6Y70G4zum8oAeSOmX5bZqYUPpPHK-Bt6F9mMKVNleRVZMPLm4RrlybQDBB4rTDElQk5SYgQko"

C= open(r"keys\C","r").readline()
def Generate_Images(prompt:str):
    system(f'python -m BingImageCreator --prompt "{prompt}" -U {C}')
    return listdir("output")[-4:]

class Show_Image:
    def __init__(self,li:list) -> None:
        self.listd=li
    def open(self,no):
        try:
            img = Image.open(f"output\\{self.listd[no]}")
            img.show()
        except:
            print("Image was not good")
            self.open(no+1)
    def close(self,no):
        #TODO
        pass
    
# Generate_Images("Spiderman")

