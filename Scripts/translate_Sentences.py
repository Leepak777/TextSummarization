#from translate import Translator
import requests
from googletrans import Translator
languages = [
    'af', 'sq', 'am', 'ar', 'hy', 'az', 'eu', 'be', 'bn', 'bs', 'bg', 'ca', 'ceb', 'ny', 'zh-cn', 'zh-tw', 'co', 'hr',
    'cs', 'da', 'nl', 'en', 'eo', 'et', 'tl', 'fi', 'fr', 'fy', 'gl', 'ka', 'de', 'el', 'gu', 'ht', 'ha', 'haw', 'iw',
    'hi', 'hmn', 'hu', 'is', 'ig', 'id', 'ga', 'it', 'ja', 'jw', 'kn', 'kk', 'km', 'rw', 'ko', 'ku', 'ky', 'lo', 'la',
    'lv', 'lt', 'lb', 'mk', 'mg', 'ms', 'ml', 'mt', 'mi', 'mr', 'mn', 'my', 'ne', 'no', 'or', 'ps', 'fa', 'pl', 'pt',
    'pa', 'ro', 'ru', 'sm', 'gd', 'sr', 'st', 'sn', 'sd', 'si', 'sk', 'sl', 'so', 'es', 'su', 'sw', 'sv', 'tg', 'ta',
    'tt', 'te', 'th', 'tr', 'tk', 'uk', 'ur', 'ug', 'uz', 'vi', 'cy', 'xh', 'yi', 'yo', 'zu'
]

#def translateSentence(input_string, language):
#    translator = Translator(to_lang=language)
#    try:
#        result = translator.translate(input_string)
#    except StopIteration:
#        # Translation not available for current language. Try another language.
#        for lang in languages:
#            if lang != language:
#                try:
#                    result = translateSentence(input_string, lang)
#                    return result
#                except StopIteration:
#                    continue
#        # Translation not available for any language.
#        raise ValueError("Translation not available for any language.")
#    return result



def translateSentence(text, dest_language):
    translator = Translator(service_urls=['translate.google.com'])
    try:
        translation = translator.translate(text, dest=dest_language)
    except requests.exceptions.ReadTimeout:
        print(f"Translation timed out for {dest_language}. Trying another language...")
        for lang in languages:
            if lang != dest_language:
                try:
                    translation = translateSentence(text, lang)
                    return translation
                except requests.exceptions.ReadTimeout:
                    continue
        # Translation not available for any language.
        print("All translations timed out. Returning original text...")
        return text
    return translation.text






