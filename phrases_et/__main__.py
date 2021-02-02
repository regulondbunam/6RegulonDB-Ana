"""#

# name: __main__.py	Version [#.#]

## synopsis

```python
program_name lc_data, valid_path, invalid_path arguments
```

## examples

```python
put here your code example
```

## description
En este módulo se mandan

## arguments

*lc_data

*valid_path

*invalid_path

## requirements

Este modulo requiere de los argumentos declarados -i,-o-in, y un archivo json de entrada

## softwareRequirements
import os
import sys

from dotenv import load_dotenv

## memoryRequirements
[Minimum memory requirements]

## storageRequirements
2MB

* __Input Format - __ __[Name]__ Description es el archivo de entrada que corresponede al argumento -i
ri.json

## output

* __Format - PhrasesCollection Description archivo de salida que contendra las frases extraídas de ri.json

__Return:__

__Type -__  __[Name]__ Description

## [Program Code]

#"""


"""#

dateCreated: [YYYY-MM-DD] -  author: [name]

dateModified [YYYY-MM-DD] - contributor: [describe the modification]

#"""

import os
import sys

import identifiers_api

from dotenv import load_dotenv

from phrases_et.utils.file_handler import load_files
from phrases_et.utils.arguments import load_arguments
from phrases_et.utils import file_handler
from phrases_et.classes.Datasets import Datasets


def run(lc_data, valid_path, invalid_path):

    for filename, data in lc_data.items():
        dataset = Datasets(filename, data, valid_path, invalid_path)
        dataset.process_objects()
        #procesar,validar, escribir objetos validados, escribir objetos no validados


if __name__ == '__main__':
    load_dotenv()
    arguments = load_arguments()

    identifiers_user = os.getenv("IDENTIFIER_USER")
    identifiers_pass = os.getenv("IDENTIFIERS_PASS")
    multigenomic_user = os.getenv("MULTIGENOMIC_USER")
    multigenomic_pass = os.getenv("MULTIGENOMIC_PASS")

    input_path = arguments.inputdir

    lc_data = file_handler.load_files(input_path)

    #
    print(lc_data)
    identifiers_api.connect("mongodb://localhost:27017/")


    source_id = "TEMP5ccca9366e06251414ea6a2c"
    source_id = "REG0-6065"

    regulondb_id = identifiers_api.get_identifier_by(source_id, "ECOLI", "regulatoryinteractions")

    run(lc_data, valid_path="arguments.validdata", invalid_path="arguments.invaliddata")

    print("valor de regulondb_id", regulondb_id)

    if regulondb_id:
        print("Entro a procesar")
    else:
        print("archivos no registrados")


#print(f"User: {identifiers_user} Password: {identifiers_pass}")