import json
import  os
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



def load_files(input_path):
    """
    inputh
    :param input_path:
    :return:
    """
    files = os.listdir(input_path)
    lc_data = {}
    for file_name in files:
        if file_name.endswith("json"):
            with open(os.path.join(input_path, file_name), 'r', encoding='utf-8') as my_file:
                content = my_file.read()
                lc_collection_data = json.loads(content)
                entity_type = lc_collection_data["metadata"]["type"]
                data = lc_collection_data["data"]
                lc_data[entity_type] = data.copy()
    return lc_data


if __name__ == "__main__":
   pass


