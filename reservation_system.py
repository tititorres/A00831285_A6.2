"""
Hotel Reservation System

This module implements a hotel reservation system with classes for managing
hotels, customers, and reservations. It includes functionality to create,
modify, and delete these entities, as well as persisting data in JSON files.
"""

import os
import json
import unittest


# Helper function for file handling
def read_file(filename):
    """Reads data from JSON file and returns a list. Handles invalid data"""
    if not os.path.exists(filename):
        return []
    with open(filename, "r", encoding="utf-8") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            print(f"Error: Invalid data in {filename}")
            return []


def write_file(filename, data):
    """Writes data to a JSON file."""
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


class Hotel:
    """Represents a hotel with attributes and methods to manage hotel data."""

    def __init__(self, hotel_id, name, location, rooms):
        self.hotel_id = hotel_id
        self.name = name
        self.location = location
        self.rooms = rooms

    @staticmethod
    def create_hotel(hotel_id, name, location, rooms):
        """Creates a new hotel and saves it to the JSON file."""
        hotels = read_file("hotels.json")
        if any(hotel["hotel_id"] == hotel_id for hotel in hotels):
            print("Error: Hotel ID already exists.")
            return
        hotels.append({
            "hotel_id": hotel_id,
            "name": name,
            "location": location,
            "rooms": rooms
        })
        write_file("hotels.json", hotels)

    @staticmethod
    def delete_hotel(hotel_id):
        """Deletes a hotel from the JSON file by its ID."""
        hotels = read_file("hotels.json")
        hotels = [
            hotel for hotel in hotels if hotel["hotel_id"] != hotel_id
        ]
        write_file("hotels.json", hotels)

    @staticmethod
    def display_hotel_info(hotel_id):
        """Displays information about a specific hotel."""
        hotels = read_file("hotels.json")
        hotel = next(
            (hotel for hotel in hotels if hotel["hotel_id"] == hotel_id),
            None
        )
        if hotel:
            print(hotel)
        else:
            print("Hotel not found.")

    @staticmethod
    def modify_hotel_info(hotel_id, **kwargs):
        """Modifies information about a specific hotel."""
        hotels = read_file("hotels.json")
        for hotel in hotels:
            if hotel["hotel_id"] == hotel_id:
                hotel.update(kwargs)
                break
        else:
            print("Hotel not found.")
        write_file("hotels.json", hotels)


class Customer:
    """Represents a customer with attributes and methods"""

    def __init__(self, customer_id, name, email):
        self.customer_id = customer_id
        self.name = name
        self.email = email

    @staticmethod
    def create_customer(customer_id, name, email):
        """Creates a new customer and saves it to the JSON file."""
        customers = read_file("customers.json")
        if any(c["customer_id"] == customer_id for c in customers):
            print("Error: Customer ID already exists.")
            return
        customers.append({
            "customer_id": customer_id,
            "name": name,
            "email": email
        })
        write_file("customers.json", customers)

    @staticmethod
    def delete_customer(customer_id):
        """Deletes a customer from the JSON file by their ID."""
        customers = read_file("customers.json")
        customers = [
            customer for customer in customers
            if customer["customer_id"] != customer_id
        ]
        write_file("customers.json", customers)

    @staticmethod
    def display_customer_info(customer_id):
        """Displays information about a specific customer."""
        customers = read_file("customers.json")
        customer = next(
            (c for c in customers if c["customer_id"] == customer_id),
            None
        )
        if customer:
            print(customer)
        else:
            print("Customer not found.")

    @staticmethod
    def modify_customer_info(customer_id, **kwargs):
        """Modifies information about a specific customer."""
        customers = read_file("customers.json")
        for customer in customers:
            if customer["customer_id"] == customer_id:
                customer.update(kwargs)
                break
        else:
            print("Customer not found.")
        write_file("customers.json", customers)


class Reservation:
    """Represents a reservation with attributes and methods"""

    def __init__(self, reservation_id, customer_id, hotel_id, room_number):
        self.reservation_id = reservation_id
        self.customer_id = customer_id
        self.hotel_id = hotel_id
        self.room_number = room_number

    @staticmethod
    def create_reservation(reservation_id, customer_id, hotel_id, room_number):
        """Creates a new reservation and saves it to the JSON file."""
        reservations = read_file("reservations.json")
        hotels = read_file("hotels.json")
        customers = read_file("customers.json")

        if not any(c["customer_id"] == customer_id for c in customers):
            print("Error: Customer does not exist.")
            return

        hotel = next(
            (h for h in hotels if h["hotel_id"] == hotel_id),
            None
        )
        if not hotel or room_number > hotel["rooms"]:
            print("Error: Invalid hotel or room number.")
            return

        reservations.append({
            "reservation_id": reservation_id,
            "customer_id": customer_id,
            "hotel_id": hotel_id,
            "room_number": room_number
        })
        write_file("reservations.json", reservations)

    @staticmethod
    def cancel_reservation(reservation_id):
        """Cancels an existing reservation by its ID."""
        reservations = read_file("reservations.json")
        reservations = [
            r for r in reservations
            if r["reservation_id"] != reservation_id
        ]
        write_file("reservations.json", reservations)


