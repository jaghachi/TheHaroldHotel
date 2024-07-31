#run only once
from databaseFiles.databaseconnect import dataBase

async def create_schema():

    db_instance = dataBase()
    db = await db_instance.get_database()
    
    # Create Customers Collection
    customers = db['customers']
    customers.insert_many([
        {
            "name": "John Doe",
            "email": "john.doe@example.com",
            "persons": 1,
            "reservations": []
        },
    ])

    # Create Reservations Collection
    reservations = db['reservations']
    reservations.insert_many([
        {
            "customer": {
                "customerId": customers.find_one({"email": "john.doe@example.com"})["_id"],
                "name": "John Doe",
                "email": "john.doe@example.com"
            },
            "roomId": None,
            "confirmationNumber": 123456,
            "checkIn": None,
            "checkOut": None
        }
    ])
    
    # Create RoomTypes Collection
    roomTypes = db['roomTypes']
    roomTypeIds = await roomTypes.insert_many([
        {"type": "Suite", "price": 200, "persons": 4},
        {"type": "Double", "price": 125, "persons": 4},
        {"type": "Single", "price": 75, "persons": 1}
    ])
    
    suite_id = roomTypeIds.inserted_ids[0]
    double_id = roomTypeIds.inserted_ids[1]
    single_id = roomTypeIds.inserted_ids[2]
    
    # Create Rooms Collection
    rooms = db['rooms']
    await rooms.insert_many([
        {"typeId": suite_id, "roomNumber": "301"},
        {"typeId": suite_id, "roomNumber": "302"},
        {"typeId": suite_id, "roomNumber": "303"},
        {"typeId": suite_id, "roomNumber": "304"},
        {"typeId": suite_id, "roomNumber": "305"},
        {"typeId": double_id, "roomNumber": "201"},
        {"typeId": double_id, "roomNumber": "202"},
        {"typeId": double_id, "roomNumber": "203"},
        {"typeId": double_id, "roomNumber": "204"},
        {"typeId": double_id, "roomNumber": "205"},
        {"typeId": single_id, "roomNumber": "101"},
        {"typeId": single_id, "roomNumber": "102"},
        {"typeId": single_id, "roomNumber": "103"},
        {"typeId": single_id, "roomNumber": "104"},
        {"typeId": single_id, "roomNumber": "105"}
    ])

    # Create RoomBookings Collection
    roomBookings = db['roomBookings']
    await roomBookings.insert_many([
        {
            "roomId": (await rooms.find_one({"roomNumber": "301"}))["_id"],
            "bookedDate": None
        }
    ])

    # Create Indexes
    await roomBookings.create_index([("roomId", 1)])
    await roomBookings.create_index([("bookedDate", 1)])
    await roomBookings.create_index([("roomId", 1), ("bookedDate", 1)])
    
    #purge dummy data
    await db['customers'].delete_many({})
    await db['reservations'].delete_many({})
    await db['roomBookings'].delete_many({})

    client.close()

if __name__ == "__main__":
    create_schema()
