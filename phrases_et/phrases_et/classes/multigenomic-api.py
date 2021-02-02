

import identifiers_api


identifiers_api.connect("mongodb://localhost:27017/")

source_id = "TEMP5ccca9366e06251414ea6a2c"
#source_id = "|REG0-5991|"
regulondb_id = identifiers_api.get_identifier_by(source_id, "ECOLI", "regulatoryinteractions")

print("valor de regulondb_id", regulondb_id)

if regulondb_id:
    print("Entro a procesar")
else:
    print("archivos no registrados")