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





from phrases_et.classes.Property import Property

class Document(object):

    def __init__(self, lc_id, regulondb_id, properties, source_id):
        self.lc_id = lc_id #source_id
        self.regulondb_id = regulondb_id #id
        self.properties = properties
        self.source_id = source_id
        self.__raw_properties = [] #No puede ser acedida desde el exterior de esta clase
        self.processed_properties = []
        self.sources = {}
        self.properties_map = {}
        self.regulondb_data = {}

    @property
    def lc_id(self):
        return self._lc_id

    @lc_id.setter
    def lc_id(self, lc_id):
        self._lc_id = lc_id

    @property
    def regulondb_id(self):
        return self._regulondb_id

    @regulondb_id.setter
    def regulondb_id(self, regulondb_id):
        self._regulondb_id = regulondb_id

    @property
    def properties(self):
        return self._properties

    @properties.setter
    def properties(self, properties):
        self._properties = properties

    @property
    def sources(self):
        return self._sources

    @sources.setter
    def sources(self, sources):
        self._sources = sources

    @property
    def _raw_properties(self):
        return self.__raw_properties

    @_raw_properties.setter
    def _raw_properties(self, raw_properties):
        self._raw_properties = raw_properties

    @property
    def processed_properties(self):
        return self._processed_properties

    @processed_properties.setter
    def processed_properties(self, processed_properties):
        self._processed_properties = processed_properties


    def regulondb_data(self):
        pass

    def process_sources(self,lc_id,regulondb_id,data,sources):
        pass
    
       # print(lc_id, regulondb_id, data, sources)
       # property.regulondb_name(lc_id, regulondb_id, data, sources)
        #for source in self.sources:
         #   for key,value in source.iteritems():
         #       source_name = {key,value}
          #  print(source_name)#




