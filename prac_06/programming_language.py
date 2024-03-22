class ProgrammingLanguage:
    """Represent a language object."""

    def __init__(self, name="", typing="", reflection=bool, year=0):
        """Initialise a ProgrammingLanguage instance.
        name: str. Programming Language name.
        typing: str. Typing of Programming Language.
        reflection: bool. Programming Language is reflection or not.
        year: int. The year of Programming Language published.
        """
        self.name = name
        self.type = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        if self.type == "Dynamic":
            return True
        else:
            return False
