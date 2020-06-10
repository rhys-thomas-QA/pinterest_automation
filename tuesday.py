import tests.add_pins as add_pins

artist_array_2 = [
    "The Rolling Stones",
    # "Creedence Clearwater Revival",
    # "John Mayer",
    # "Guns N Roses",
    # "Metallica",
    # "Eric Clapton",
    # "Greenday"
]


# Tuesday
def lambda_handler_2(event=None, context=None):
    for n in artist_array_2:
        add_pins.full_process(n)
    print("New pins added for eight boards!")

lambda_handler_2()