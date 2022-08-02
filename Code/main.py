from flask import Flask, render_template, request
import Tokenization
import getUserTweets
import Performance
import Vectorization
import Test
app = Flask(__name__)
model,bow_Vectorization = Test.model_vect()
streamming_tweet = getUserTweets.public_tweets()
streamming_tweet.append("sad")
import json

data = {"Eleven": "Millie",
        "Mike": "Finn",
        "Will": "Noah"}

with open('app.json', 'w') as f:
    json.dump(data, f)
i=-1

@app.route('/', methods=["GET","POST"])
def main():
    if request.method=="POST":
        inp=[request.form.get("inp")]
        print((type(inp)))
        print(inp)
        check=Tokenization.clean_tweet(inp)
        print(check)
        check=bow_Vectorization.transform(check).toarray()
        print(check)
        y_pred = model.predict(check)
        if y_pred ==1:
            return render_template('home.html',message="😔💔🥺",value=streamming_tweet)
        else:
            return render_template('home.html',message="😃😍😝")
    return render_template('home.html')



@app.route('/home2', methods=["GET","POST"])
def main_tweet():
    if request.method=="POST":
        inp=request.form.get("inp")
        inp1 = request.form.get("inp1")
        inp1=int(inp1)
        data = streamming_tweet[inp1]
        check = [data]
        check=Tokenization.clean_tweet(check)
        print(check)
        check=bow_Vectorization.transform(check).toarray()
        print(check)
        y_pred = model.predict(check)

        if y_pred ==1:
            return render_template('home2.html',message="😔💔🥺",value=data,index=inp1)
        else:
            return render_template('home2.html',message="😃😍😝",value=data,index=inp1)
    return render_template('home2.html',value=streamming_tweet[0],index=0)

#set FLASK_APP=main.py
#set FLASK_ENV=development
#flask run
