class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(self.name, self.age)


# main method
if __name__  == "__main__":
    p = Person("Abdul", 20)
    p.show()

    # modifying class object
    # p.name = "Waheed"
    # p.show()

    # deleting object properties
    # del p.name
    # p.show() # now it throw an error saying it has no such instance

    # deleting object itself
    # del p
    
