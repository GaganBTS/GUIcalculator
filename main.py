from tkinter import *
from tkinter import messagebox





# ----------- brain_of_calculator ------------- #
def write(num):
    if num != "=":
       expression_text.insert(END,num)
    else:
        result()
def result():
    exp = expression_text.get()
    try:
      result = eval(exp)
    except:
        messagebox.showerror(title="INVALID INPUT",message="Please enter valid expression excluding characters like "
                                                           "alphabets,=,brackets etc.")
    else:

     expression_text.delete(0,END)
     expression_text.insert(0,result)
def clear():
    expression_text.delete(0,END)



# ----------------------------- UI_SETUP ------------------------ #
window = Tk()
window.title("CALCULATOR")
window.config(padx=40,pady=40,bg="#0A1931")

# ----entry---- #
expression_text = Entry(font=("Comic Sans MS",14,"normal"))
expression_text.grid(row=0,column=0,columnspan=6,ipadx=110,pady=10)
expression_text.focus()

# ----- buttons ----- #
button_prop = {
    "fg":"#7C83FD",
    "bg":"white",
    "width":6,
    "height":1,
    "highlightthickness":0,
    "font": ("Comic Sans MS",17,"bold"),

}
# ---------properties of buttons as a dictionary to be passed as kwargs later------- #
button9 = Button(window,text="9",**button_prop,command=lambda:write(9))
button9.grid(column=0,row=1,pady=4)
button8 = Button(window,text="8",**button_prop,command=lambda:write(8))
button8.grid(column=1,row=1)
button7 = Button(window,text="7",**button_prop,command=lambda:write(7))
button7.grid(column=2,row=1)
buttonplus = Button(window,text="+",**button_prop,command=lambda:write("+"))
buttonplus.grid(column=3,row=1)
button6 = Button(window,text="6",**button_prop,command=lambda:write(6))
button6.grid(column=0,row=2,pady=4)
button5 = Button(window,text="5",**button_prop,command=lambda:write(5))
button5.grid(column=1,row=2)
button4 = Button(window,text="4",**button_prop,command=lambda:write(4))
button4.grid(column=2,row=2)
buttonminus = Button(window,text="-",**button_prop,command=lambda:write("-"))
buttonminus.grid(column=3,row=2)
button3 = Button(window,text="3",**button_prop,command=lambda:write(3))
button3.grid(column=0,row=3,pady=4)
button2 = Button(window,text="2",**button_prop,command=lambda:write(2))
button2.grid(column=1,row=3)
button1 = Button(window,text="1",**button_prop,command=lambda:write(1))
button1.grid(column=2,row=3)
buttonmultiply = Button(window,text="*",**button_prop,command=lambda:write("*"))
buttonmultiply.grid(column=3,row=3)
button0 = Button(window,text="0",**button_prop,command=lambda:write(0))
button0.grid(column=0,row=4,pady=4)
buttonmodulo = Button(window,text="%",**button_prop,command=lambda:write('%'))
buttonmodulo.grid(column=1,row=4)
buttondivide = Button(window,text="/",**button_prop,command=lambda:write("/"))
buttondivide.grid(column=2,row=4)
buttonresult = Button(window,text="=",**button_prop,command=lambda:write("="))
buttonresult.grid(column=3,row=4)
btn_clr = Button(window,text="Clear",**button_prop,command=clear)
btn_clr.grid(column=2,row=5,columnspan=2,ipadx=40,pady=10)


window.mainloop()