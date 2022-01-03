from flask import Flask, request, render_template, send_from_directory
import os
import functions

POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route("/")
def page_index():
    json_data = functions.read_json("posts.json")

    tags = functions.tags(json_data)

    return render_template("index.html", tags=tags)


@app.route("/tag")
def page_tag():
    json_data = functions.read_json("posts.json")

    tag = request.args["tag"]
    taged_posts = functions.tag_search(json_data, tag)

    return render_template("post_by_tag.html", posts=taged_posts, tag=tag)


@app.route("/post", methods=["GET", "POST"])
def page_post_create():
    if request.method == "GET":
        return render_template("post_form.html")
    if request.method == "POST":
        json_data = functions.read_json("posts.json")

        # Работа с файлом и проверка его наличия
        file = request.files['picture']
        if file.filename == '':
            return 'Ошибка загрузки'
        # Сохранение файла в папку /uploads/images
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))

        # Работа с текстом и проверка его наличия
        new_content = request.form.get("content")
        if new_content == "":
            return "Ошибка загрузки"

        # Формирование данных о загруженном посте
        post = {
            "pic": os.path.join(app.config['UPLOAD_FOLDER'], file.filename),
            "content": new_content
        }
        json_data.append(post)

        # Запись в файл posts.json нового поста
        functions.write_json("posts.json", json_data)

        return render_template("post_uploaded.html", new_post=post)


@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


app.run(debug=True)
