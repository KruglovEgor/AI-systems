from os import putenv

putenv("SWI_HOME_DIR", "E:\\Program Files\\swipl")


from pyswip import Prolog


prolog = Prolog()
prolog.consult("genshin_2.pl")

query = "weapon(X, 'Bow')."
res = list(prolog.query(query))
print(res)



QUALITIES = {
    5: [5, "5", "legendary", "five", "five-star", "легендарный", "пять звезд", "пяти звездный", "лега"],
    4: [4, "4", "epic", "four", "four-star", "эпический", "четыре звезды", "четырех звездный", "эпик"]
}

ELEMENTS = {
    "Dendro": ["dendro", "дендро"],
    "Cryo": ["cryo", "крио"],
    "Pyro": ["pyro", "пиро"],
    "Hydro": ["hydro", "гидро"],
    "Geo": ["geo", "гео"],
    "Electro": ["electro", "электро"],
    "Anemo": ["anemo", "анемо"]
}

WEAPONS = {
    "Bow": ["bow", "лук", "лучник"],
    "Catalyst": ["catalyst", "каталист", "катализатор"],
    "Polearm": ["polearm", "копье", "копейщик"],
    "Sword": ["sword", "однорук", "одноручный"],
    "Claymore": ["claymore", "двурук", "двуручный"]
}

REGIONS = {
    "Mondstadt": ["mondstadt", "монштад"],
    "Liyue": ["liyue", "ли юэ", "лиюэ"],
    "Inazuma": ["inazuma", "иназума"],
    "Sumeru": ["sumeru", "сумеру"],
    "Fontaine": ["fontaine", "фонтейн"],
    "Natlan": ["natlan", "натлан"],
    "Snezhnaya": ["snezhnaya", "снежная"],
    "Other world": ["other world", "не из этого мира", "не из нашего мира", "другого мира", "другой мир"]
}

GENDERS = {
    "Female": ["female", "f", "woman", "w", "женщина", "девушка", "ж", "женский"],
    "Male": ["male", "m", "man", "мужчина", "парень", "мужской", "м"]
}


def format_input(str):
    str.lower().strip()
    punc_marks = [",", ".", ";", "!", "?"]
    for mark in punc_marks:
        str = str.replace(mark, " ")

    # type_of_weapon = {
    #     "bow catalyst": ["range", "дальний", "дальнего", "издали"],
    #     "polearm sword claymore": ["melee", "ближнего", "ближний", "в упоре", "близи"]
    # }
    #
    # for weap, key_list in type_of_weapon.items():
    #     for keyword in key_list:
    #         str = str.replace(keyword, weap)

    return str.split()


def get_matches(key_dict, parsed_inp):
    res = [[], []]
    matches = []
    not_list = ["не", "нет", "no", "not"]

    for i in range(len(parsed_inp)):
        word = parsed_inp[i]
        for param, key_words in key_dict.items():
            if word in key_words:
                matches.append([param, i])

    start = 0
    if len(matches) == 0:
        return []
    elif len(matches) >= 1:
        for i in range(len(matches)):
            met_not = False
            for j in range(start, matches[i][1]):
                if parsed_inp[j] in not_list:
                    met_not = True
                    if matches[i][0] in res[0]:
                        res[0].remove(matches[i][0])
                    elif matches[i][0] not in res[1]:
                        res[1].append(matches[i][0])
            if not met_not:
                res[0].append(matches[i][0])
            start = matches[i][1]+1

    return res


def get_preferences():
    print("Hi, we can help you find a character for you!")
    print("We will ask you some questions")
    print("1) What quality would you prefer?")
    parsed_qual = format_input(input())
    quals = get_matches(QUALITIES, parsed_qual)
    print("2) What element would you prefer?")
    parsed_elem = format_input(input())
    elems = get_matches(ELEMENTS, parsed_elem)
    print("3) What weapon would you prefer?")
    parsed_weapon = format_input(input())
    weapons = get_matches(WEAPONS, parsed_weapon)
    print("4) What region would you prefer?")
    parsed_reg = format_input(input())
    regs = get_matches(REGIONS, parsed_reg)
    print("5) What gender would you prefer?")
    parsed_gender = format_input(input())
    genders = get_matches(GENDERS, parsed_gender)

    # print("qual", quals)
    # print("elem", elems)
    # print("weap", weapons)
    # print("reg", regs)
    # print("gen", genders)



get_preferences()