class TestHotelManagement(unittest.TestCase):
    """Unit tests for the Hotel Management System."""

    def setUp(self):
        """Sets up a clean environment for each test by clearing JSON files."""
        for filename in [
            "hotels.json",
            "customers.json",
            "reservations.json"
        ]:
            write_file(filename, [])

    def test_create_hotel(self):
        """Tests the creation of a hotel."""
        Hotel.create_hotel(1, "Hotel Paradise", "New York", 100)
        hotels = read_file("hotels.json")
        self.assertEqual(len(hotels), 1)
        self.assertEqual(hotels[0]["name"], "Hotel Paradise")

    def test_create_customer(self):
        """Tests the creation of a customer."""
        Customer.create_customer(1, "John Doe", "john@example.com")
        customers = read_file("customers.json")
        self.assertEqual(len(customers), 1)
        self.assertEqual(customers[0]["email"], "john@example.com")

    def test_modify_customer_info(self):
        """Tests modifying a customer's information."""
        Customer.create_customer(1, "John Doe", "john@example.com")
        # Verify initial customer details
        customers = read_file("customers.json")
        self.assertEqual(customers[0]["name"], "John Doe")
        self.assertEqual(customers[0]["email"], "john@example.com")
        # Now modify the customer's information
        Customer.modify_customer_info(1, name="John Smith", email="js@ex.com")
        # Verify the customer details have been updated
        customers = read_file("customers.json")
        self.assertEqual(customers[0]["name"], "John Smith")
        self.assertEqual(customers[0]["email"], "johnsmith@example.com")

    def test_create_reservation(self):
        """Tests the creation of a reservation."""
        Hotel.create_hotel(1, "Hotel Paradise", "New York", 100)
        Customer.create_customer(1, "John Doe", "john@example.com")
        Reservation.create_reservation(1, 1, 1, 50)
        reservations = read_file("reservations.json")
        self.assertEqual(len(reservations), 1)

    def test_cancel_reservation(self):
        """Tests canceling a reservation."""
        Hotel.create_hotel(1, "Hotel Paradise", "New York", 100)
        Customer.create_customer(1, "John Doe", "john@example.com")
        Reservation.create_reservation(1, 1, 1, 50)
        # Verify the reservation is created
        reservations = read_file("reservations.json")
        self.assertEqual(len(reservations), 1)
        # Now cancel the reservation
        Reservation.cancel_reservation(1)
        # Verify the reservation is canceled
        reservations = read_file("reservations.json")
        self.assertEqual(len(reservations), 0)

    def test_modify_hotel_info(self):
        """Tests modifying a hotel's information."""
        Hotel.create_hotel(1, "Hotel Paradise", "New York", 100)
        Hotel.modify_hotel_info(1, name="Updated Paradise", rooms=150)
        hotels = read_file("hotels.json")
        self.assertEqual(hotels[0]["name"], "Updated Paradise")
        self.assertEqual(hotels[0]["rooms"], 150)

    def test_modify_non_existent_hotel_or_customer(self):
        """Tests modifying a non-existent hotel or customer."""
        # Attempt to modify a non-existent hotel
        Hotel.modify_hotel_info(999, name="Non-existent Hotel", rooms=200)
        hotels = read_file("hotels.json")
        self.assertEqual(len(hotels), 0)  # No hotels should be modified
        # Attempt to modify a non-existent customer
        Customer.modify_customer_info(999, name="NA", email="na@ex.com")
        customers = read_file("customers.json")
        self.assertEqual(len(customers), 0)  # No customers should be modified

    def test_create_hotel_duplicate_id(self):
        """Tests creating a hotel with a duplicate hotel_id."""
        Hotel.create_hotel(1, "Hotel Paradise", "New York", 100)
        # Try to create a hotel with the same ID
        Hotel.create_hotel(1, "Hotel Sunshine", "Los Angeles", 50)
        hotels = read_file("hotels.json")
        self.assertEqual(len(hotels), 1)  # Only one hotel should exist
        self.assertEqual(hotels[0]["name"], "Hotel Paradise")

    def test_create_customer_duplicate_id(self):
        """Tests creating a customer with a duplicate customer_id."""
        Customer.create_customer(1, "John Doe", "john@example.com")
        # Try to create a customer with the same ID
        Customer.create_customer(1, "Jane Doe", "jane@example.com")
        customers = read_file("customers.json")
        self.assertEqual(len(customers), 1)
        self.assertEqual(customers[0]["name"], "John Doe")

    def test_delete_non_existent_hotel(self):
        """Tests deleting a non-existent hotel."""
        # Try to delete a hotel that does not exist
        Hotel.delete_hotel(999)
        hotels = read_file("hotels.json")
        self.assertEqual(len(hotels), 0)

    def test_delete_non_existent_customer(self):
        """Tests deleting a non-existent customer."""
        # Try to delete a customer that does not exist
        Customer.delete_customer(999)
        customers = read_file("customers.json")
        self.assertEqual(len(customers), 0)

    def test_cancel_non_existent_reservation(self):
        """Tests canceling a non-existent reservation."""
        # Try to cancel a reservation that does not exist
        Reservation.cancel_reservation(999)
        reservations = read_file("reservations.json")
        self.assertEqual(len(reservations), 0)

    def test_delete_hotel(self):
        """Tests the deletion of a hotel."""
        Hotel.create_hotel(1, "Hotel Paradise", "New York", 100)
        Hotel.create_hotel(2, "Hotel Sunshine", "Los Angeles", 50)
        # Verify both hotels exist
        hotels = read_file("hotels.json")
        self.assertEqual(len(hotels), 2)
        # Now delete one hotel
        Hotel.delete_hotel(1)
        # Verify the hotel has been deleted
        hotels = read_file("hotels.json")
        self.assertEqual(len(hotels), 1)
        self.assertEqual(hotels[0]["hotel_id"], 2)


if __name__ == "__main__":
    unittest.main()
