import inspect
from abc import ABCMeta, abstractmethod


class TimeSeriesFeature(metaclass=ABCMeta):
    def __repr__(self):
        constructor_attributes = inspect.getfullargspec(self.__init__).args
        attributes_to_print = [str(getattr(self, attribute)) for attribute in constructor_attributes
                               if attribute in self.__dict__]
        return f'{self.__class__.__name__}({", ".join(attributes_to_print)})'

    @abstractmethod
    def fit_transform(self, time_series):
        pass