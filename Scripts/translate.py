from translate import Translator

def translateSentence(input_string, language):
    translator = Translator(to_lang=language) 
    return translator.translate(input_string)

