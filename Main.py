import eel
import Utils


@eel.expose
def create_key(word):
    return Utils.create_key(word)


@eel.expose
def get_key_hints():
    return Utils.get_key_hints()


@eel.expose
def create_word(key):
    return Utils.create_word(key)


@eel.expose
def get_word_hints():
    return Utils.get_word_hints()


eel.init("web")
eel.start("main.html", size=(550, 700))
