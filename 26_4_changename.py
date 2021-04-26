oldname =  "new.txt"
newname="rename.txt"
with open(oldname) as f:
    content = f.read()

    with open(newname,"w") as f:
        f.write(content)

    