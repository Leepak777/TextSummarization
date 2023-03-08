import requests
import mtranslate

languages = [
    'af', 'sq', 'am', 'ar', 'hy', 'az', 'eu', 'be', 'bn', 'bs', 'bg', 'ca', 'ceb', 'ny', 'zh-cn', 'zh-tw', 'co', 'hr',
    'cs', 'da', 'nl', 'en', 'eo', 'et', 'tl', 'fi', 'fr', 'fy', 'gl', 'ka', 'de', 'el', 'gu', 'ht', 'ha', 'haw', 'iw',
    'hi', 'hmn', 'hu', 'is', 'ig', 'id', 'ga', 'it', 'ja', 'jw', 'kn', 'kk', 'km', 'rw', 'ko', 'ku', 'ky', 'lo', 'la',
    'lv', 'lt', 'lb', 'mk', 'mg', 'ms', 'ml', 'mt', 'mi', 'mr', 'mn', 'my', 'ne', 'no', 'or', 'ps', 'fa', 'pl', 'pt',
    'pa', 'ro', 'ru', 'sm', 'gd', 'sr', 'st', 'sn', 'sd', 'si', 'sk', 'sl', 'so', 'es', 'su', 'sw', 'sv', 'tg', 'ta',
    'tt', 'te', 'th', 'tr', 'tk', 'uk', 'ur', 'ug', 'uz', 'vi', 'cy', 'xh', 'yi', 'yo', 'zu'
]




def translateSentence(text, dest_language):
    try:
        translation = mtranslate.translate(text, dest_language)

    except (requests.exceptions.ReadTimeout, requests.exceptions.ConnectTimeout, requests.exceptions.ConnectionError):
        print(f"Translation failed for {dest_language}. Trying another language...")
        for lang in languages:
            if lang != dest_language:
                try:
                    translation = translateSentence(text, lang)
                    return translation
                except (requests.exceptions.ReadTimeout, requests.exceptions.ConnectTimeout, requests.exceptions.ConnectionError):
                    continue
        # Translation not available for any language.
        print("All translations failed. Returning original text...")
        return text
    return translation


def translateEnglish(text):
    dest_language = 'en'
    try:
        translation = mtranslate.translate(text, dest_language)

    except (requests.exceptions.ReadTimeout, requests.exceptions.ConnectTimeout, requests.exceptions.ConnectionError):
        return text
    return translation








