from flask import Blueprint, render_template, request
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

from .models import User
from .basilica_service import connection as basilica_connection

stats_routes = Blueprint("stats_routes", __name__)

@stats_routes.route("/stats/iris")
def iris():
    # train the model (on the fly, in real-time):
    X, y = load_iris(return_X_y=True)
    clf = LogisticRegression(random_state=0, solver="lbfgs", multi_class="multinomial").fit(X, y)
    # make a prediction:
    results = str(clf.predict(X[:2, :]))
    return results

@stats_routes.route("/")
def twitoff_prediction_form():
    return render_template("prediction_form.html")

@stats_routes.route("/stats/predict", methods=["POST"])
def twitoff_prediction():
    print("FORM DATA:", dict(request.form))
    screen_name_a = request.form["screen_name_a"]
    screen_name_b = request.form["screen_name_b"]
    tweet_text = request.form["tweet_text"]
    
    #
    # TRAIN THE MODEL
    #
    # inputs: embeddings for each tweet
    # labels: screen name for each tweet

    model = RandomForestClassifier(random_state=42,max_depth = 16,min_samples_leaf = 14,
              min_samples_split=8)

    user_a = User.query.filter(User.screen_name == screen_name_a).one()
    user_b = User.query.filter(User.screen_name == screen_name_b).one()

    user_a_tweets = user_a.tweets
    user_b_tweets = user_b.tweets

    embeddings = [] # wrapping in a list to make an array
    labels = []
    all_tweets = user_a_tweets + user_b_tweets
    for tweet in all_tweets:
        embeddings.append(tweet.embedding)     # embedding are our x
        labels.append(tweet.user.screen_name) # labels are our y

    model.fit(embeddings, labels) 
    
    #
    # MAKE PREDICTION
    #
   
    example_embedding = basilica_connection.embed_sentence(tweet_text, model="twitter")
    result = model.predict([example_embedding])
    print(result)
    maj_clss = max(set(labels), key=labels.count)
    y_pred = [maj_clss] * len(embeddings)
    #predictions = [(value) for value in y_pred]
    screen_name_most_likely = result[0]
    predictionr = [screen_name_most_likely] * len(embeddings)
    acc = accuracy_score(y_pred,predictionr)

    return render_template("prediction_results.html",
    screen_name_a=screen_name_a,
    screen_name_b=screen_name_b,
    screen_name_most_likely = screen_name_most_likely,
    tweet_text = tweet_text,
    acc = acc,
    result = result
    
    )
