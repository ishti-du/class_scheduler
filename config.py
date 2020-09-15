from .data import Data


class Config:
    __singletonConfig = None

    """
    Singleton Implementation take from:
    https://www.tutorialspoint.com/python_design_patterns/python_design_patterns_singleton.htm
    """

    @staticmethod
    def getInstance():
        if Config.__singletonConfig is None:
            Config()
        return Config.__singletonConfig

    def __init__(self):
        if Config.__singletonConfig is not None:
            raise Exception("This is a singleton class, cannot instantiate")
        else:
            self._POPULATION_SIZE = 9
            self._NUM_OF_ELITE_SCHEDULES = 1
            self._MUTATION_RATE = 0.1
            self._TOURNAMENT_SELECTION_SIZE = 3
            self._data = Data()
            Config.__singletonConfig = self

    def get_POPULATION_SIZE(self):
        return self._POPULATION_SIZE

    def get_NUM_OF_ELITE_SCHEDULES(self):
        return self._NUM_OF_ELITE_SCHEDULES

    def get_MUTATION_RATE(self):
        return self._MUTATION_RATE

    def get_TOURNAMENT_SELECTION_SIZE(self):
        return self._TOURNAMENT_SELECTION_SIZE

    def get_data(self):
        return self._data