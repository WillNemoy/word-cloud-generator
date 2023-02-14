test_string = "Enter text here. The word cloud generator will extract noun phrases with two or more words. This parameter was chosen as it strikes a good balance between insightfulness and restrictiveness."

remove_text = " dsffs {random son} {i dont} dwadse {34}"

##from spacy.lang.en import English
#import spacy
#nlp = spacy.load("en_core_web_sm")
##nlp = English()

#!!!IDEAS: remove stop words at the beginning and end of phrases
#!!!Currently not removing 1-grams

import spacy
nlp = spacy.load("en_core_web_sm")
import en_core_web_sm
nlp = en_core_web_sm.load()

import re

import pandas as pd
import numpy as np

#https://stackoverflow.com/questions/33289820/noun-phrases-with-spacy
def word_cloud_generator(text, remove_text):
        
    #get the noun phrases to remove
    #https://stackoverflow.com/questions/38999344/extract-string-within-parentheses-python
    remove_phrases = re.findall('\{([^}]+)', remove_text)        

    # Using filter() and lambda function to filter out punctuation characters
    def remove_punctuation(text):
        result = ''.join(filter(lambda x: x.isalpha() or x.isdigit() or x.isspace(), str(text)))
        return result

    #remove punctutation
    text = remove_punctuation(text)
    
    #create SpaCy object
    text = nlp(text)

    #select noun phrases
    for np in text.noun_chunks:
        print(np.text)
        
    
    noun_phrases = []
    noun_phrases_count = []
    """
    #only return noun phrases with at least 2 words
    for phrase in txtBlob:
            if (" " in phrase) and not (phrase in remove_phrases):
                noun_phrases.append(phrase)
                
    #get the count of noun phrases
    for noun_phrase in noun_phrases:
        noun_phrase_count = str(txtBlob).count(noun_phrase)
        noun_phrases_count.append(noun_phrase_count)
  
    word_cloud_data = {'x': noun_phrases, "value": noun_phrases_count}

    # Create the DataFrame
    df = pd.DataFrame(word_cloud_data)
    df = df.drop_duplicates()
    df = df.sort_values(by="value", ascending=False)

    if len(df) >= 20:
        #must be iloc as the index was not reset
        df = df.iloc[0:20]
                
    return df
    """

output = word_cloud_generator(test_string, remove_text)
print(output)