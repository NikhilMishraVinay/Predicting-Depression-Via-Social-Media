from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer

def bow_vectorizer(lem):
    bow_vectorizer = CountVectorizer(max_df=0.90, min_df=2, max_features=4500, stop_words='english')
    bow = bow_vectorizer.fit_transform(lem).toarray()
    return [bow,bow_vectorizer]
def tfidf_vectorizer(lem):
    tfidf_vectorizer = TfidfVectorizer(max_df=0.90, min_df=2, max_features=3500, stop_words='english')
    tfidf = tfidf_vectorizer.fit_transform(lem).toarray()
    return [tfidf,tfidf_vectorizer]
# def userTweet(tweet):
#      tfidf_vectorizer = TfidfVectorizer(max_df=0.90, min_df=2, max_features=3500, stop_words='english')
#      return tfidf_vectorizer.transform(tweet).toarray()