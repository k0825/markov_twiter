import abc
from morph import is_keyword
from markov import Markov


class Responder(metaclass=abc.ABCMeta):
    def __init__(self, name):
        self._name = name

    @abc.abstractmethod
    def response(self, *args):
        pass

    @property
    def name(self):
        return self._name


class MarkovResponder(Responder):
    def response(self, parts):
        markov = Markov()
        keyword = next((w for w, p in parts if is_keyword(p)), '')
        response = markov.generate(keyword)
        return response
