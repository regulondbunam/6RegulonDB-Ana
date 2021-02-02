
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








import os
import json


import identifiers_api
from phrases_et.classes.Document import Document


class Datasets(object):

    def __init__(self, file_name, data, valid_path, invalid_path):
        """

        :param kwargs:
        """
        self.filename = file_name
        self.data = data
        self.valid_path = valid_path
        self.invalid_path = invalid_path
        self.valid_objects = []
        self.invalid_objects = []

    @property
    def filename(self):

        return self._filename

    @filename.setter
    def filename(self, file_name):
        self._filename = file_name

    @property
    def valid_path(self):
        return self._valid_path

    @valid_path.setter
    def valid_path(self, valid_path):
        self._valid_path = valid_path

    @property
    def invalid_path(self):
        return self._invalid_path

    @invalid_path.setter
    def invalid_path(self, invalid_path):
        self._invalid_path = invalid_path

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        self._data = data

    @property
    def valid_objects(self):
        return self._valid_objects

    @valid_objects.setter
    def valid_objects(self, valid_objects):
        self._valid_objects = valid_objects

    @property
    def invalid_objects(self):
        return self.invalid_objects

    @invalid_objects.setter
    def invalid_objects(self, invalid_objects):
        self._invalid_objects = invalid_objects

    @staticmethod
    def write_file(file_path, file_name, data):  # no necesariamente es la ruta
        """

        :param filename: # mi_ruta_de_salida/datos_validos/mi_archivo.json
        :param data: contiene todos los json procesos
        :return:
        """
        # Aqui ira mi codigo para crear archivo
        with open(os.path.join(file_path, file_name), 'w', encoding='utf-8') as fp:
            json.dump(data, fp, indent=2)

    def process_objects(self):

     for lc_object in self.data:
         for lc_id, lc_object_data in lc_object.items():
             regulondb_id = "TEMP5ccca9366e06251414ea6a2c"
             # identifiers_api.get_id(lc_id)
             if regulondb_id is not None:
                 data = lc_object_data["data"]
                 source_id = lc_object_data["sources"]

                 document = Document(lc_id, regulondb_id, data, source_id)
                 document.process_sources(lc_id, regulondb_id, data, source_id)

