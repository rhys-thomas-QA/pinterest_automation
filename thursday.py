import tests.add_pins as add_pins

artist_array_4 = [
    "Rage Against the Machine",
    "Pink Floyd",
    "Aerosmith",
    "Black Sabbath",
    "ZZ Top",
    "Bob Dylan",
    "Elvis Presley"
]


# Thursday
def lambda_handler_4(event=None, context=None):
    for n in artist_array_4:
        add_pins.full_process(n)
    print("New pins added for eight boards!")

lambda_handler_4()