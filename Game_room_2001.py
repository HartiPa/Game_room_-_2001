from random import randint

winning_score = 2001

def game_2001(type_dice="D6",hod=2):
    # základní atributy
    user_score = 0
    pc_score = 0
    dice = 0
    pocet_kol = 1

    # výběr kosty
    dice_type = {
        "D3":3,
        "D4":4,
        "D6":6,
        "D8":8,
        "D10":10,
        "D12":12,
        "D20":20,
        "D100":100
    }
    if type_dice in dice_type:
        dice += dice_type[type_dice]
    else:
        print("Invalid dice type")
    print(f"{dice}-hraná kosta")

    while user_score < winning_score and pc_score < winning_score:
        # hod hráče:
        hody = []
        print(f"Počet kol : {pocet_kol}")
        for i in range(hod):
            h = randint(1,dice)
            if h == 7:
                user_score =  user_score // 7
            elif h == 11:
                user_score *= 11
            else:
                hody.append(h)
            user_score += h
        print(f"hráč = {user_score} {hody}")
        hody.clear()

        # hod pc:
        for i in range(hod):
            h = randint(1, dice)
            if h == 7:
                pc_score = pc_score // 7
            elif h == 11:
                pc_score *= 11
            else:
                hody.append(h)
            pc_score += h
        print(f"počítač = {pc_score} {hody}")
        print()

        if (user_score or pc_score) < winning_score:
            print(input('Pro další hod stiskni: "ENTER"'))
        hody.clear()
        pocet_kol += 1

    # Vyhlášení vítěže:
    if user_score < pc_score:
        print(pc_score)
        print("Počítač vyhrál!")
    elif user_score > pc_score:
        print(user_score)
        print("Hráč vyhrát!")


game_2001("D20")



"""
2001 - Pravidla hry Každý hráč začíná s 0 body.
 - Ve svém tahu hráč hodí 2 kostkami (standardní kostky D6).
 - Počet získaných bodů se přičte k celkovému skóre.
 - Počínaje druhým tahem:
       pokud hráč hodí 7,
       vydělí svůj počet bodů 7,
       bez ohledu na zlomkovou část,
       pokud hodí 11,
       vynásobí aktuální počet bodů 11.
 - Vyhrává hráč, který jako první dosáhne 2001 bodů.

 Implementace:
 - Implementujte verzi hry pro dva hráče.
 - Mělo by se jednat o konzolovou aplikaci.
 - Druhým hráčem by měl být počítač.
 - Po každém tahu zobrazte aktuální skóre.
 - Hod hráče by měl proběhnout po stisknutí klávesy enter.
 - Hod počítače proběhne automaticky po hodu hráče.
 - Program ukončete, když hráč nebo počítač překročí 2001 bodů.

Modifikace 1:
 - Pravděpodobně jste si všimli, že současná verze hry není příliš interaktivní a spočívá pouze v klikání na klávesu Enter.
 - Zkusme ji udělat trochu interaktivnější.
    - Před každým hodem dejte hráči na výběr.
    - Nechte ho vybrat 2 kostky z následujících: D3, D4, D6, D8, D10, D12, D20, D100
    - Hráč může použít 2 kostky stejného druhu nebo 2 různé kostky.
    - Výběr kostek nechte provést hráče zadáním příslušného řetězce (jeden pro každou kostku).
    - Můžete použít kód z úlohy Kostky.
    - Výběr kostek počítačem by měl být náhodný.

Modifikace 2:
 - Nyní zkuste přenést hru na server pomocí nástroje Flask.
 - Pro ukládání informací mezi tahy použijte skrytá pole formuláře.
 - Není to nejlepší řešení (může být náchylné k podvádění), ale to nás zatím nezajímá.
 - Výběr kostek před hodem by měl být proveden pomocí formuláře.

"""