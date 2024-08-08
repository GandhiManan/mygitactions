def hello():
    print("Inside Function 1")
    hello2()


def hello2():
    print("Inside Function 2")

if __name__ == "main":
  hello()
