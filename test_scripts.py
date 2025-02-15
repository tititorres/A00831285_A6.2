import os
import json

def create_json_file_with_data(filename, data):
    """Crea un archivo JSON con datos iniciales."""
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

def generate_test_files_with_data():
    """Genera los archivos JSON necesarios con datos iniciales."""
    files_with_data = {
        "hotels.json": [
            {"hotel_id": 1, "name": "Hotel Paradise", "location": "New York", "rooms": 100},
            {"hotel_id": 2, "name": "Ocean View Resort", "location": "Miami", "rooms": 200}
        ],
        "customers.json": [
            {"customer_id": 1, "name": "John Doe", "email": "john@example.com"},
            {"customer_id": 2, "name": "Jane Smith", "email": "jane@example.com"}
        ],
        "reservations.json": [
            {"reservation_id": 1, "customer_id": 1, "hotel_id": 1, "room_number": 50},
            {"reservation_id": 2, "customer_id": 2, "hotel_id": 2, "room_number": 100}
        ]
    }

    for filename, data in files_with_data.items():
        if not os.path.exists(filename):
            create_json_file_with_data(filename, data)
            print(f"Archivo {filename} creado con datos iniciales.")
        else:
            print(f"Archivo {filename} ya existe.")

if __name__ == "__main__":
    generate_test_files_with_data()
