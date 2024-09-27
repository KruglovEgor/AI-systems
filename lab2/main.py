from os import putenv

putenv("SWI_HOME_DIR", "E:\\Program Files\\swipl")


from pyswip import Prolog


prolog = Prolog()
prolog.consult("genshin_2.pl")


QUALITIES = {
    5: [5, "5", "legendary", "five", "five-star", "легендарный", "пять", "пяти-звездный", "лега"],
    4: [4, "4", "epic", "four", "four-star", "эпический", "четыре", "четырех-звездный", "эпик"]
}

ELEMENTS = {
    "'Dendro'": ["dendro", "дендро"],
    "'Cryo'": ["cryo", "крио"],
    "'Pyro'": ["pyro", "пиро"],
    "'Hydro'": ["hydro", "гидро"],
    "'Geo'": ["geo", "гео"],
    "'Electro'": ["electro", "электро"],
    "'Anemo'": ["anemo", "анемо"]
}

WEAPONS = {
    "'Bow'": ["bow", "bows", "лук", "луки", "лучник", "лучники", "лучников", "лучниц", "лучница", "лучницы"],
    "'Catalyst'": ["catalyst", "catalysts", "каталист", "каталисты", "каталистов", "катализатор", "катализаторы", "катализаторов"],
    "'Polearm'": ["polearm", "polearms", "копье", "копья", "копейщик", "копейщики", "копейщиков", "копейщиц", "копейщицы"],
    "'Sword'": ["sword", "однорук", "одноручный", "одноручное"],
    "'Claymore'": ["claymore", "двурук", "двуручный", "двуручное"]
}

REGIONS = {
    "'Mondstadt'": ["mondstadt", "монштад"],
    "'Liyue'": ["liyue", "ли юэ", "лиюэ"],
    "'Inazuma'": ["inazuma", "иназума"],
    "'Sumeru'": ["sumeru", "сумеру"],
    "'Fontaine'": ["fontaine", "фонтейн"],
    "'Natlan'": ["natlan", "натлан"],
    "'Snezhnaya'": ["snezhnaya", "снежная"],
    "'Other world'": ["other", "нашего", "другого", "другой", "our", "here", "иной"]
}

GENDERS = {
    "'Female'": ["female", "females", "f", "woman", "women", "w", "женщина", "женщин", "женщиной", "женщины", "девушка",
                 "девушки", "девушкой", "ж", "женский", "женские"],
    "'Male'": ["male", "males", "m", "man", "men", "мужчина", "мужчин", "мужчиной", "мужской", "мужскому", "парень",
               "парни", "парней", "мужской", "мужские", "мужскому", "м"]
}


def format_input(inp_str):
    inp_str.lower().strip()
    punc_marks = [",", ".", ";", "!", "?", "'", '"']
    for mark in punc_marks:
        inp_str = inp_str.replace(mark, " ")

    return inp_str.split()


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
        return res
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

    return quals, elems, weapons, regs, genders


def get_query(quals, elems, weapons, regs, genders):
    key_words = ["quality", "element", "weapon", "region", "gender"]
    prefs = [quals, elems, weapons, regs, genders]
    query = ""

    for i in range(len(key_words)):
        key_word = key_words[i]
        preference = prefs[i]
        temp_query = ""
        if len(preference[0]) > 0:
            for j in range(len(preference[0])):
                if j != len(preference[0])-1:
                    temp_query += f"{key_word}(Name, {preference[0][j]}); "
                else:
                    temp_query += f"{key_word}(Name, {preference[0][j]})"

        elif len(preference[1]) > 0:
            temp_query += f"{key_word}(Name, {key_word.capitalize()}), "
            for j in range(len(preference[1])):
                if j != len(preference[1])-1:
                    temp_query += f"{key_word.capitalize()} \\= {preference[1][j]}, "
                else:
                    temp_query += f"{key_word.capitalize()} \\= {preference[1][j]}"

        if len(temp_query) != 0:
            if i == 0:
                query += f"({temp_query})"
            else:
                query += f", ({temp_query})"

    if len(query) > 0:
        return query + "."
    else:
        return "character(Name)."


quals, elems, weapons, regs, genders = get_preferences()
query = get_query(quals, elems, weapons, regs, genders)
res = list(prolog.query(query))
if len(res) > 0:
    print("Here are matches: ")
    for character in res:
        print(character["Name"])
else:
    print("Ops, there are no characters matching your description :(")


