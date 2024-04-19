import requests

# URL base de la API
base_url = "https://jsonplaceholder.typicode.com"


# Endpoint al que queremos hacer la solicitud (por ejemplo, obtener la lista de usuarios)
endpoint = "/users"

# URL completa
url = base_url + endpoint

# Realizar la solicitud GET
print("Realizando Petición....")
response = requests.get(url)

# Comprobar si la solicitud fue exitosa (código de estado 200)
if response.status_code == 200:
    # Obtener los datos de respuesta en formato JSON
    print("Se obtuvo los datos...")
    data = response.json()
    # Imprimir los datos obtenidos
    print("Datos de usuarios:")
    with open("archivo.txt", "w") as file:
        for user in data:
            print(f"ID: {user['id']}, Nombre: {user['name']}, Email: {user['email']}")
            file.write(
                f"ID: {user['id']}, Nombre: {user['name']}, Email: {user['email']}\n"
            )
else:
    print("La solicitud falló. Código de estado:", response.status_code)
