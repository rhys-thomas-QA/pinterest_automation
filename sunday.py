import tests.add_pins as add_pins

artist_array_7 = [
    "Iron Maiden",
    "Buddy Holly",
    "Jeff Buckley",
    "Snow Patrol",
    "King Crimson",
    "Bob Marley",
    "Joan Jett"
]


def lambda_handler_7(event=None, context=None):
    for n in artist_array_7:
        add_pins.full_process(n)
    print("New pins added for eight boards!")
