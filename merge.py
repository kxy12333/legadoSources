import os

if os.path.exists("./merge"):
    os.remove("./merge")
merge = open("./merge", 'a+', encoding='utf-8')
for root, dirs, files in os.walk("./sources"):
    for file in files:
        f = open(os.path.join(root, file), "r", encoding='utf-8')
        merge.write(f.read())
