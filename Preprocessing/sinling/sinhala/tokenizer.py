import re
from typing import Tuple, Text, Dict, List

import emoji

Boolean = bool

__all__ = [
    'SinhalaTokenizer',
    'SinhalaTweetTokenizer'
]


def is_a_sinhala_letter(s: Text) -> Boolean:
    if len(s) != 1:
        return True
    sinhala_lower_bound = 3456
    sinhala_upper_bound = 3583
    cp = ord(s[0])  # first letter of str
    if sinhala_lower_bound <= cp <= sinhala_upper_bound:
        return True
    return False


def contains_sinhala(s: Text) -> Boolean:
    for c in s:
        if is_a_sinhala_letter(c):
            return True
    return False


# noinspection SpellCheckingInspection
class Tokenizer:
    def tokenize(self, sentence: Text) -> List[Text]:
        raise NotImplementedError()


# noinspection SpellCheckingInspection
class SinhalaTokenizer(Tokenizer):
    def __init__(self):
        self.isolate_punctuations_with_spaces = False
        self.punctuation_marks = [
            '.', ',', '\n', ' ', '¸', '‚','෴',
            '"', '/', '-', '|', '\\', '—', '¦',
            '”', '‘', '\'', '“', '’', '´', '´',
            '!', '@', '#', '$', '%', '^', '&', '*', '+', '-', '£', '?', '˜',
            '(', ')', '[', ']', '{', '}',
            ':', ';',
            '\u2013'  # EN - DASH
        ]
        self.invalid_chars = [
            'Ê',
            '\u00a0', '\u2003',  # spaces
            '\ufffd', '\uf020', '\uf073', '\uf06c', '\uf190',  # unknown or invalid unicode chars
            '\u202a', '\u202c', '\u200f'  # direction control chars(for arabic, starting from right etc)
        ]
        self.line_tokenizing_chars = [
            '.', '?', '!', ':', ';', '\u2022'
        ]
        self.punctuations_without_line_tokenizing_chars = [
            ',', '¸', '‚',
            '"', '/', '-', '|', '\\', '—', '¦',
            '”', '‘', '\'', '“', '’', '´', '´',
            '!', '@', '#', '$', '%', '^', '&',
            '*', '+', '-', '£', '?', '˜',
            '(', ')', '[', ']', '{', '}',
            ':', ';',
            '\u2013'
        ]
        self.short_forms = [
            'ඒ.', 'බී.', 'සී.', 'ඩී.', 'ඊ.', 'එෆ්.', 'ජී.', 'එච්.',
            'අයි.', 'ජේ.', 'කේ.', 'එල්.', 'එම්.', 'එන්.', 'ඕ.',
            'පී.', 'කිව්.', 'ආර්.', 'එස්.', 'ටී.', 'ඩබ.', 'ඩබ්ලිව්.',
            'එක්ස්.', 'වයි.', 'ඉසෙඩ්.',
            'පෙ.', 'ව.', 'වී.',
            'රු.',
            'පා.',  # parliment
            '0.', '1.', '2.', '3.', '4.', '5.', '6.', '7.', '8.', '9.'
        ]

        self.number_bullets = ['0.', '1.', '2.', '3.', '4.', '5.', '6.', '7.', '8.', '9.',]

        # Do not use `short_form_identifier` at `punctuation_marks`
        self.short_form_identifier = '\u0D80'

        #  init ignoring chars
        self.ignoring_chars = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
            'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
            '\u200c', '\u0160', '\u00ad', '\u0088', '\uf086', '\u200b', '\ufeff', 'Á', 'À', '®', '¡', 'ª', 'º', '¤','>','<'
            '¼', '¾', 'Ó', 'ø', '½', 'ˆ', '', '¢', 'ÿ', '·', 'í', 'Ω', '°', '×', 'µ', '', '~', 'ƒ', '', 'ë', 'Î','◞',
            '‰', '»', '«', 'à', '«', '·', '¨', '…', '⋆', '›', '¥', '⋆', '', '˝', '', '', '◊', 'Ł', '', 'ê', 'Õ', 'Ä',
            'á', 'Ñ', 'Í', '', 'Ñ', 'ç', 'Æ', 'ô', 'Ž', '€', '§', 'Æ', '÷', 'é', '¯', 'é', 'æ', 'î', 'ï', 'ä', 'Ô', 'õ','→',
            'È', 'Ý', 'ß', 'õ', '', 'ù', 'å', 'Ø', 'Œ', 'Ô', 'Ü', '', 'Ö', 'Û', 'Ï', 'ñ', 'ý', 'œ', '¹', '', 'É', '¯','❤',
            'Ò', '`','"','´','“','”','*','♦','█','=','','_','' '\u200d'
        ]

        # init word tokenizer
        self.word_tokenizer_delims = '[{}]'.format(
            re.escape(''.join(self.punctuation_marks + self.invalid_chars)))

        # init line tokenizer
        self.line_tokenizer_delims = '[{}]'.format(re.escape(''.join(self.line_tokenizing_chars)))

    #replace number with ########
    def clean_numbers(self, x):
        if bool(re.search(r'\d', x)):
            x = re.sub('[0-9]{5,}', '#####', x)
            x = re.sub('[0-9]{4}', '####', x)
            x = re.sub('[0-9]{3}', '###', x)
            x = re.sub('[0-9]{2}', '##', x)
            x = re.sub('[0-9]{1}', '#', x)
        return x

    def tokenize(self, sentence: Text) -> List[Text]:
        # remove ignoring chars from document
        for ignoring_char in self.ignoring_chars:
            if ignoring_char in sentence:
                sentence = sentence.replace(ignoring_char, '')

        for number_bullet in self.number_bullets:
            if number_bullet in sentence:
                sentence = sentence.replace(number_bullet, '')

        # prevent short forms being splitted into separate tokens
        # Eg: පෙ.ව.
        for short_form in self.short_forms:
            representation = short_form[0:-1] + self.short_form_identifier
            sentence = sentence.replace(short_form, representation)

        parts = re.split(r'({})'.format(self.word_tokenizer_delims), sentence)
        tokens = [token.replace(self.short_form_identifier, '.') for token in parts if len(token.strip()) != 0]

        #replace numbers with ###
        i = 0
        for token in tokens:
            tokens[i] = self.clean_numbers(token)
            i += 1

        #remove punctuations
        new_tokens_without_punctionations = []
        for token in tokens:
            if(token not in self.punctuation_marks):
                new_tokens_without_punctionations.append(token)

        return new_tokens_without_punctionations

    def split_sentences(self, doc: Text, return_sinhala_only: Boolean = False) -> List[Text]:
        # remove ignoring chars from document
        for ignoring_char in self.ignoring_chars:
            if ignoring_char in doc:
                doc = doc.replace(ignoring_char, '')

        # stop words being present with a punctuation at start or end of the word
        # Eg: word?     word,
        if self.isolate_punctuations_with_spaces:  # default is set to FALSE
            for punctuation in self.punctuations_without_line_tokenizing_chars:
                doc = doc.replace(punctuation, ' ' + punctuation + ' ')

        # prevent short forms being splitted into sentences
        # Eg: පෙ.ව.
        for short_form in self.short_forms:
            representation = short_form[0:len(short_form) - 1] + self.short_form_identifier
            doc = doc.replace(short_form, representation)

        #remove text between parenthesis.
        parenthesis_text = re.findall(r'\([^()]+\)', doc)
        for text in parenthesis_text:
            if(len(text) < 40):
                doc = re.sub(r'\([^()]+\)', '', doc)

        #clean numbers
        # doc = self.clean_numbers(doc)

        sentences = []
        # split lines
        parts = re.split(r'{}'.format(self.line_tokenizer_delims), doc)

        for sentence in parts:
            sentence = sentence.replace(self.short_form_identifier, '.')
            sentence = sentence.strip()
            if contains_sinhala(sentence):  # filter empty sentences and non-sinhala sentences
                sentences.append(sentence)
            elif not return_sinhala_only and len(sentence) != 0:
                sentences.append(sentence)
        return sentences


