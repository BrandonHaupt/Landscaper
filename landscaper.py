while(True):
    user_choice = input("[1] Mow Lawn [2] Check Stats [Q] Quit")
    money = 0
    
    if(user_choice == "1"):
        print("You found an lawn and asked the owner to mow it, you recieved $1 as payment, he found it kind of awkward that you used your teeth though")
        money += 1
    
    
    if(user_choice == "Q"):
        break
    