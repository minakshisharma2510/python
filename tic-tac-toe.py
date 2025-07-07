# # tic-tac-toe

d = {1:' ', 2:' ', 3:' ', 4:' ', 5:' ', 6:' ', 7:' ', 8:' ', 9:' '}
#  for displaying a row in grid

def display_row(d,row_number): 
    print("     |     | ")
    print("  ",d[1 + 3*(row_number-1)], "  ","|",d[2 + 3*(row_number-1)], "   "," |",d[3 + 3*(row_number-1)], "  "," ",sep ='')
    print("     |     | ")
display_row(d,1)
#
def display_horizontal_line(n):
    for i in range(n):
        print("=",end ='')
    print(" ")
display_horizontal_line(17)
#
def display_board(d):
    for i in range(1,4):
        display_row(d,i)
        if i < 3:
            display_horizontal_line(17)
display_board(d)
#
def player_name():
    user_1 = input("hi! please enter name of first player")
    print("hi", user_1)
    user_1_char = input("please choose your character x or o")
    while(user_1_char != 'x' and user_1_char != 'o'):
        print("looks like you have not entered from x and o")
        user_1_char = input("please choose your character x or o ")
    user_2 = input("hi! please enter name of second player")
    if user_1_char == 'x': 
        user_2_char = 'o'
    else: 
        user_2_char = 'x'
    print(user_1,"choosed",user_1_char)
    print(user_2,"choosed",user_2_char)
    return((user_1, user_1_char), (user_2, user_2_char))

def row_check(d,char,i):
    if d[1 + i*3] == char and d[2+i*3] == char and d[3+i*3] == char:
        return True
    else:
        return False
    
def column_check(d,char,i):
    if [i+1] == char and d[i+4] == char and d[i+7] == char:
        return True
    else:
        return False
    
def diag1_check(d,char):
    if d[1] == char and d[5] == char and d[9] == char:
        return True
    else:
        return False
    
def diag2_check(d,char):
    if d[3] == char and d[5] == char and d[9] == char:
        return True
    else:
        return False
    
def won(d,char):
    flag = 0
    for i in range(3):
        if row_check(d,char,i) == True:
            flag = 1
        if column_check(d,char,i) == True:
            flag = 1 
    if diag1_check(d,char) == True or diag2_check(d,char) == True:
        flag = 1
    if flag == 1:
        return True
    else:
        return False
    
def complete(d):
    flsg = 1
    for i in range(1, 10):
        if d[i] == ' ':
            flag = 0
    if flag == 0:
        return False
    else:
        return True
(user_1 , user_1_char) , (user_2 , user_2_char)= player_name()

ref = {1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9'}
print("FOllowing are number relation to grid cells")
display_board(ref)

player =1
# d = {1: ' ', 2: ' ',3:' ',4:' ',5:' ',6:' ',7:' ',8:' ',9:' '}
# display_board(d)
while(True):
    if player == 1:
        print(user_1 , "Please select a cell from 1,2...9 where you want to put" ,user_1_char)
        place = input()
        ls = ['1','2','3','4','5','6','7','8','9']
        flag1 = 1
        flag2 = 1
        while(flag1 == 1 or flag2 == 1):
            flag1 = 1
            flag2 = 1
            if place not in ls:
                print ("You have choose not choose form 1 to  9 . Please choosen from 1 - 9")
                place = input("Try again")
                continue
            else:
                flag1 = 0
            place = int(place)
            if d[place] != ' ':
                print("This place is already occupied")
                place = input("Try again")
                continue
            else:
                flag2 = 0
        d[place] = user_1_char
        display_board(d)
        if won (d,user_1_char) == True:
            print( "Congrats!", user_1 ,"You won")
            break
        player = 2
    else:
        print(user_2 , "Please select a cell from 1,2...9 where you want to put" ,user_2_char)
        place = input()
        ls = ['1','2','3','4','5','6','7','8','9']
        flag1 = 1
        flag2 = 1
        while(flag1 == 1 or flag2 == 1):
            flag1 = 1
            flag2 = 1
            if place not in ls:
                print ("You have choose not choose form 1 to  9 . Please choosen from 1 - 9")
                place = input("Try again")
                continue
            else:
                flag1 = 0
            place = int(place)
            if d[place] != ' ':
                print("This place is already occupied")
                place = input("Try again")
                continue
            else:
                flag2 = 0
        d[place] = user_2_char
        display_board(d)
        if won (d,user_2_char) == True:
            print("Congrats!", user_2 ,"You won")
            break
        player = 1
    if complete(d) == True:
        print("Match Draw!!!")
        break
    