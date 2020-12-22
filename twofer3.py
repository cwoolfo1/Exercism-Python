class twofer3:
    def twofer(name):
        if name is None:
            name = "you"
        return "One for "+name+", one for me"
    print(twofer(input("enter a name: ")))