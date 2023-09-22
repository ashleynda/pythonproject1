from translate import Translator

text = "South-korea is beautiful"
translator = Translator(to_lang='ja')
translation = translator.translate(text)
print(translation)

