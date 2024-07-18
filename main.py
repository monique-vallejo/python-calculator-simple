import customtkinter
from tkinter import END
from tkinter import messagebox
def clear():
    entryField.delete(0, END)

def click(number):
    entryField.insert(END, number)

def answer():
     expression=entryField.get()
     try:
         result = eval(expression)
         ans=round(result,1)
         entryField.delete(0, END)
         entryField.insert(0, ans)
     except SyntaxError:
        messagebox.showerror('Oops! Something went wrong.', 'You used an invalid expression!')
     except ZeroDivisionError:
         messagebox.showerror('Oops! Something went wrong.', 'A number cannot be divide by zero!')


#GUI START HERE!
root = customtkinter.CTk()
root.title('Pocket Calculator')
root.geometry('300x320')
root.config(bg='#DCEDC8')


entryField=customtkinter.CTkEntry(root, font=('monospace', 20, 'bold'), text_color= '#546E7A',
                                  fg_color='#A5D6A7', border_color= 'green', width=280, height=50, bg_color='#A5D6A7')
entryField.grid(row=0, column=0, padx=10, pady=10, columnspan=4)


b0 = customtkinter.CTkButton(root, text= '0', font=('monospace', 20, 'bold'), width=60, bg_color='black',
                             cursor='hand2', command=lambda :click('0'),  fg_color='#66BB6A', border_color= 'green', hover_color='#2E7D32')

b1 = customtkinter.CTkButton(root, text= '1', font=('monospace', 20, 'bold'), width=60, bg_color='black',
                             cursor='hand2', command=lambda :click('1'), fg_color='#66BB6A', border_color= 'green', hover_color='#2E7D32')


b2 = customtkinter.CTkButton(root, text= '2', font=('monospace', 20, 'bold'), width=60, bg_color='black',
                             cursor='hand2', command=lambda :click('2'), fg_color='#66BB6A', border_color= 'green', hover_color='#2E7D32')

b3 = customtkinter.CTkButton(root, text= '3', font=('monospace', 20, 'bold'), width=60, bg_color='black',
                             cursor='hand2', command=lambda :click('3'), fg_color='#66BB6A', border_color= 'green', hover_color='#2E7D32')

b4 = customtkinter.CTkButton(root, text= '4', font=('monospace', 20, 'bold'), width=60, bg_color='black',
                             cursor='hand2', command=lambda :click('4'), fg_color='#66BB6A', border_color= 'green', hover_color='#2E7D32')

b5 = customtkinter.CTkButton(root, text= '5', font=('monospace', 20, 'bold'), width=60, bg_color='black',
                             cursor='hand2', command=lambda :click('5'), fg_color='#66BB6A', border_color= 'green', hover_color='#2E7D32')


b6 = customtkinter.CTkButton(root, text= '6', font=('monospace', 20, 'bold'), width=60, bg_color='black',
                             cursor='hand2', command=lambda :click('6'),fg_color='#66BB6A', border_color= 'green', hover_color='#2E7D32')

b7 = customtkinter.CTkButton(root, text= '7', font=('monospace', 20, 'bold'), width=60, bg_color='black',
                             cursor='hand2', command=lambda :click('7'), fg_color='#66BB6A', border_color= 'green', hover_color='#2E7D32')

b8 = customtkinter.CTkButton(root, text= '8', font=('monospace', 20, 'bold'), width=60, bg_color='black',
                             cursor='hand2', command=lambda :click('8'), fg_color='#66BB6A', border_color= 'green', hover_color='#2E7D32')


b9 = customtkinter.CTkButton(root, text= '9', font=('monospace', 20, 'bold'), width=60, bg_color='black',
                             cursor='hand2', command=lambda :click('9'),fg_color='#66BB6A', border_color= 'green', hover_color='#2E7D32')

bplus = customtkinter.CTkButton(root, text= '+', font=('monospace', 20, 'bold'), width=60, bg_color='black',
                             cursor='hand2', fg_color='#A1887F', hover_color='#5D4037', command=lambda :click('+'))
bminus = customtkinter.CTkButton(root, text= '-', font=('monospace', 20, 'bold'), width=60, bg_color='black',
                             cursor='hand2', fg_color='#A1887F', hover_color='#5D4037', command=lambda :click('-'))

bmultiply = customtkinter.CTkButton(root, text= '*', font=('monospace', 20, 'bold'), width=60, bg_color='black',
                             cursor='hand2', fg_color='#A1887F', hover_color='#5D4037', command=lambda :click('*'))

bdivide = customtkinter.CTkButton(root, text= '/', font=('monospace', 20, 'bold'), width=60, bg_color='black',
                             cursor='hand2', fg_color='#A1887F', hover_color='#5D4037', command=lambda :click('/'))

bdot = customtkinter.CTkButton(root, text= '.', font=('monospace', 20, 'bold'), width=60, bg_color='black',
                             cursor='hand2', fg_color='#A1887F', hover_color='#5D4037', command=lambda :click('.'))
bclear = customtkinter.CTkButton(root, text= 'C', font=('monospace', 20, 'bold'), width=60, bg_color='black',
                             cursor='hand2', fg_color='#E57373', hover_color='#D32F2F', command= clear)


bequal = customtkinter.CTkButton(root, text= '=', font=('monospace', 20, 'bold'), width=280, bg_color='black',
                             cursor='hand2', fg_color='#7CB342', hover_color='#33691E', command= answer)

b0.grid(row=4, column=0, pady=10)
bclear.grid(row=4, column=1)
bdot.grid(row=4, column=2)
bdivide.grid(row=4, column=3)
b1.grid(row=3, column=0, pady=10)
b2.grid(row=3, column=1)
b3.grid(row=3, column=2)
bmultiply.grid(row=3, column=3)
b4.grid(row=2, column=0, pady=10)
b5.grid(row=2, column=1)
b6.grid(row=2, column=2)
bminus.grid(row=2, column=3)
b7.grid(row=1, column=0, pady=10)
b8.grid(row=1, column=1)
b9.grid(row=1, column=2)
bplus.grid(row=1, column=3)
bequal.grid(row=5, column=0, columnspan=4)


root.mainloop()

