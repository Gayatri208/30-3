with open('new.txt') as f:
    content = f.read()

    content = content.replace("hello","ggg")
  with open('new.txt','w') as f:
      f.write(content) 
  