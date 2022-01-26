'''
Model:logic 
View:User Sees 
Controller:controller behaviour of view
'''
from model import Model
from view import View

class Controller():

    def __init__(self):
        self.view = View(self)
        self.model=Model()

    def main(self):
        self.view.main()

    def on_button_clicked(self,caption):
        #print(f'Button {caption} Clicked')
        result=self.model.calculate(caption)
        self.view.value_var.set(result)

if __name__ == "__main__":
    app=Controller()
    app.main() 