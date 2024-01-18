import tkinter as tk
import math

button_config = {
    "bg":"#000000",
    "fg":"#FFFAFA",
    "font":("Consolas bold",12),
    "height": "2",
    "width": "7",
    "relief": "flat",
    "activebackground":"#000000"
}

digits = ["√","x²","C","n!","sin","cos","tan","sin-¹","cos-¹","tan-¹","DEG","RAD"]

numbers = ["1","2","3","4","5","6","7","8","9","0",".","="]

convert_deg = 1
convert_inverse_deg = 1

cnt = 0


class Calculator:
    def __init__(self, master):
        
        self.master = master
        self.displayFrame = tk.Frame(self.master)
        self.displayFrame.pack()
        self.buttonsFrame = tk.Frame(self.master)
        self.buttonsFrame.pack()
        self.output = tk.Entry(self.displayFrame, 
                               width=39, relief="flat", bd=5, font=("Consolas bold",14),fg="#FFFAFA", bg="#000000")
        self.output.grid(row=0,column=0)
        self.change = tk.Button(self.displayFrame,
                                button_config, width=3, height=0, text="DEG", bg="#0000CD",command=self.degreesRadian)
        self.change.grid(row=0,column=1)
        self.createButtons()

    def createButtons(self):
        self.buttons = [
            ["√", "x²", "**","(",")","/"],
            ["sin","cos","7","8","9","+"],
            ["sin-¹","cos-¹","4","5","6","-"],
            ["tan","tan-¹","1","2","3","*"],
            ["n!","π",".","0","=","C"]
                       ]
        

        for i in range(len(self.buttons)):
            for j in range(len(self.buttons[i])):
                text = self.buttons[i][j] 
                '''create a new button every iteration, with a different text, but same configuration
                   ->Lambda explanation: We define text = text to bind every function to correct button
                     without this, the only text it will be passed is C, that's last in the matrix,
                     so when clicking buttons, the only value that will appear on display it will be C.
                '''
                if text in numbers:
                    b = tk.Button(self.buttonsFrame,button_config,bg="#0000CD",
                    text=text, command = lambda text = text: self.buttonsAction(text)) 
                else:
                    b = tk.Button(self.buttonsFrame,button_config,text=text, command = lambda text = text: self.buttonsAction(text)) 
                b.grid(row = i, column = j)

    def buttonsAction(self, text):
        global convert_deg
        global convert_inverse_deg
        if text != "=":
            if text not in digits:
                self.output.insert('end',text)

            else:
                if text == "√":
                    self.addValue(math.sqrt(float(self.output.get())))
                elif text == "n!":
                    self.addValue(math.factorial(float(self.output.get())))
                elif text == "x²":
                    self.addValue(float(self.output.get()) ** 2)
                elif text == "C":
                    self.addValue("")
                elif text == "π":
                    self.addValue(3.1415926535897932)
                elif text == "sin":
                    self.addValue(math.sin(float(self.output.get()) * convert_deg))
                elif text == "cos":
                    self.addValue(math.cos(float(self.output.get()) * convert_deg))
                elif text == "tan":
                    self.addValue(math.tan(float(self.output.get()) * convert_deg))
                elif text == "sin-¹":
                    self.addValue(math.asin(float(self.output.get())) * convert_inverse_deg)
                elif text == "cos-¹":
                    self.addValue(math.acos(float(self.output.get())) * convert_inverse_deg)
                elif text == "tan-¹":
                    self.addValue(math.atan(float(self.output.get())) * convert_inverse_deg)
        else:
            self.addValue(eval(self.output.get()))
                    
    def addValue(self, value):
        self.output.delete(0, 'end')
        self.output.insert('end',value)

    def degreesRadian(self):
        global cnt
        global convert_deg
        global convert_inverse_deg
        
        if(cnt == 0): 
            convert_deg = math.pi / 180
            convert_inverse_deg = 180 / math.pi
            self.change['text'] = "RAD"
            cnt = 1
        else: 
            convert_deg = 1
            convert_inverse_deg = 1
            self.change['text'] = "DEG"
            cnt = 0
            
                            
root = tk.Tk()
Calculator(root)
root.mainloop()