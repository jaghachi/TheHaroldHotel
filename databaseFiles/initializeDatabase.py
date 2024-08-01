import asyncio
from datetime import datetime
from databaseconnect import dataBase


async def create_schema():
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

    # Close the client
    db_instance.client.close()

async def main():
    await create_schema()

asyncio.run(main())
