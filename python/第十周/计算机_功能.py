import tkinter as tk


root =tk.Tk()
root.geometry("350x500")
root.title("计算器")
root.resizable(0,0)

displayFrame = tk.Frame(root,width=350,height=150)
displayFrame.pack(side='top',fill=tk.X,padx=0,pady=0)

displayLabel = tk.Label(displayFrame,font=('',36,'bold'),anchor='e')
displayLabel.pack(fill=tk.X,expand=1,padx=10,pady=10)

buttonFrame=tk.Frame(root,width=350,height=350,background='red')
buttonFrame.pack(side='top',fill=tk.BOTH,expand=1,padx=0,pady=0)

button_font=('Helvetica',18,'bold')
button_width=10
button_height=50
button_pads=10
button_paddy=10

buttonStrings=[
    ['CE','C',"\u2190",'/'],
    ['7','8','9','*'],
    ['4','5','6','-'],
    ['1','2','3','+'],
    ['+/-','0','.','=']
]

buttonDict={}
row_index=0
for roister in buttonStrings:
    col_index=0
    for colStr in roister:
        button=tk.Button(buttonFrame, text=colStr, width=button_width, height=button_height, padx=button_pads, pady=button_paddy)
        buttonDict[colStr]=button
        button.grid(row=row_index,column=col_index,stick=tk.E+tk.N+tk.S+tk.W)
        col_index+=1
    row_index+=1

for i in range(5):
    buttonFrame.grid_rowconfigure(i,weight=1)
for i in range(4):
    buttonFrame.grid_columnconfigure(i,weight=1)

operationDict={'operator':None,'number1':None,'number2':None}
displayNumber=tk.StringVar()
displayLabel.config(textvariable=displayNumber)
def resetOperaDict():
    operationDict['operator']=None
    operationDict['number1']=None
    operationDict['number2']=None
displayNumber.set(0)
def setCommand(text,cmd):
    buttonDict[text].config(command=cmd)

def ce():
    displayNumber.set(0)
def c():
    resetOperaDict()
    operationDict['number1']=None
    displayNumber.set(0)

def delNum():
    if (displayNumber.get()[0]=='-'and len(displayNumber.get())==2)or len(displayNumber.get())==1:
        displayNumber.set(0)
    else:
        displayNumber.set(displayNumber.get()[:-1])
def fourRule(op:dict,opr):
    op['operator']=opr
    op['number1']=displayNumber.get()
    displayNumber.set(0)

def operation(op:dict):
    global result
    if not op['operator']:
        pass
    else:
        if op['operator']=='+':
            result=float(op['number1'])+float(displayNumber.get())
        if op['operator']=='-':
            result=float(op['number1'])-float(displayNumber.get())
        if op['operator']=='*':
            result=float(op['number1'])*float(displayNumber.get())
        if op['operator']=='/':
            if float(displayNumber.get())==0:
                c()
                return
            result=float(op['number1'])/float(displayNumber.get())
        if int(result)==result:
            result=int(result)
        else:
            result='{:>20f}'.format(result)
        displayNumber.set(result)
        op['number1']=result
        resetOperaDict()

def plusOrMinus():
    if displayNumber.get()=='0':
        return
    if displayNumber.get()[0]=='-':
        displayNumber.set(displayNumber.get()[1:])
    else:
        displayNumber.set('-'+displayNumber.get())
def setPoint():
    if'.'not in displayNumber.get():
        displayNumber.set(displayNumber.get()+'.')
def shush(num):
    if operationDict['number1'] is not None and operationDict['operator'] is None:
        c()
    if displayNumber.get()=='0':
        displayNumber.set(num)
    else:
        displayNumber.set(displayNumber.get()+str(num))

for i in range(10):
    print(i)
    buttonDict[str(i)].config(command=lambda num=i:shush(num))
buttonDict['.'].config(command=setPoint)
setCommand('+/-',plusOrMinus)
setCommand('=', lambda opera=operationDict:operation(opera))
setCommand('+', lambda opera = operationDict:fourRule(opera, '+'))
setCommand('-', lambda opera = operationDict:fourRule(opera, '-'))
setCommand('*', lambda opera = operationDict:fourRule(opera, '*'))
setCommand('/', lambda opera = operationDict:fourRule(opera, '/'))
setCommand('\u2190',delNum)
setCommand('CE',ce)
setCommand('C',c)
root.mainloop()