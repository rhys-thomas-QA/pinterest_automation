import requests
import json
import urllib.parse
import cloudinary.uploader
import cloudinary.api

board_id = 821344119481342852
bookmark = 0
lowercase_artist = ""
description = ""
image_url = ""
replaced_slash_image_url = ""
dashed_lowercase_artist = ""
pinimg_image_url = ""
pin_id = ""

cloudinary.config(
    cloud_name='dohldvzge',
    api_key='583672847454456',
    api_secret='m9TxiFjyUrnbH6fN_xMGfBs2unM'
)

cloudinary_upload_preset = 'kk4tiben'


def get_board_ids(artist):
    global lowercase_artist
    global dashed_lowercase_artist
    lowercase_artist = artist.lower()
    remove_dot = lowercase_artist.replace(".", "")
    dashed_lowercase_artist = remove_dot.replace(" ", "-")
    payload = {}
    headers = {
    #removed for security purposes
    }
    board_url = "https://www.pinterest.co.uk/resource/BoardResource/get/?source_url=%2Fwhatguitarshouldibuy%2F" + dashed_lowercase_artist + "%2F&data=%7B%22options%22%3A%7B%22isPrefetch%22%3Afalse%2C%22username%22%3A%22whatguitarshouldibuy%22%2C%22slug%22%3A%22" + dashed_lowercase_artist + "%22%2C%22field_set_key%22%3A%22detailed%22%7D%2C%22context%22%3A%7B%7D%7D&_=1589761481969"
    response = requests.request("GET", board_url, headers=headers, data=payload)
    content = response.content
    parsed = json.loads(content)
    global description
    description = parsed["resource_response"]["data"]["description"]


def post_image_to_cloudinary():
    base_path = "/Users/rhysthomas/Documents/WhatGuitarShouldIBuy/Pinterest/"
    file_name = base_path + dashed_lowercase_artist + "/" + dashed_lowercase_artist + "-3.png"
    response = cloudinary.uploader.upload(file_name)
    global image_url
    image_url = str(response["url"])


def create_new_pin(artist):
    headers = {
    #removed for security purposes
    }
    base_url = "https://www.pinterest.co.uk/resource/PinResource/create/"
    source_url = 'source_url=/pin-builder/&data='
    encode_image_url = image_url.replace("https://", "https%3A%//")
    global replaced_slash_image_url
    first_half = '{"options":{"board_id":"' + str(
        board_id) + '","field_set_key":"create_success","skip_pin_create_log":true,"description":"' + description + '","link":"whatguitarshouldibuy.com/' + dashed_lowercase_artist + '","title":"How to sound like ' + artist + '","image_url":"'
    second_half = '","method":"uploaded","upload_metric":{"source":"partner_upload_standalone"}},"context":{}}'
    encoded_first_half = urllib.parse.quote(first_half, safe="")
    encoded_second_half = urllib.parse.quote(second_half, safe="")
    payload = source_url + encoded_first_half + encode_image_url + encoded_second_half
    url = base_url
    response = requests.request("POST", url, headers=headers, data=payload)
    status_code = response.status_code
    if status_code == 200:
        print(artist + " pin creation successful")
    elif status_code == 400:
        print(artist + " pin failed to create")
    elif status_code == 429:
        print("Too many requests")
    cloudinary.api.delete_all_resources()



def full_process(artist):
    get_board_ids(artist)
    post_image_to_cloudinary()
    create_new_pin(artist)


artist_array_1 = [
    "Queen",
    "Lynyrd Skynyrd",
    "Foo Fighters",
    "Dire Straits",
    "Red Hot Chilli Peppers",
    "Zakk Wylde",
    "Slayer"
]
artist_array_2 = [
    "The Rolling Stones",
    "Creedence Clearwater Revival",
    "John Mayer",
    "Guns N Roses",
    "Metallica",
    "Eric Clapton",
    "Greenday"
]
artist_array_3 = [
    "Radiohead",
    "Oasis",
    "Blur",
    "ACDC",
    "Led Zeppelin",
    "Jimi Hendrix",
    "The Doors"
]
artist_array_4 = [
    "Rage Against the Machine",
    "Pink Floyd",
    "Aerosmith",
    "Black Sabbath",
    "ZZ Top",
    "Bob Dylan",
    "Elvis Presley"
]
artist_array_5 = [
    # "The White Stripes",
    "Ed Sheeran",
    "Johnny Cash",
    "The Eagles",
    "The Beatles",
    "Chet Atkins",
    "The Lumineers"
]
artist_array_6 = [
    "Megadeth",
    "Chuck Berry",
    "John Lennon",
    "B.B. King",
    "The Clash",
    "Fleetwood Mac",
    "Santana"
]
artist_array_7 = [
    "Iron Maiden",
    "Buddy Holly",
    "Jeff Buckley",
    "Snow Patrol",
    "King Crimson",
    "Bob Marley",
    "Joan Jett"
]


# Monday
def lambda_handler_1(event=None, context=None):
    for n in artist_array_1:
        full_process(n)
    print("New pins added for 7 artists!")


# Tuesday
def lambda_handler_2(event=None, context=None):
    for n in artist_array_2:
        full_process(n)
    print("New pins added for 7 artists!")


# Wednesday
def lambda_handler_3(event=None, context=None):
    for n in artist_array_3:
        full_process(n)
    print("New pins added for 7 artists!")


# Thursday
def lambda_handler_4(event=None, context=None):
    for n in artist_array_4:
        full_process(n)
    print("New pins added for 7 artists!")


# Friday
def lambda_handler_5(event=None, context=None):
    for n in artist_array_5:
        full_process(n)
    print("New pins added for 7 artists!")


# Saturday
def lambda_handler_6(event=None, context=None):
    for n in artist_array_6:
        full_process(n)
    print("New pins added for 7 artists!")


# Sunday
def lambda_handler_7(event=None, context=None):
    for n in artist_array_7:
        full_process(n)
    print("New pins added for 7 artists!")


lambda_handler_6()
# full_process("Ed Sheeran")
