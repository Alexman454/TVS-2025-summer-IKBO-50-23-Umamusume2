import random

def rock_paper_scissors():
    sp = {'1': "Scissors", '2': "Paper", '3': "Rock"}
    k1, chs = random.choice(list(sp.items()))
    chs = k1+chs
    x = input("Are you ready?\nRock..Paper..Scissors!\n").capitalize()
    if not(x in sp.values()):
        return "No..."
    k2 = next((k for k, v in sp.items() if v == x), None)
    x = k2+x
    print(x[1:]," VS ",chs[1:])
    if (x == chs):
        return "Draw!"
    else:
        match(int(x[:1])):
            case 1:
                if int(chs[:1])==2:
                    return "You Win!"
                else:
                    return "You Lost!"
            case 2:
                if int(chs[:1])==3:
                    return "You Win!"
                else:
                    return "You Lost!"
            case 3:
                if int(chs[:1])==1:
                    return "You Win!"
                else:
                    return "You Lost!"

def head_or_tails():
    sp = ["Heads","Tails"]
    chs = random.choice(sp)
    x=input("Heads or Tails?\n").capitalize()
    if (x==chs):
        return "Correct!"
    elif x in sp:
        return "You Lost!"
    else:
        return "...Huh? Anyway..You Lost!"

def guess_number():
    sp = random.randint(1, 200)
    print("Can you guess a number?")
    while True:
        x=int(input("Take a guess!\n"))
        if x>sp:
            print("Too much! Try lesser number.")
        elif x<sp:
            print("Not enough! Try bigger number.")
        else:
            return "Correct! Good job!"

def hangman():
    sp = ["determination","patience","bravery","justice","integrity","kindness","perseverance"]
    chs = random.choice(sp)
    att = 7
    gs = set()
    print("Can you guess a word?")
    while att > 0:
        show = " ".join([letr if letr in gs else "_" for letr in chs])
        print(show)
        x = input("Take a guess on letter: ")
        if x in chs:
            print("Correct letter!")
            gs.add(x)
            if all(ch in gs for ch in chs):
                return "You Win!\nCorrect word is " + chs
        else:
            print("Wrong letter...")
            att -= 1
    return "You couldn't guess word... Correct answer was " + chs

def dice_battle():
    print("Ready to throw a dice?")
    hp = 1
    ehp = 1
    print("You both had 5 hp!")
    while (hp>0 and ehp>0):
        x = input("Press Enter to throw a dice!")
        yu = random.randint(1, 6)
        en = random.randint(1, 6)
        print("You threw",yu,"and your enemy threw",en)
        if yu > en:
            print("You Won!")
            ehp-=1
        elif yu < en:
            print("You Lost..")
            hp-=1
        else:
           print("Draw!")
    if (hp==0):
        return "You died...Game over!"
    else:
        return "Congratulations! Hp left... " + str(hp)

