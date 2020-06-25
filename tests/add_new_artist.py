import requests
import json
import urllib.parse
import time
import re
import cloudinary
import cloudinary.uploader
import cloudinary.api
from artist_array import artist_array
import PySimpleGUI as sg


artistSearchUrl = 0
urlencodedartist = 0
guides = 0
guides_array = 0
artistBoardUrl = 0
boardId = 0
description = 0
image_url = 0
replaced_slash_image_url = 0
pin_id = 0
pinimg_image_url = 0

emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F"  # emoticons
                           u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                           u"\U0001F680-\U0001F6FF"  # transport & map symbols
                           u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags=re.UNICODE)
cloudinary.config(
    cloud_name='dohldvzge',
    api_key='583672847454456',
    api_secret='m9TxiFjyUrnbH6fN_xMGfBs2unM'
)

cloudinary_upload_preset = 'kk4tiben'


def search_url(artist):
    global urlencodedartist
    urlencodedartist = urllib.parse.quote(artist, safe="")
    decodedUrl = "/search/pins/?q=" + urlencodedartist + "&rs=typed"
    encodedUrl = urllib.parse.quote(decodedUrl, safe="")
    splitArtist = artist.split(" ")

    # splitArtist is an array of the names of the artist
    array = []
    for n in splitArtist:
        output = ("&term_meta[]=" + n + "%7Ctyped")
        array.append(output)

    artistString = ''.join(array)
    encodedArtistString = urllib.parse.quote(artistString, safe="")

    json_data = '{"options":{"isPrefetch":false,"article":null,"auto_correction_disabled":false,"corpus":null,"customized_rerank_type":null,"filters":null,"page_size":null,"query":' + "\"" + artist + "\"" + ',"query_pin_sigs":null,"redux_normalize_feed":true,"rs":"typed","scope":"pins","source_id":null},"context":{}}'
    encodedJson = urllib.parse.quote(json_data, safe="")
    # print(encodedJson)
    epoch_time = int(time.time())
    stringTime = str(epoch_time)
    fullUrl = encodedUrl + encodedArtistString + "&data=" + encodedJson + "&_=" + stringTime
    global artistSearchUrl
    artistSearchUrl = "https://www.pinterest.co.uk/resource/BaseSearchResource/get/?source_url=" + fullUrl


def get_search_results(artist):
    search_url(artist)
    headers = {
    #removed for security purposes
    }
    payload = {}
    response = requests.request("GET", artistSearchUrl, headers=headers, data=payload)
    response_body = response.content
    parsed = json.loads(response_body)
    # print(parsed)
    global guides
    guides = parsed["resource_response"]["data"]["guides"]


def saving_guides():
    global guides_array
    guides_array = []
    trimmed_guides = guides[:15]
    for n in trimmed_guides:
        guide = n["display"]
        guides_array.append(guide)


def create_board(artist):
    urlencodedartist = urllib.parse.quote(artist, safe="")
    payload = 'source_url=/whatguitarshouldibuy/boards/&data=%7B%22options%22%3A%7B%22name%22%3A%22' + urlencodedartist + '%22%2C%22description%22%3A%22%22%2C%22category%22%3A%22other%22%2C%22privacy%22%3A%22public%22%2C%22collab_board_email%22%3Atrue%2C%22collaborator_invites_enabled%22%3Afalse%7D%2C%22context%22%3A%7B%7D%7D'
    headers = {
    #removed for security purposes
    }
    global artistBoardUrl
    artistBoardUrl = "https://www.pinterest.co.uk/resource/BoardResource/create/"

    response = requests.request("POST", artistBoardUrl, headers=headers, data=payload)
    status_code = response.status_code

    if status_code == 200:
        print(artist + " board creation successful")
    elif status_code == 400:
        print(artist + " board failed to create")
    elif status_code == 429:
        print("Too many requests")
    content = response.content
    parsedResponse = json.loads(content)
    global boardId
    boardId = parsedResponse["resource_response"]["data"]["id"]


