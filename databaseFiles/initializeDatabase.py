"""
class: initializeDatbase
most recent update: 8/13/2024 (commenting)
programmers: Jonathan Aghachi

Description: It sets up collections for room types, rooms, customers, reservations, and room bookings.
"""
import pydoc

import asyncio
from datetime import datetime
from databaseconnect import dataBase


async def create_schema():
    """
    Creates and initializes the database schema for a hotel reservation system.

    This function creates several collections in the MongoDB database, inserts initial data,
    creates indexes, and purges dummy data. The collections created include room types, rooms,
    customers, reservations, and room bookings.

    Attributes:
    -----------
    db_instance : dataBase
        An instance of the dataBase class to manage database connections and operations.
    db : AsyncIOMotorClient
        The MongoDB database object for performing operations.
    
    Collections:
    ------------
    roomTypes : collection
        Stores information about different room types.
    rooms : collection
        Stores information about individual rooms.
    customers : collection
        Stores customer information.
    reservations : collection
        Stores reservation details.
    roomBookings : collection
        Stores booking details for specific rooms.

    Methods:
    --------
    create_index(keys: list, **kwargs) -> str:
        Creates an index on the specified keys in the collection.
    """

    db_instance = dataBase()
    db = await db_instance.get_database()
    
    # Create RoomTypes Collection
    roomTypes = db['roomTypes']
    result = await roomTypes.insert_many([
        {"type": "Suite", "price": 200, "persons": 4},
        {"type": "Double", "price": 125, "persons": 4},
        {"type": "Single", "price": 75, "persons": 1}
    ])

    suite_id = result.inserted_ids[0]
    double_id = result.inserted_ids[1]
    single_id = result.inserted_ids[2]

    # Create Rooms Collection
    rooms = db['rooms']
    await rooms.insert_many([
        {"typeId": suite_id, "roomNumber": "301"},
        #{"typeId": suite_id, "roomNumber": "302"},
        #{"typeId": suite_id, "roomNumber": "303"},
        #{"typeId": suite_id, "roomNumber": "304"},
        #{"typeId": suite_id, "roomNumber": "305"},
        {"typeId": double_id, "roomNumber": "201"},
        #{"typeId": double_id, "roomNumber": "202"},
        #{"typeId": double_id, "roomNumber": "203"},
        #{"typeId": double_id, "roomNumber": "204"},
        #{"typeId": double_id, "roomNumber": "205"},
        {"typeId": single_id, "roomNumber": "101"},
        #{"typeId": single_id, "roomNumber": "102"},
        #{"typeId": single_id, "roomNumber": "103"},
        #{"typeId": single_id, "roomNumber": "104"},
        #{"typeId": single_id, "roomNumber": "105"}
    ])
    
    # Find a room for reservations and room bookings to correctly populate collection
    room = await rooms.find_one({"roomNumber": "301"})

    # Create Customers Collection
    customers = db['customers']
    await customers.insert_one(
        {
            "name": "John Doe",
            "email": "john.doe@example.com",
            "persons": 1
        },
    )

    # Find the customer
    customer = await customers.find_one({"email": "john.doe@example.com"})

    # Create Reservations Collection
    reservations = db['reservations']
    await reservations.insert_one(
        {
            "customerId": customer["_id"], # type: ignore
            "persons": 0,
            "roomId": room["_id"], # type: ignore
            "confirmationNumber": "name-123456",
            "checkIn": datetime(2023, 8, 1),
            "checkOut": datetime(2023, 8, 5)
        }
    )

    # Create RoomBookings Collection
    roomBookings = db['roomBookings']
    room = await rooms.find_one({"roomNumber": "301"})
    await roomBookings.insert_one(
        {
            "roomId": room["_id"], # type: ignore
            "bookedDate": datetime(1989, 7, 3)
        }
    )

    # Create Indexes
    await roomBookings.create_index([("roomId", 1)])
    await roomBookings.create_index([("bookedDate", 1)])
    await roomBookings.create_index([("roomId", 1), ("bookedDate", 1)])

    # Purge dummy data to start with a clean database
    await db['customers'].delete_many({})
    await db['reservations'].delete_many({})
    await db['roomBookings'].delete_many({})
    #await db['rooms'].delete_many({})
    #await db['roomTypes'].delete_many({})

    # Close the client
    db_instance.client.close()

async def main():
    """
    The main function that runs the schema creation asynchronously.
    """
    await create_schema()

asyncio.run(main())
