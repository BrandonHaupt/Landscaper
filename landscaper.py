win_amount = 1000
game = {"lawn-tools": 0, "money": 0}
tools = [
    {"name": "Teeth", "profit": 1, "cost": 0},
    {"name": "Scissors", "profit": 5, "cost": 5},
    {"name": "Old-timey Push Lawnmower ", "profit": 50, "cost": 25},
    {"name": "Batter-Powered Lawnmower", "profit": 100, "cost": 250},
    {"name": "Starving Students", "profit": 250, "cost": 500}
]

# GAME PRIMARY 
def mow_lawn():
    tool = tools[game["lawn-tools"]]
    print(f"You found a lawn and asked the owner to mow it, you used {tool['name']} and you recieved {tool['profit']}.")
    game["money"] += tool["profit"]

# CHECK STATS FUNCTION
def check_stats():
    tool = tools[game["lawn-tools"]]
    print(f'You currently have {game["money"]} and are using {tool["name"]}')
    
# CHECK UPGRADE FUNCTION
def upgrade():
    if(game["lawn-tools"] >= len(tools) - 1):
        print("No more upgrades available!")
        return 0
    
    next_tool = tools[game["lawn-tools"]+1]
    if(next_tool == None):
        print("there is no more tools available")
        return 0
    if(game["money"] < next_tool["cost"]):
        print("You dont have enought money for the tool")
        return 0
    game["money"] -= next_tool["cost"]
    game["lawn-tools"] += 1
    print("You upgraded your tool!")
    
# GAME WIN FUNCTION
def win_check():
    if(game["lawn-tools"] == 4 and game["money"] >= win_amount):
        print("You won the game! Congradulations!!!!")
        return True
    return False

# PRIMARY LOOP
while(True):
    user_choice = input("[1] Mow Lawn [2] Check Stats [3] Upgrade Tool [Q] Quit")
    
    if(user_choice == "1"):
        mow_lawn()
        
    if(user_choice == "2"):
        check_stats()
        
    if(user_choice == "3"):
        upgrade()
        
    if(user_choice == "q" or user_choice == "Q"):
        print("You quit the game")
        break
    
    if(win_check()):
        break