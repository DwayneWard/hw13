from flask import Flask, request, render_template, send_from_directory
import json
import os

# from functions import ...

POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route("/")
def page_index():
    # В функцию
    with open("posts.json", encoding="utf-8") as f:
        raw_json = json.load(f)

    match = []
    for post in raw_json:
        text = post["content"].split(" ")
        for word in text:
            if "#" in word:
                tag = word.replace("#", "")
                tag = tag.replace("!", "")
                match.append(tag)
    match = set(match)
    #

    return render_template("index.html", tags=match)


@app.route("/tag")
def page_tag():
    tag = request.args["tag"]
    tag = "#" + tag

    with open("posts.json", encoding="utf-8") as f:
        raw_json = json.load(f)
    tag_post = []
    for post in raw_json:
        if tag in post["content"]:
            tag_post.append(post)

    return render_template("post_by_tag.html", posts=tag_post)


@app.route("/post", methods=["GET", "POST"])
def page_post_create():
    if request.method == "GET":
        return render_template("post_form.html")
    if request.method == "POST":

        file = request.files['picture']
        if file.filename == '':
            return 'No selected file'

        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))

        with open("posts.json", encoding="utf-8") as f:
            raw_json = json.load(f)
        post = {
            "pic": "/uploads/images/...",  # Как указать тут динамический путь?
            "content": request.form.get("content")
        }
        raw_json.append(post)

        with open("posts.json", "w") as f:
            json.dump(raw_json, f)

        return render_template("post_uploaded.html", new_post=post)


@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


app.run(debug=True)
