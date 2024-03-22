class Guitar:
    """Represent a guitar object."""

    def __init__(self, name="", year=0, cost=0):
        """Initialise a Guitar instance.

        :param name: str. Name of guitar.
        :param year: int. Year of guitar made.
        :param cost: float. Cost of guitar
        """
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string.

        :return: f'{self.name} ({self.year}) : ${self.cost}'
        """
        return f'{self.name} ({self.year}) : ${self.cost}'
