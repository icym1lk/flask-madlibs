from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import story, story2, story3, story4

app = Flask(__name__)
app.config["SECRET_KEY"] = "passphrase"
debug = DebugToolbarExtension(app)

@app.route("/")
def index():
    first_word = story.prompts[0]
    second_word = story.prompts[1]
    third_word = story.prompts[2]
    fourth_word = story.prompts[3]
    fifth_word = story.prompts[4]
    return render_template("index.html", first_word=first_word, second_word=second_word, third_word=third_word, 
    fourth_word=fourth_word, fifth_word=fifth_word)

@app.route("/story")
def story_page():
    first_word = request.args["first_word"]
    second_word = request.args["second_word"]
    third_word = request.args["third_word"]
    fourth_word = request.args["fourth_word"]
    fifth_word = request.args["fifth_word"]
    template = request.args["template"]

    response = {}
    ans = [first_word, second_word, third_word, fourth_word, fifth_word]

    for i in range(0,5):
        response[story.prompts[i]] = ans[i]

    if template == "1":
        newStory = story.generate(response)
    elif template == "2":
        newStory = story2.generate(response)
    elif template == "3":
        newStory = story3.generate(response)
    elif template == "4":
        newStory = story4.generate(response)

    return render_template("story.html", newStory=newStory, template=template)