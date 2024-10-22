import os

if os.path.exists("./merge.json"):
    os.remove("./merge.json")
merge = open("./merge.json", 'a+', encoding='utf-8')
merge.write('[')
for root, dirs, files in os.walk("./sources"):
    for file in files:
        f = open(os.path.join(root, file), "r", encoding='utf-8')
        merge.write(f.read())
        if file != files[-1]:
            merge.write(',')
merge.write(']')
