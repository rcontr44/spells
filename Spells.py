def Heal():
    global cpuHP
    global playerHP

    if (playerMP < 10):
        res = "Not enough mana !"
    else:
        banditBash()
        damage = 0
        playerMP -= playerMP - 10
        playerHp = playerHP + random.randint(0,10)

        if(cpuHP <= 0):
            res = "You have won!"
        else:
            res = "Bandit took" + str(damage) + " damage."
            menu(playerHP, playerMaxHP, playerMP, playerSP, cpuHP, cpuMP, cpuSP, playerChoice)
        lbl.configure(text = res)
#####################################################################################################
def Light():
    global cpuHP
    global playerHP

    if (playerMP < 5):
        res = "Not enough mana !"
    else:
        banditBash()
        damage = random.randint()
        playerMP -= playerMP - 5
        cpuHP = cpuHP - damage

        if (cpuHP <= 0):
            res = "You have won!"
        else:
            res = "Bandit took" + str(damage) + " damage."
            menu(playerHP, playerMaxHP, playerMP, playerSP, cpuHP, cpuMP, cpuSP, playerChoice)
        lbl.configure(text=res)
########################################################################################################
def Blizzard():
    global cpuHP
    global playerHP

    if (playerMP < 15):
        res = "Not enough mana !"
    else:
        banditBash()
        damage = random.randint()
        playerMP -= playerMP - 15
        cpuHP = cpuHP - damage

        if (cpuHP <= 0):
            res = "You have won!"
        else:
            res = "Bandit took" + str(damage) + " damage."
            menu(playerHP, playerMaxHP, playerMP, playerSP, cpuHP, cpuMP, cpuSP, playerChoice)
        lbl.configure(text=res)
###################################################################################################################
def Shine():
    global cpuHP
    global playerHP

    if (playerMP < 10):
        res = "Not enough mana !"
    else:
        banditBash()
        damage = random.randint()
        playerMP -= playerMP - 10
        cpuHP = cpuHP - damage

        if (cpuHP <= 0):
            res = "You have won!"
        else:
            res = "Bandit took" + str(damage) + " damage."
            menu(playerHP, playerMaxHP, playerMP, playerSP, cpuHP, cpuMP, cpuSP, playerChoice)
        lbl.configure(text=res)
############################################################################
def Permafrost():
    global cpuHP
    global playerHP

    if (playerMP < 20):
        res = "Not enough mana !"
    else:
        banditBash()
        damage = rand0m.randint()
        playerMP -= playerMP - 20
        cpuHP = cpuHP - damage

        if (cpuHP <= 0):
            res = "You have won!"
        else:
            res = "Bandit took" + str(damage) + " damage."
            menu(playerHP, playerMaxHP, playerMP, playerSP, cpuHP, cpuMP, cpuSP, playerChoice)
        lbl.configure(text=res)

