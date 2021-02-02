"""#

### load_arguments

__description:__

 Define y retorna los argumentos a utilizar por el programa principal

__usage:__

```python

load_arguments()

```

__return:__

* __ArgumentParser - __ __arguments__

__exception:__

*__Category (Error, Warning or Message)__ [Description of the exception ()]

#"""







class Property(object):

    def __init__(self, _source_name, regulondb_name, regulondb_value, phrases, **kwargs):
        self._source_name = _source_name
        self.regulondb_name = regulondb_name
        self.regulondb_value = kwargs.get("value", "objeto", None)
        self.phrases = []

    def regulondb_name(self):
        return self._regulondb_name

    #@regulondb_name.setter #a(b)...c
    def regulondb_name(self, source_name, **kwargs):
        pass
        #self.__source_name = source_name




