import argparse


def load_arguments():
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter,
                                     description="Argumentos",
                                     epilog="")

    parser.add_argument(
        "-i", "--inputdir",
        help='Directorio de entrada de los archivos JSON de la base de datos Lisen&Curate'
    )
    parser.add_argument(
        "-o", "--validdata",
        help="Directorio que contiene los datos que han sido validos"
    )
    parser.add_argument(
        "-i", "--invaliddata",
        help='Directorio que contiene los  datos que fueron no validos'
    )
    parser.add_argument(
        "-l", "--log",
        help='Directorio que contiene el porque fueron invalidos los datos'
    )
    return parser.parse_args()


    args = parser.parse_args()
    print("Hola %$", )