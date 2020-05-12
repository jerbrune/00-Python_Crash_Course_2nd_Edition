class dog:
    """A simple attempt to model a dog"""

    def __init__(self, name, age):
        #une fonction dans une class est une "méthode"
        #la méthode __init__ démarre authomatiquemeent dès la création d'une instance "dog"
        #instance de la class dog est automatiquement passé comme argument avec l'argument self
        """Initialize name and age attributes"""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog seeting in response to a command"""
        print(f"{self.name} is now sitting")

    def roll_over(self):
        print(f"{self.name} rolled over !")
