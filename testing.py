import json

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

print(match)

# tag = input("введите тэг")
# tag = "#" + tag
#
# with open("posts.json", encoding="utf-8") as f:
#     raw_json = json.load(f)
# tag_post = []
# for post in raw_json:
#     if tag in post["content"]:
#         tag_post.append(post)
#
# print(tag_post)

with open("posts.json", encoding="utf-8") as f:
    raw_json = json.load(f)
post = {
    "pic": "test",
    "content": "text"
}
raw_json.append(post)

print(raw_json)