def update_board(artist):
    string_guides_array = ", ".join(guides_array)
    stringify_list = str(string_guides_array)
    url = "https://www.pinterest.co.uk/resource/BoardResource/update/"
    source_url = "/whatguitarshouldibuy/boards/&data="
    global description
    description = ',"description":"' + artist + '. How to sound like ' + artist + '. My site can show you what guitar to buy to sound like ' + artist + '.' + stringify_list
    data = '{"options":{"board_id":"' + str(
        boardId) + '","name":"' + artist + '"' + description + '","privacy":"public","allow_homefeed_recommendations":true},"context":{}}'
    encoded_data = urllib.parse.quote(data, safe="")
    payload = source_url + encoded_data
    headers = {
    #removed for security purposes
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    status_code = response.status_code
    if status_code == 200:
        print(artist + " board update successful")
    elif status_code == 400:
        print("Board failed to update description")
    elif status_code == 429:
        print("Too many requests")


def search_for_pins(artist):
    search_url(artist)
    headers = {
    #removed for security purposes
    }
    payload = {}
    search_response = requests.request("GET", artistSearchUrl, headers=headers, data=payload)
    response_body = search_response.text
    parsed = json.loads(response_body)
    results_array = parsed["resource_response"]["data"]["results"]
    description_array = []
    for n in results_array:
        description = n["description"]
        no_emoji_description = emoji_pattern.sub(r'', description)
        description_array.append(no_emoji_description)
    link_array = []
    for m in results_array:
        link = m["link"]
        string_link = str(link)
        new_string_link = string_link.replace("https:", "https%3A")
        # slash_replace = new_string_link.replace("/", "%2F")
        if link is not None:
            link_array.append(new_string_link)
        elif link is None:
            link_array.append("None")
    title_array = []
    for o in results_array:
        title = o["title"]
        title_array.append(title)
    pin_id_array = []
    for r in results_array:
        pin_id = r["id"]
        pin_id_array.append(pin_id)

    splitArtist = artist.split(" ")

    # splitArtist is an array of the names of the artist
    array = []
    for n in splitArtist:
        output = ("&term_meta[]=" + n + "%7Crecentsearch%7C0")
        array.append(output)
    artistString = ''.join(array)
    source_url = "?q=" + urlencodedartist + "&rs=rs&eq=&etslf=311" + artistString
    encoded_source_url = urllib.parse.quote(source_url, safe="")
    data = "&data="
    # create the pin payloads from the results response
    i = 0
    while i <= 20:
        payload_array = []
        first_half_payload = '{"options":{"description":"' + description_array[i] + '"' + ',"link":"'
        encoded_first_half_payload = urllib.parse.quote(first_half_payload, safe="")
        # slash_link = link_payload.replace()
        link_payload = link_array[i]
        second_half_payload = '","title":"' + title_array[
            i] + '","clientTrackingParams":"CwABAAAAEDgxMDY4NjgwMTM2NDk1NTUGAAMACAA'
        third_half_payload = '","board_id":"' + str(
            boardId) + '","pin_id":"' + pin_id_array[
                                  i] + '","is_buyable_pin":false,"is_removable":false,"carousel_slot_index":0},"context":{}}'
        encoded_second_half_payload = urllib.parse.quote(second_half_payload, safe="")
        encoded_third_half_payload = urllib.parse.quote(third_half_payload, safe="")
        payload = encoded_first_half_payload + link_payload + encoded_second_half_payload + '%7E0' + encoded_third_half_payload
        payload_array.append(payload)
        url = "https://www.pinterest.co.uk/resource/RepinResource/create/"
        full_payload = 'source_url=/search/pins' + encoded_source_url + data + payload
        headers = {
        #removed for security purposes
        }
        pin_response = requests.request("POST", url, headers=headers, data=full_payload)
        status_code = pin_response.status_code
        if status_code == 200:
            print(artist + " pin has been added successfully")
        elif status_code == 400:
            print(artist + " pin failed to save")
        elif status_code == 429:
            print("Too many requests")
        i += 1


def post_image_to_cloudinary(artist):
    lowercase_artist = artist.lower()
    dashed_lowercase_artist = lowercase_artist.replace(" ", "-")
    base_path = "/Users/rhysthomas/Documents/WhatGuitarShouldIBuy/Pinterest/"
    file_name = base_path + dashed_lowercase_artist + "/" + dashed_lowercase_artist + "-1.png"
    response = cloudinary.uploader.upload(file_name)
    global image_url
    image_url = str(response["url"])


def create_new_pin(artist):
    headers = {
    #removed for security purposes
    }
    lowercase_artist = artist.lower()
    dashed_lowercase_artist = lowercase_artist.replace(" ", "-")
    base_url = "https://www.pinterest.co.uk/resource/PinResource/create/"
    encoded_pin_builder = urllib.parse.quote("/pin-builder/", safe="")
    source_url = 'source_url=' + encoded_pin_builder + '&data='
    encode_image_url = image_url.replace("https://", "https%3A%2F%2F")
    global replaced_slash_image_url
    replaced_slash_image_url = encode_image_url.replace("/", "%2F")
    first_half = '{"options":{"board_id":"' + str(
        boardId) + '","field_set_key":"create_success","skip_pin_create_log":true' + description + '","link":"whatguitarshouldibuy.com/' + dashed_lowercase_artist + '","title":"How to sound like ' + artist + '","image_url":"'
    second_half = '","method":"uploaded","upload_metric":{"source":"partner_upload_standalone"}},"context":{}}'
    encoded_first_half = urllib.parse.quote(first_half, safe="")
    encoded_second_half = urllib.parse.quote(second_half, safe="")
    payload = source_url + encoded_first_half + replaced_slash_image_url + encoded_second_half
    url = base_url
    response = requests.request("POST", url, headers=headers, data=payload)
    status_code = response.status_code
    if status_code == 200:
        print(artist + " pin creation successful")
    elif status_code == 400:
        print(artist + " pin failed to create")
    elif status_code == 429:
        print("Too many requests")
    content = response.content
    parsed_response = json.loads(content)
    global pin_id
    pin_id = parsed_response["resource_response"]["data"]["id"]
    global pinimg_image_url
    pinimg_image_url = parsed_response["resource_response"]["data"]["images"]["474x"]["url"]


def update_board_cover(artist):
    url = "https://www.pinterest.co.uk/resource/BoardResource/update/"
    headers = {
    #removed for security purposes
    }
    source_url = "source_url=/whatguitarshouldibuy/boards/&data="
    first_half = '{"options":{"board_id":"' + boardId + '","url":"'
    encoded_first_half = urllib.parse.quote(first_half, safe="")
    image_link = pinimg_image_url.replace("https://", "https%3A//")
    second_half = '","pin_id":"' + str(pin_id) + '","pin_image_url":"'
    encoded_second_half = urllib.parse.quote(second_half, safe="")
    third_half = '","crop_x":0,"crop_y":52,"height":236,"width":236,"scale":1},"context":{}}'
    encoded_third_half = urllib.parse.quote(third_half, safe="")
    full_payload = source_url + encoded_first_half + image_link + encoded_second_half + image_link + encoded_third_half
    response = requests.request("POST", url, headers=headers, data=full_payload)
    status_code = response.status_code
    if status_code == 200:
        print(artist + " board cover updated")
    elif status_code == 400:
        print(artist + " board cover failed to update")
    elif status_code == 429:
        print("Too many requests")
    cloudinary.api.delete_all_resources()


def full_process(artist):
    get_search_results(artist)
    saving_guides()
    create_board(artist)
    update_board(artist)
    search_for_pins(artist)
    # post_image_to_cloudinary(artist)
    # create_new_pin(artist)
    # update_board_cover(artist)


full_process("Rock Music")
