from googletrans import Translator

def translate(text, dest):
    return Translator().translate(text=text, dest=dest).text