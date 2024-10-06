def person(**info):
    for key, value in info.items():
        print(f"{key} is {value}")

person(name = "An", age = "18")