# Importa las clases y funciones del sistema
from reservation_system import Hotel, Customer, Reservation, read_file

# Verifica los datos iniciales
print("Hoteles:")
hotels = read_file("hotels.json")
print(hotels)

print("\nClientes:")
customers = read_file("customers.json")
print(customers)

print("\nReservaciones:")
reservations = read_file("reservations.json")
print(reservations)

# Crear un nuevo hotel
print("\nCreando un nuevo hotel...")
Hotel.create_hotel(3, "Mountain Lodge", "Denver", 50)

# Verificar que el hotel se haya agregado
print("\nHoteles actualizados:")
hotels = read_file("hotels.json")
print(hotels)

# Crear un cliente nuevo
print("\nCreando un nuevo cliente...")
Customer.create_customer(3, "Alice Johnson", "alice@example.com")

# Verificar clientes actualizados
print("\nClientes actualizados:")
customers = read_file("customers.json")
print(customers)

# Crear una nueva reservación
print("\nCreando una nueva reservación...")
Reservation.create_reservation(3, 3, 3, 25)

# Verificar reservaciones actualizadas
print("\nReservaciones actualizadas:")
reservations = read_file("reservations.json")
print(reservations)

# Cancelar una reservación
print("\nCancelando la reservación con ID 1...")
Reservation.cancel_reservation(1)

# Verificar reservaciones actualizadas
print("\nReservaciones después de la cancelación:")
reservations = read_file("reservations.json")
print(reservations)
