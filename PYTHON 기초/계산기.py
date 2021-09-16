# import tkinter as tk

# disValue = 0
# operator = {'+':1, '-':2, '/':3, 'X':4, 'C':5, '.':6, '%':7, '<':8, '=':9, '+/-':10}
# stoValue = 0
# opPre = 0

# def number_click(value):
#     # print('숫자',value)
#     global disValue
#     disValue = (disValue*10) + value
#     str_value.set(disValue)

# def clear():
#     global disValue, stoValue, opPre
#     disValue = 0
#     stoValue = 0
#     opPre = 0
#     str_value.set(disValue)

# def oprator_click(value):
#     # print('명령',value)
#     global disValue, operator, stoValue, opPre
#     op = operator[value]
#     if op == 5:
#         clear()
#     elif disValue == 0:
#         opPre = 0
#     elif opPre == 0:
#         opPre = op
#         stoValue = disValue
#         # disValue = 0
#         str_value.set(disValue)
#     elif op == 9:
#         if opPre == 1:
#             disValue = stoValue + disValue 
#         elif opPre == 2:
#             disValue = stoValue - disValue
#         elif opPre == 3:
#             if stoValue % disValue != 0:
#                 disValue = stoValue / disValue
#             else:
#                 disvalue = stoValue // disValue
#         elif opPre == 4:
#             disValue = stoValue * disValue

#         str_value.set(disValue)
#         opPre = 0
#     else:
#         disValue = 0
#         stoValue = 0
#         clear()

# def button_click(value):
#     print(value)
#     try:
#         value = int(value)
#         number_click(value)
#     except:
#         oprator_click(value)


# win = tk.Tk() # 창 생성
# win.title("계산기") # 창 제목
# win.option_add("*Font","맑은고딕 25") # 전체 폰트

# str_value = tk.StringVar()
# str_value.set(str(disValue))

# dis = tk.Entry(win, textvariable = str_value, justify = 'right')
# dis.grid(column = 0, row = 0 , columnspan = 4, ipadx = 22, ipady= 30)

# calItem = [['%','C','/','<'],
#            ['7','8','9','X'],
#            ['4','5','6','-'],
#            ['1','2','3','+'],
#            ['+/-','0','.','=']]

# for i, items in enumerate(calItem):
#     for k, item in enumerate(items):
#         bt = tk.Button(win, 
#             text = item, 
#             width = 5, 
#             height = 3,
#             command = lambda cmd = item: button_click(cmd)
#             )
#         bt.grid(column=k, row=(i+1))
# win.mainloop() # 창 실행

import tkinter as tk

disValue = 0
operator = {'+':1, '-':2, '/':3, 'X':4, 'C':5, '.':6, '%':7, '<':8, '=':9, '+/-':10}
stoValue = 0
opPre = 0

def number_click(value):
    global disValue

    disValue = (disValue*10) + value
    str_value.set(disValue)

def clear():
    global disValue, stoValue, opPre

    disValue = 0
    stoValue = 0
    opPre = 0
    str_value.set(disValue)

def oprator_click(value):
    global disValue, operator, stoValue, opPre

    op = operator[value]
    
    if op == 5:
        clear()
    elif disValue == 0:
        opPre = 0
    elif opPre == 0:
        opPre = op
        stoValue = disValue
        # disValue = 0
        str_value.set(disValue)
    elif op == 9:
        if opPre == 1:
            disValue = stoValue + disValue 
        elif opPre == 2:
            disValue = stoValue - disValue
        elif opPre == 3:
            if stoValue % disValue != 0:
                disValue = stoValue / disValue
            else:
                disvalue = stoValue // disValue
        elif opPre == 4:
            disValue = stoValue * disValue

        str_value.set(disValue)
        opPre = 0
    else:
        disValue = 0
        stoValue = 0
        clear()

def button_click(value):
    print(value)
    try:
        value = int(value)
        number_click(value)
    except:
        oprator_click(value)


win = tk.Tk() # 창 생성
win.title("계산기") # 창 제목
win.option_add("*Font","맑은고딕 25") # 전체 폰트

str_value = tk.StringVar()
str_value.set(str(disValue))

dis = tk.Entry(win, textvariable = str_value, justify = 'right')
dis.grid(column = 0, row = 0 , columnspan = 4, ipadx = 22, ipady= 30)

calItem = [['%','C','/','<'],
           ['7','8','9','X'],
           ['4','5','6','-'],
           ['1','2','3','+'],
           ['+/-','0','.','=']]

for i, items in enumerate(calItem):
    for k, item in enumerate(items):
        bt = tk.Button(win, 
            text = item, 
            width = 5, 
            height = 3,
            command = lambda cmd = item: button_click(cmd)
            )
        bt.grid(column=k, row=(i+1))
win.mainloop() # 창 실행
