import spacy
nlp = spacy.load("zh_core_web_sm")
text = "北京是中国的首都"
doc = nlp(text)
for token in doc:
    print(token.text, token.pos_, token.dep_)