# noinspection SpellCheckingInspection
class SinhalaTweetTokenizer(Tokenizer):
    def __init__(self):
        self.tokenizer = SinhalaTokenizer()
        self._special_chars = ['_']
        self._special_chars_map = str.maketrans({ord(c): '_{}'.format(c) for c in self._special_chars})
        self._var_type_pattern = {
            'hashtag': r'#\w+',
            'mention': r'@\w+',
            'url': r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
        }  # for creation of lookups

    def escape(self, string: Text) -> Tuple[Text, Dict[Text, Tuple[Text, Text]]]:
        """
        Escape special characters in a string.
        """
        lookup = {}
        string = string.translate(self._special_chars_map)
        var_id= 0
        for var_type, pattern in self._var_type_pattern.items():
            vals = re.findall(pattern, string)
            for v in vals:
                var, val = 'VAR_{}'.format(var_id), v
                lookup[var] = (val, var_type)
                string = string.replace(val, var)
                var_id += 1
        return string, lookup

    # noinspection PyMethodMayBeStatic
    def unescape(self, string: Text, lookup: Dict[Text, Tuple[Text, Text]]) -> Text:
        """
        UnEscape special characters in a string.
        """
        for var, val in lookup.items():
            string = string.replace(var, val[0])
        return re.sub(r'_(.)', r'\1', string)

    def tokenize(self, sentence: Text) -> List[Text]:
        """
        Tokenize the input sentence(tweet) and return `List[Text]` containing tokens.
        """
        sentence, lookup = self.escape(sentence)
        for e in emoji.UNICODE_EMOJI:
            if e in sentence:
                sentence = sentence.replace(e, ' {} '.format(e))
        sentence = re.sub(r'\xa0', ' ', sentence)
        sentence = re.sub(r' +', ' ', sentence)
        tokens = [self.unescape(token, lookup) for token in self.tokenizer.tokenize(sentence)]
        return tokens

    def split_sentences(self, doc: Text, return_sinhala_only: Boolean = False) -> List[Text]:
        doc, lookup = self.escape(doc)
        sentences = [self.unescape(token, lookup) for token in self.tokenizer.split_sentences(doc, return_sinhala_only)]
        return sentences
