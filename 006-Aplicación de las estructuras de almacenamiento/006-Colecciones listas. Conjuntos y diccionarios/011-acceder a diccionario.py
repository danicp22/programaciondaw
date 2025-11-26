persona = {
    "nombre":"Daniel",
    "apellidos":"Calve Pardo",
    "correo":"daniel@example.com",
    "edad":18,
    "telefonos":[
        {
            "tipo":"fijo",
            "numero":96738948
        },
        {
            "tipo":"movil",
            "numero":68576895
        }
    ]
}

print(persona)
print(persona["telefonos"][0]["numero"])