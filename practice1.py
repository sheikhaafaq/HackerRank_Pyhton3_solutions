#practice1
dictionary = {
    "name" :"Aafaq",
    "age" : 20,
    "likes" :"python"
    }

def about(name,age,likes):
     sentence = "Meet {}, he/she is {} years old and he likes {}".format(name,age,likes)
     return sentence

x= about(**dictionary)
print(x)


def foo(**kwargs):
     for keys,values in kwargs.items():
          print("{}:{}".format(keys,values))

foo(**dictionary)
