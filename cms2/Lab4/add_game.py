"""Quiz on history of Ukraine"""
class Level:
    """
    Level standart
    """
    
def que_level_1(quest):
    flg = None
    while True:
        print(quest, "\n('Yes' or 'No')")
        answr = input(">>> ")
        if answr == "Yes" or answr == "No":
            if answr == "Yes":
                flg = True
                break
            else:
                flg = False
                break
        else:
            print("Incorrect answer, try again!")
    return flg

def que_level_2(quest, answr):
    while True:
        print(quest, "\nEnter:\t'a' or 'b' or 'c")
        your_answr = input(">>> ")
        if your_answr in ('a', 'b', 'c'):
            if your_answr == answr:
                return True
            else:
                return False
        else:
            print("Incorrect answer, try again!")

def que_level_3(answr):
    while True:
        print("Do you love Jesus and Ukraine?\n('Yes!!!' or 'No')")
        your_answr = input(">>> ")
        if your_answr in ('Yes!!!', 'No'):
            if your_answr == 'Yes!!!':
                print("I love you!;)")
                return True
            else:
                return False
        else:
            print("---Incorrect answer, try again! LOOK AT EXAMPLES, and corect them---")

if __name__ == '__main__':
    print("Enter your name (in English): ")
    name_player = (input(">>> "))
    
    print(name_player, "did you ready to know, how well you know the history of Ukraine? \n('Yes' or 'No')")
    while True:
        flg = input(">>> ")
        if flg == "Yes":
            break
        else:
            print("Incorrect answer, try again!")
# __________________level №1__________________

    print("Then, let's start")
    amount_of_points = 0
    for i in range(3):
        print("\n___level №1___")
        level_point = 0

        quest = "Was Ukrainian territory occupied by russia?"
        if que_level_1(quest): level_point += 3
        quest = "Did Volodymyr the Great christen Kyivan Rus?"
        if que_level_1(quest): level_point += 3
        quest = "Did World War II end in 1939?"
        if que_level_1(quest) == False: level_point += 3
        quest = "Was Simon Petliura the first president of Ukraine?"
        if que_level_1(quest) == False: level_point += 3
        quest = "The first constitution in Europe was created in Ukraine?"
        if que_level_1(quest): level_point += 3

        if level_point >= 9: # 60%
            amount_of_points += level_point
            print("---A good result. Then, let's try to go to the next level---")
            break
        elif i == 2:
            amount_of_points += level_point
            print("---Bad result. let's try to go to the next level---")
        else:
            print("---Bad result. The test is filled, try again!---")
    # __________________level №2_____________________
    quest_varian = ["When they christened the Kyivan Rus?\na - 920\tb - 988\tc - 1218", 
    "Who was the first Hetman?\na - Dmytro Vyshnevetskyi\nb - Kyrylo Rozumovskyi\nc - Petro Sahaidachnyi", 
    "What does the flag of Ukraine symbolize?\na - The sky and the wheat field\nb - Sunrise\nc - Water and land",
    "Who wrote the text of the national anthem of Ukraine?\na - Taras Shevchenko\nb - Pavlo Chubynskyi\nc - Oleg Vinnyk",
    "When Ukraine's independence was proclaimed?\na - 29.02.1996\nb - 12.02.1992\nc - 12.02.1991",
    "Who is the author of the song 'Chervona Ruta'?\na - Volodymyr Ivasyuk\nb - Oleg Sapchuk\nc - There is no author",
    "Which organization was the author of universals?\na - Organization Ukrainian Nationalists\nb - 'Ukrainian Insurgent Army'\nc - 'Ukrainian Central Rada'",
    "Who destroyed the Cossacks?\na - Catherine 2\nb - Peter 1\nc - Joseph Stalin"]
    tru_answr = ['b', 'a', 'a', 'b', 'c', 'a', 'c', 'a']
    for i in range(2):
        print("\n___level №2___")
        level_point = 0
        for i in range(8):
            if que_level_2(quest_varian[i], tru_answr[i]):
                level_point += 7

        if level_point >= 33: # 60%
            amount_of_points += level_point
            print("---A good result. Then, let's try to go to the next level---")
            break
        elif i == 1:
            amount_of_points += level_point
            print("---Bad result. let's try to go to the next level---")
        else:
            print("---Bad result. The test is filled, try again!---")


    # __________________level №3___________________

    if que_level_3('Yes!!!'):
        amount_of_points += 30
    else:
        amount_of_points = 0
    
    #___________________Results___________________
    print("_______________________________________________\nResults:")
    if amount_of_points == 0:
        print(name_player, ",you don't know history... learn to love Jesus and Ukraine!\nYour score is", amount_of_points, "out of 100")
    elif amount_of_points <= 60:
        print(name_player, ",you don't know history... I advise you to teach.\nYour score is", amount_of_points, "out of 100")
    elif amount_of_points <= 75:
        print(name_player, ",not bad, but worth learning\nYour score is", amount_of_points, "out of 100")
    elif amount_of_points <= 90:
        print(name_player, ",good level of knowledge\nYour score is", amount_of_points, "out of 100")
    else:
        print(name_player, ",you are a genius!!!!!\nYour score is", amount_of_points, "out of 100")
    print("_______________________________________________")
