"""# **Importing Essential libraries of nltk**


"""

from nltk.tokenize import word_tokenize
import re
from nltk.corpus import stopwords
from nltk.stem import regexp
from nltk.stem.wordnet import WordNetLemmatizer

"""# **Function for Natural language processing pipeline**"""

def clean_tweet(tweet_data):
    new_tweet = []
    for tweet in tweet_data:
        new_tweet.append(str.lower(tweet))
    # splitting a phrase, sentence, paragraph, or an entire text document into smaller units, such as individual
    # words or terms
    tokens = [word_tokenize(i) for i in new_tweet]
    reg_exp = []
    for word in tokens:
        clean = []
        for w in word:
            # Convert into regular expression
            res = re.sub(r'[^\w\s]', "", w)
            if res != "":
                clean.append(res)
        reg_exp.append(clean)
    imp_data = []
    for word in reg_exp:
        clean = []
        for w in word:
            # eliminate unimportant words, allowing applications to focus on the important words instead.
            if w not in stopwords.words('english'):
                clean.append(w)
        imp_data.append(clean)
        # Lemmitize the tweets
    wnet = WordNetLemmatizer()
    lem = []
    for words in imp_data:
        clean = ""
        flag = 0
        for w in words:
            if flag == 0:
                clean = clean + wnet.lemmatize(w)
                flag = 1
            else:
                clean = clean + " " + wnet.lemmatize(w)
        lem.append(clean)
    return lem;
