eq_list1 = """~EQ SHEET [page 1]~
[0] quad formula 
[1] discrimnate 
[2] cos rule
[98] next page
[99] EXIT"""

eq_list2 = """~EQ SHEET [page 2]~
[3] mid point
[4] tan iden  
[5] sin/cos iden
[98] next page 
[99] EXIT"""

eq_list3 = """~EQ SHEET [page 3]~
[6] SIN
[7] COS
[8] TAN
[98] next page 
[99] EXIT"""

eq_list4 = """~EQ SHEET [page 4]~
[9] circle_eqs
[10] NULL 
[11] NULL
[98] first page 
[99] EXIT"""

max_page = 4
max_in = 9
next_page = 98
exit = 99
c_eqs = 9



def menu_out(inp):

    if inp == 1: 
        return eq_list1
    elif inp == 2:
        return eq_list2
    elif inp == 3: 
        return eq_list3
    elif inp == 4:
        return eq_list4

    else:
        print("menu error")
        print(inp)
        input("~enter~")




def getting_in():

    print(eq_list1)
    
    sheet_count = 1

    while True:

        uin = None
        try:
            uin = int(input("--> "))

        except ValueError:
            print("input invalid")
            input("~enter~")
            return None 


        if uin == next_page:

            sheet_count += 1
            
            # resets page once max is reached
            if sheet_count == max_page + 1:
                sheet_count = 1

            print(menu_out(sheet_count))
        

        elif uin <= max_in or uin == exit:
            return uin
            break

        else:
            print("input invalid")
            input("~enter~")
            print(menu_out(sheet_count))



def display_eq(choice):

    #max 21 chars per line
    #eq lists:
    #circle eqs

    c_list = """(x-a)^2+(y-b)^2=r^2\nS=r(theta)\nA=1/2r^2(theta)"""
            
    #all the eqs
    eq_list = ["-b+-(b^2-(4ac))\n/2a", #quad
            "b^2-4ac", #dis
            "a^2=b^2+c^2-2bc*cosA", #cos rule
            "MID=((x1+x2)/2,\n    (y1+y2)/2)", #mid
            "tanx=sinx/cosx", #tan iden
            "sin^2(x)+cos^2(x)=1", #cossin iden
            "SIN:(a or 180-a)+k360", #SIN
            "COS:(a or -a)+k360", #COS
            "TAN:(a) + k180", #TAN
            ]

    if choice == c_eqs:
        print(c_list)

    if choice != exit and choice != c_eqs:
        print(eq_list[choice])



def main():
    
    user_in = None
    while user_in != exit:
        user_in = getting_in()

        while user_in == None:
            user_in = getting_in()

        if user_in <= max_in:
            display_eq(user_in)
            input("~enter~")



main()
