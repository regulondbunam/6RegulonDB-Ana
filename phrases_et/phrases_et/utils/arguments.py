import argparse

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


def load_arguments():
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter,
                                     description="Argumentos",
                                     epilog="Consulta de argumentos")

    parser.add_argument(
        "-i", "--inputdir",
        help='Directorio de entrada de los archivos JSON de la base de datos Lisen&Curate',
        required=True

    )
    parser.add_argument(
        "-o", "--validdata",
        help="Directorio que contiene los datos que han sido validos",
        required=False,
        dest='valid_path'
    )
    parser.add_argument(
        "-inv", "--invaliddata",
        help='Directorio que contiene los  datos que fueron no validos',
        required=False,
        dest='invalid_path'

    )
    parser.add_argument(
        "-l", "--log",
        help='Directorio que contiene el porque fueron invalidos los datos',
        required=False
    )


    arguments = parser.parse_args()

    return arguments
