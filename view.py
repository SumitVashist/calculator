import tkinter as tk
from tkinter import ttk

class View(tk.Tk):
    Pad=7
    MAX_BUTTON_PER_ROW=4
    button_captions =[
        'C','+/-','%','/',
        7,8,9,'*',
         4, 5 ,6 ,'-',
         1,2,3,'+',
         0,'.','='
    ]

    def __init__(self,controller):
        super().__init__()
        self.controller = controller
        self.title(' Calculator  ')
        self.config(bg='black')
        self.value_var=tk.StringVar()
        self._make_main_frame()
        self._make_label()
        self._make_buttons()
        self._centre_window()

    
    def main(self):
        self.mainloop()
    
    def _make_main_frame(self):
        self.main_frame=ttk.Frame(self)
        self.main_frame.pack(padx=self.Pad,pady=self.Pad)

    def _make_label(self):
        lbl=tk.Label(
            self.main_frame,anchor='e',textvariable=self.value_var,
            state='disabled',bg='black',fg='white',font=('Arial',30))
        lbl.pack(fill='both')

    def _make_buttons(self):
        outer_frm=ttk.Frame(self.main_frame)
        outer_frm.pack()

        frm=ttk.Frame(outer_frm)
        frm.pack()
        buttons_in_row=0
    
        for caption in self.button_captions:
            if buttons_in_row==self.MAX_BUTTON_PER_ROW:
                frm=ttk.Frame(outer_frm)
                frm.pack()
                buttons_in_row=0
            btn=ttk.Button(frm,text=caption,command=(lambda button=caption : self.controller.on_button_clicked(button)),width=15)
            btn.pack(side='left')
            buttons_in_row+=1

    def _centre_window(self):
        self.update()
        width=self.winfo_width()
        height=self.winfo_height()
       
        x_offset=(self.winfo_screenwidth()-width) // 2
        y_offset=(self.winfo_screenheight()-height) // 2
        
        self.geometry(f'{width}x{height}+{x_offset}+{y_offset}')
