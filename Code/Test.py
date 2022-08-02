import re  # for regular expressions
import pandas as pd  # For analyze data
import numpy as np  # for working with arrays
import Tokenization
#import getUserTweets
import Performance
import Vectorization
import model
"""# Upload .CSV file"""
def model_vect():

    data = pd.read_csv("./file.csv")  # read csv file

    data.info()

    """# **Drop Unnecessary Columns**"""

    data.drop(data.columns[14:], axis=1, inplace=True)

    data.drop(data.columns[7:13], axis=1, inplace=True)

    data.drop(data.columns[1:6], axis=1, inplace=True)

    data.info()

    """# **Drop that rows in which null is present**"""

    data = data.dropna()  # drop that row in which null value is present

    data.info()

    """# **Set of different types of tweets**"""

    depression = set()
    for i in data['name']:
        depression.add(i)

    """# **Print Different types of tweets**"""

    depression

    """# List of sad tweets"""

    depression_list = ['Abby',
                       'Depressed Quotes',
                       'Depression Quotes',
                       'Depression Quotes™➰',
                       'so sad today']

    """# Label the tweets 
       if sad/Depressed then true
      otherwise labelled it as false
    
    """

    depression_status = []
    for status in data['name']:
        if status in depression_list:
            depression_status.append(True)
        else:
            depression_status.append(False)

    df = data.drop(data.columns[2:], axis=1)

    """# Add a new colomn named as 'label'"""

    df['label'] = depression_status

    """# Count the negative and positive tweets"""

    df["label"].value_counts()

    """# Eleminates specials characters and numbers from tweets"""


    def remove_pattern(input_txt, pattern):
        r = re.findall(pattern, input_txt)
        for i in r:
            input_txt = re.sub(i, '', input_txt)

        return input_txt

    df['tidy_tweet'] = np.vectorize(remove_pattern)(df['tweet'], "@[\w]*")
    df.head()

    df['tidy_tweet'] = df['tidy_tweet'].str.replace("[^a-zA-Z#]", " ", regex=True)
    df.head(10)

    """# Remove that word which length less than three"""


    df['tidy_tweet'] = df['tidy_tweet'].apply(lambda x: ' '.join([w for w in x.split() if len(w) > 2]))

    df.head(10)

    """# **Call cleaned_tweet Function**"""
    cleaned_tweet = Tokenization.clean_tweet(df['tidy_tweet'])
    df["cleaned_tweet"] = cleaned_tweet

    tokenized_tweet = df['cleaned_tweet'].apply(lambda x: x.split())  # tokenizing

    x,bow_Vectorization = Vectorization.bow_vectorizer(df['cleaned_tweet'])

    y = depression_status

    from sklearn.preprocessing import LabelEncoder  # For label Encoding

    y = LabelEncoder().fit_transform(y)
    y

    from sklearn.model_selection import train_test_split

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2,
                                                        random_state=1)  # split the data set into train and test
    model1=model.classifier(x_train,y_train)
    y_pred = model1.predict(x_test)
    print(y_pred)

    Performance.confusionMatrix(y_test, y_pred)

    Performance.perfection(y_test, y_pred)

    return [model1,bow_Vectorization]


