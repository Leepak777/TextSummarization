from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
from sumy.utils import get_stop_words
from sumy.nlp.stemmers import Stemmer




def generate_summary(file_path):
    language='english'
    SENTENCES_COUNT = 0

    with open(file_path, 'r', errors='ignore') as f:
        text = f.read()


    desired_char = '.'

    for char in text:
        if char == desired_char:
            SENTENCES_COUNT += 1
            
    SENTENCES_COUNT /= 10 
    if SENTENCES_COUNT <= 1:
        SENTENCES_COUNT = 1
    parser = PlaintextParser.from_file(file_path, Tokenizer(language))
    stemmer = Stemmer(language)
    summarizer = LsaSummarizer(stemmer)
    summarizer.stop_words = get_stop_words(language)
    summary = summarizer(parser.document, SENTENCES_COUNT)
    summary_sentences = []
    for sentence in summary:
        summary_sentences.append(str(sentence))
    return summary_sentences


