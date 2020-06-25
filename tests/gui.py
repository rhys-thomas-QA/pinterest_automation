import PySimpleGUI as sg
# from testy import full_process
import requests
import json
import urllib.parse
import time


sg.theme('LightBrown13')	# Add a touch of color
sg.theme_background_color("white")
sg.theme_text_element_background_color("white")
# sg.theme_element_background_color("red")
# sg.theme_text_color("White")
# sg.theme_button_color("Red")
# sg.theme


# All the stuff inside your window.
layout = [  [sg.Text('Add new pins for a board')],
            [sg.Text('Enter the exact name of the board'), sg.InputText()],
            [sg.Text('Enter the number of pins you want to save'), sg.InputText()],
            [sg.Button('Add my pins!'), sg.Button('Close software')],
            # [sg.Output(size=(50, 10), key='-OUTPUT-')],
            ]

# Create the Window
window = sg.Window('AutoPinner', layout)
sg.theme_list()
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event in (None, 'Add my pins!'):
        print = sg.Print
        # full_process(values[0], values[1])

        import requests
        import json
        import urllib.parse
        import time


        board_id = 0
        extended_board_id = 0
        pin_array = []
        image_signature_array = []
        second_pin_array = 0
        search_results_image_signatures_array = 0
        different_value_ids = []
        pin_id_array = []
        description_array = []
        link_array = []
        title_array = []
        results_array = []
        bookmark = 0


        def get_board_ids(artist):
            url = "https://www.pinterest.co.uk/resource/BoardsResource/get/?source_url=%2Fwhatguitarshouldibuy%2Fboards%2F&data=%7B%22options%22%3A%7B%22isPrefetch%22%3Afalse%2C%22privacy_filter%22%3A%22all%22%2C%22sort%22%3A%22last_pinned_to%22%2C%22field_set_key%22%3A%22profile_grid_item%22%2C%22username%22%3A%22whatguitarshouldibuy%22%2C%22page_size%22%3A25%2C%22group_by%22%3A%22visibility%22%2C%22include_archived%22%3Atrue%2C%22redux_normalize_feed%22%3Atrue%7D%2C%22context%22%3A%7B%7D%7D&_=1589165390707"
            payload = {}
            headers = {
            #removed for security purposes
            }
            response = requests.request("GET", url, headers=headers, data=payload)
            content = response.content
            parsed_response = json.loads(content)
            global board_id
            data = parsed_response["resource_response"]["data"]
            board_bookmark = parsed_response["resource"]["options"]["bookmarks"]
            array = []
            for n in data:
                if n["name"] == artist:
                    board_id = n["id"]
                    array.append(board_id)
            while len(array) == 0:
                url = "https://www.pinterest.co.uk/resource/BoardsResource/get/?source_url=%2Fwhatguitarshouldibuy%2Fboards%2F&data=%7B%22options%22%3A%7B%22bookmarks%22%3A%5B%22" + str(
                    board_bookmark) + "%22%5D%2C%22isPrefetch%22%3Afalse%2C%22privacy_filter%22%3A%22all%22%2C%22sort%22%3A%22last_pinned_to%22%2C%22field_set_key%22%3A%22profile_grid_item%22%2C%22username%22%3A%22whatguitarshouldibuy%22%2C%22page_size%22%3A25%2C%22group_by%22%3A%22visibility%22%2C%22include_archived%22%3Atrue%2C%22redux_normalize_feed%22%3Atrue%7D%2C%22context%22%3A%7B%7D%7D&_=1589165410049"
                payload = {}
                headers = {
                #removed for security purposes
                }
                rest_of_board = requests.request("GET", url, headers=headers, data=payload)
                rest_of_board_content = rest_of_board.content
                parsed_rest_of_board = json.loads(rest_of_board_content)
                data_parsed = parsed_rest_of_board["resource_response"]["data"]
                board_bookmark = parsed_rest_of_board["resource"]["options"]["bookmarks"]
                for n in data_parsed:
                    if n["name"] == artist:
                        board_id = n["id"]
                        array.append(board_id)
            print("Board ids retrieved")
            window.Refresh()


        def get_board_pins(artist):
            lowercase_artist = artist.lower()
            dashed_lowercase_artist = lowercase_artist.replace(" ", "-")
            global image_signature_array

            def board_url(board_id):
                board_url = "https://www.pinterest.co.uk/resource/BoardFeedResource/get/?source_url=%2Fwhatguitarshouldibuy%2F" + dashed_lowercase_artist + "%2F&data=%7B%22options%22%3A%7B%22isPrefetch%22%3Afalse%2C%22board_id%22%3A%22" + str(
                    board_id) + "%22%2C%22board_url%22%3A%22%2Fwhatguitarshouldibuy%2F" + dashed_lowercase_artist + "%2F%22%2C%22field_set_key%22%3A%22partner_react_grid_pin%22%2C%22filter_section_pins%22%3Atrue%2C%22sort%22%3A%22default%22%2C%22layout%22%3A%22default%22%2C%22page_size%22%3A25%2C%22redux_normalize_feed%22%3Atrue%7D%2C%22context%22%3A%7B%7D%7D&_=1589162950870"
                response = requests.request("GET", board_url, headers=headers, data=payload)
                content = response.content
                parsed = json.loads(content)
                data = parsed["resource_response"]["data"]
                del data[-1:]
                for n in data:
                    image_signature = n["image_signature"]
                    image_signature_array.append(image_signature)

            payload = {}
            headers = {
            #removed for security purposes
            }
            if board_id != 0:
                board_url(board_id)
            elif board_id == 0:
                board_url(extended_board_id)
            print(artist + " board pins retrieved")
            window.Refresh()



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
            response_body = response.text
            parsed = json.loads(response_body)
            global bookmark
            bookmark = parsed["resource"]["options"]["bookmarks"][0]
            global results_array
            results_array = parsed["resource_response"]["data"]["results"]
            promoted_array = []
            for n in results_array:
                is_promoted = n["is_promoted"]
                if is_promoted is True:
                    promoted_array.append(n["image_signature"])
            global search_results_image_signatures_array
            search_results_image_signatures_array = []
            for n in results_array:
                search_results_image_signatures = n["image_signature"]
                search_results_image_signatures_array.append(search_results_image_signatures)
            global different_value_ids
            if image_signature_array != 0:
                different_value_ids = list(
                    set(search_results_image_signatures_array) - set(image_signature_array) - set(promoted_array))
            elif image_signature_array != 0:
                different_value_ids = list(
                    set(search_results_image_signatures_array) - set(image_signature_array) - set(promoted_array))

            while len(different_value_ids) <= 20:
                print("Not enough different pins, searching for more")
                url = "https://www.pinterest.co.uk/resource/BaseSearchResource/get/"
                artist_with_space = artist.replace(" ", "%2520")
                shortened_artist_with_space = artist.replace(" ", "%20")
                payload = 'source_url=/search/pins/%3Fq%3D' + artist_with_space + '%26rs%3Dtyped%26term_meta%5B%5D%3D' + artist_with_space + '%257Ctyped&data=%7B%22options%22%3A%7B%22bookmarks%22%3A%5B%22' + bookmark + '%22%5D%2C%22isPrefetch%22%3Afalse%2C%22article%22%3Anull%2C%22auto_correction_disabled%22%3Afalse%2C%22corpus%22%3Anull%2C%22customized_rerank_type%22%3Anull%2C%22filters%22%3Anull%2C%22page_size%22%3Anull%2C%22query%22%3A%22' + shortened_artist_with_space + '%22%2C%22query_pin_sigs%22%3Anull%2C%22redux_normalize_feed%22%3Atrue%2C%22rs%22%3A%22typed%22%2C%22scope%22%3A%22pins%22%2C%22source_id%22%3Anull%7D%2C%22context%22%3A%7B%7D%7D'
                headers = {
                #removed for security purposes
                }
                response = requests.request("POST", url, headers=headers, data=payload)
                content = response.content
                parsed_content = json.loads(content)
                bookmark = parsed_content["resource"]["options"]["bookmarks"][0]
                second_results_array = parsed_content["resource_response"]["data"]["results"]
                results_array = results_array + second_results_array
                for n in second_results_array:
                    second_search_results_image_signatures = n["image_signature"]
                    search_results_image_signatures_array.append(second_search_results_image_signatures)
                if image_signature_array != 0:
                    different_value_ids = list(
                        set(search_results_image_signatures_array) - set(image_signature_array) - set(promoted_array))
                elif image_signature_array != 0:
                    different_value_ids = list(
                        set(search_results_image_signatures_array) - set(image_signature_array) - set(promoted_array))
            print("Got search results for " + artist)
            window.Refresh()


        def comparison_of_board_pins_and_results_pins():
            global pin_id_array
            global description_array
            global link_array
            global title_array
            for u in different_value_ids:
                for x in results_array:
                    if u == x["image_signature"]:
                        pin_id = x["id"]
                        pin_id_array.append(pin_id)
                        description = x["description"]
                        description_array.append(description)
                        link = x["link"]
                        if link is not None:
                            link_array.append(link)
                        elif link is None:
                            link_array.append("None")
                        title = x["title"]
                        title_array.append(title)


        def save_pins(artist, number_of_pins_to_save):
            splitArtist = artist.split(" ")
            array = []
            for n in splitArtist:
                output = ("&term_meta[]=" + n + "%7Ctyped")
                array.append(output)
            artistString = ''.join(array)
            url = "https://www.pinterest.co.uk/resource/RepinResource/create/"
            source_url = "?q=" + urlencodedartist + "&rs=typed" + artistString
            encoded_source_url = urllib.parse.quote(source_url, safe="")
            data = "&data="
            i = 0
            while i <= int(number_of_pins_to_save):
                first_half_payload = '{"options":{"description":"' + description_array[i] + '"' + ',"link":"'
                encoded_first_half_payload = urllib.parse.quote(first_half_payload, safe="")
                link_payload = link_array[i]
                split_link_payload = link_payload.replace(":", "%3A")
                second_half_payload = '","title":"' + title_array[
                    i] + '","clientTrackingParams":"CwABAAAAEDQ1MTUyNDk5MzUzNjUwMTAGAAMACAA~0","board_id":"' + str(
                    board_id) + '","pin_id":"' + pin_id_array[
                                          i] + '","is_buyable_pin":false,"is_removable":false,"carousel_slot_index":0},"context":{}}'
                encoded_second_half_payload = urllib.parse.quote(second_half_payload, safe="")
                payload = encoded_first_half_payload + split_link_payload + encoded_second_half_payload

                # encoded_search = urllib.parse.quote("/search/pins/", safe="")
                full_payload = 'source_url=/search/pins/' + encoded_source_url + data + payload
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


        def cleanup():
            del pin_array[:]
            del image_signature_array[:]
            del search_results_image_signatures_array[:]
            del different_value_ids[:]
            del pin_id_array[:]
            del description_array[:]
            del link_array[:]
            del title_array[:]
            del results_array[:]


        def full_process(artist, number_of_pins_to_save):
            get_board_ids(artist)
            get_board_pins(artist)
            get_search_results(artist)
            comparison_of_board_pins_and_results_pins()
            save_pins(artist, number_of_pins_to_save)
            cleanup()

        full_process(values[0], values[1])
    if event in (None, 'Close software'):	# if user closes window or clicks cancel
        break

window.close()
