import nltk 
from nltk.corpus import stopwords
nltk.download('stopwords') 

# we use the list of stop words that are downloaded from nltk lib.
stop_words = set(stopwords.words('english'))
# print('list of stop words:', stop_words)

def nlp_preprocessing(total_text, index, column):
    if type(total_text) is not int:
        string = ""
        for words in total_text.split():
            # remove the special chars in review like '"#$@!%^&*()_+-~?>< etc.
            word = ("".join(e for e in words if e.isalnum())) # Returns only words with (A-z) and (0-9)
            # Conver all letters to lower-case
            word = word.lower()
            # stop-word removal
            if not word in stop_words:
                string += word + " "
        data[column][index] = string 

# we take each title and we text-preprocess it.
for index, row in data.iterrows():
    nlp_preprocessing(row['product_name'], index, 'product_name') 

data.head() 
