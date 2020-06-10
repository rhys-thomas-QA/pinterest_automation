import tests.add_pins as add_pins

artist_array_6 = [
    "Megadeth",
    "Chuck Berry",
    "John Lennon",
    "B.B. King",
    "The Clash",
    "Fleetwood Mac",
    "Santana"
]


# Saturday
def lambda_handler_6(event=None, context=None):
    for n in artist_array_6:
        add_pins.full_process(n)
    print("New pins added for eight boards!")
