 try:
 open("mars.jpg")
 except FileNotFoundError as err:
     print("got a problem trying to read the file:", err)

got a problem trying to read the file: [Errno 2] No such file or directory: 'mars.jpg'
