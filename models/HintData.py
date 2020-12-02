

titlesKeyProcess = [
    "Распределим буквы по группам, по количеству звуков в произношении",
    "Каждой букве сопоставим ее номер в алфавите",
    "Значение каждого номера переведем в соответствующую систему счисления в зависимости от номера группы",
    "Добавим в начала кода каждой буквы id ее группы"
]

titlesWordProcess = [
    "Переведем числа из соотвествующих систем счисления в десятичную, чтобы получить номера букв в алфавите",
    "Каждый номер заменим на соответсвующую букву в алфавите"
]


def create_key_hints(key_values):
    hints = list()
    hints.append([titlesKeyProcess[0], "0"])
    for i in range(1, len(titlesKeyProcess)):
        hints.append([titlesKeyProcess[i], key_values[i - 1]])
    return hints


def create_word_hints(word_values):
    hints = list()
    for i in range(0, len(titlesWordProcess)):
        hints.append([titlesWordProcess[i], word_values[i]])
    return hints
