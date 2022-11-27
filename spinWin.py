import random as rd
status=True
count=0
while(status):
    element = ["⭐", "💰", "⚽", "🏏"]
    a = rd.choice(element)
    b = rd.choice(element)
    c = rd.choice(element)
    print(f'''{a} {b} {c} ''')
    count+=1

    if a == b or a == c:
        if a == b and a == c:
            print(f'''**********************************************\n---------- Bingo !! You Win The Game ---------\n**********************************************''')
            print(f"Total Spins taken To Win The Game :{count}")
            break

    choice=input("You Want to Continue ? :Y/N\n")

    if choice.upper()=="Y":
        status = True
    elif choice.lower()=="N":
        print("Game Finished !!")
        status=False
    else:
        print("Invalid Choice!! Please Replay The Game")
        status = False








