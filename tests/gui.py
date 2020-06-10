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
                'authority': 'www.pinterest.co.uk',
                'accept': 'application/json, text/javascript, */*, q=0.01',
                'x-pinterest-appstate': 'active',
                'x-app-version': 'a2a392a',
                'x-requested-with': 'XMLHttpRequest',
                'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-mode': 'cors',
                'sec-fetch-dest': 'empty',
                'referer': 'https://www.pinterest.co.uk/',
                'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
                'cookie': 'csrftoken=34d8c022b199d4258a6f48e00a1a9aa3; bei=false; cm_sub=denied; logged_out=True; fba=True; g_state={"i_p":1588835383497,"i_l":2}; ujr=1; fbm_274266067164=base_domain=.www.pinterest.co.uk; _auth=1; _pinterest_sess=TWc9PSZ1WUxsbE5zaW1qOUltc1ppV2d3UTZ2emdBRGlOdEJ4dlptU2dvMHB2SlIzN01rVDlxcEFna21ocWNoMGZJT2dBZjR4Qk5yTVgwRlVUR2R2enNHRlVWRnBFYWtGYnkwK3VmZTJ3K2JHakZJMXNUeEZHVHFFaFE4ZFpyZy9FRjBGNnB2S0JEZCtsd3ZhL0xyazBWd0I3d3dJRFRORTFUOHJrYUxmTjF2NnMvK1l0UmZlM004NEdaTi9MTDJLalg5RFY4SG5vV05Md2hNdGJJZHFWelVsTTZyUDlRYld1SmUxZkh0eG9RSitoMGh4VGpWcGVkUGprV1pnRVFmL3hlOWQ4L2JueFd4dnZqZzUxd2FxUDVZTVNCd3lDVS9aZ2VkRlRlOU1WSC8zWTIwWkNtNnhGMHk0RUgzV0hIVURWOGNyZ00rcHd3VExtMmZWeFFxNk02bE1WVklJQnZlMVBHZWFkVEhyRHlrU2dXdmtaTzkvQmlGd050RlNZYzFWV1N5bThWdWs1cGNsS0xLQW5CUWoxTHpuQ1VNQWVtaFVtdGROWHEwcHpySmVrb09uTEdKYkFoTnA3cEo0THNMT25nWWYxejliQTY5M2xvbENUNHpVclNLT05rT2gxMlJTYWtjYTRnVGgycTJ6SmdIWWVOV2U1QjZxbEFHUVNrU1FMbk15VlptVHU2VVVFNXZ4ZGdhRXBHcTB6U2pzVU9sV3JYMjJBRnNwWVd2czQ2K1ovOHdtVnBRUThYWkh4WjlzdE5pUjNzUVBKWldNM21SaWp1akJ5YmFkSjFuVnlDV1JtbzRLUzZxVm1pSkNkaVN2RkFDQi9mY3R1bXczRVArZFYxS1JtNHJYaVFqSmZxaHg2TGVkOE9wYjl2SkpYU2JPRnZBYkhteTlFNGptOXBmRjR4dlJTN0VJZWNBUTdhSUV1elowV3ZYU0dDeUVpOWZ0YitoSUdYQWQyWVVvWmNlT3Q1K0pRNnZOcWYwWlJDVm5YSWNtcTQ1a2NjNGRBTG1hdmhSOE40QnZCN1pUR2ZmVVJGcHJLTXN6Y2xKeGN3ZHpwVWlxMkVSY2g4V1Y2cGlYTUMrT1RsNTFSZytOVTVFeE84Q2hVdW9PcUZMM3VpS3JjWGRVeW0yQWhuTklBNDlaTzhPbnF2aDJyOGxBb1FicCtlN1Qvc2l1UHpJWWdHeDhaaXBHNUtIQUpTZ0hsamdKVkpoNkRjb3hOR3Z3a1YrQVFMYzd3SFFmRzZMTTJVdTZBM2IwNUsyRnVzNkJnM3JqNVVvUFhrSnhoQTQ1Wk9sWXJORHcyZ25BMWxyWGFPT2VWUnZsTVJ2S3dOZGE3ZysvbjAyaHdLcHozSUFRbXJrOEl2ODZpNThKdGFRcXB3MUx5VGd2dzBadmsrQ2tQbFE3RytBc2VYd0Z5aTd6RzVnREI3U2NiZVQxTk9jMjh6eXErbHdNZTN4TzdyelVGNCszY3F6TTIrUFRHMUU4aWVTSzZVbStXZ2tLZ21Va0E3VmlTSlFKN0pqRmlURGFnaTlXY3gxaERKSXRYeDA3R25oZDVWUW9OYmhYaFdHZ3dScCtmek1EUzJkcGF3bzIwa29lcHloMGQ2ZW12YjhWZXFlUmdhWTFka0R1WFVOSUdpQlYvYU9jdWdYSDF3elVLd3c2R25UZFMxT3hDSnF3SUFPVzNPc1JaeTJoR1psZlhpdk0yTzNyM0Z6TVpxalE2WUtlcjRjWVdsZ3J0V3JGY1RqN0FtRWF5K0lrTHo0TUk3R3EyUU12eTJFSkVCM1NubDIzQnN6S2VzK0R3OEpOdEwwSXBOTFlwNm1YdS9HYnhhN2ZLMjlUQ0xKTHJRTWx0OWVHaFVEMDhTQmxVQ083WWlpYmYrbVpZJnVhM3BLN0dYL2NYdlFmb1drQXEvM2h2WHNxcz0=; _routing_id="11b53b90-db40-4e10-9b81-b511e4736845"; sessionFunnelEventLogged=1'
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
                    'authority': 'www.pinterest.co.uk',
                    'accept': 'application/json, text/javascript, */*, q=0.01',
                    'x-pinterest-appstate': 'background',
                    'x-app-version': 'a2a392a',
                    'x-requested-with': 'XMLHttpRequest',
                    'x-pinterest-experimenthash': '2e3e38c28e4784f66619577a6be42e0816322aeb279dad5136a775535b171fd0a69723cf299c262579d9b3284a5a2f28e9b2997ad3decc8974ced878298da87f',
                    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
                    'sec-fetch-site': 'same-origin',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-dest': 'empty',
                    'referer': 'https://www.pinterest.co.uk/',
                    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
                    'cookie': 'csrftoken=c492d0826894d834bbd0d87ef80dbef2; _routing_id="d1b1a40a-8e88-4ce4-8a19-214bfb84556a"; sessionFunnelEventLogged=1; bei=false; cm_sub=denied; logged_out=True; fba=True; _auth=1; _pinterest_sess=TWc9PSZzYnhDQzlxc0ZaQ2pTMVNUaGZ4YVZ1S3pEUXljMFdQTjNnTG5zQWRGSWVhZFhtU3ZuK3F1TFdVRjZBcWQ2R1lRai9nODlyZDMzMDNVN3lENS9jSEs2dXRvempUUGZXcllmdVUrcHozQlljcjBsTTFRWHNoQjRmM0RRdDZlSklQUEhkeE93SEt0VjdTWUtJMm4rK0tRWTFVbTNkY0VOL2FhRjZndnQrY1BDVkFja1R0Sm5MaHRVSGgwQW5vR3RlKzJxSUY1b3p1ZEtDRWxBQWZSK1NkRUJrSGZyTGUzOE13NXNCN2pteFpuRDhOUURGVzRWa0l5THB2OENlQU9paGh3a2M2SGk5WXNkaEVldkhpQmZqT1lld2dBZWFCVUozOXkwM3NxKzFlRm15akZyRk9yV0ozK2daMDZnYm9sRUg4U1grN1gzY05oZng3dmY3eWpvZzdlbDRXeDJJWVZHZXFqY1gvaFhETXFhWTAxTmY1N1BOU3drYnF2ZkJKRmtXOHR1NzdFQkNrSGs3ZmFUc1dBVW1nRUdrd3RnZ3RrNVhGWkk3d0hnU00yZmlkbkZua0szNUQ3NXZubzNDcTNaR3B3bXN6Smh4REZKMkI0U1pDMUFCbGN2OFBGSmpxeU9sSEhKTHFyMWMxUUNaVS9kclV6ZHdPN3FxZGlRMi9vanZFL1FxSEo2bGFaQVh0QUhkUVFHWENhcFlFa0llMW90VnhiR2Q4SllqMmRHSzFrV0FXVGp0RHQ2dHl6WkNBeFd3TytKUk1Cbk5TQ3djNjlYdUxEc0JnTnJ1a1BKNjVvOVJQYTN5cEgvME9VbHUwdmUwTitoOFAyVjlYM0grdFRoTUJTNVF3OW9oTFQ1ajVWajdFdmdDVzRNOEs4V05LbkFBSEtJZVl1akdGY0F6WnRHclE2aDM0SkZ2R3FoZ2ZGUVJHanc2QWM0VWdZNGJIdm02b0ZaK1BpeGhaU1Exd0J4VkZyZXJWalBUT01yZ3MvdnZ2aEFsVkpNWHpSYkdqSk43QXJkNDk0MkcrR1RMVzRHSk9VSVVvRGtLekZEc3VLU3B1VUEzeCtEWVY0YXc0eEMzL0hpb2RpQTBaRjY2K3h6RVJKODFvYkZQMzRHUXRPSVBSaWtlM2QwS25PaDZxeHVqNm5nUm0yUi9OMURFQURBL0ZZVFQrajFVUDFTeVZqdndSOU40VDJPVnd0WXFEaXpaaHdIbnpWTjVhQnlBT0ZpdW55T0N4bm1sNGlBb24zazl2VzJZM0RxT3NtdDFtRWUza1lWQmk4RG8zY05TVTFCS1IxWWVXWjhLTnR0ckVJbWwwbFkreWFvbHZkOWkybVpXeUMxa0NGRGpJeFYwU3QwejZ3U0ZXOUttSXgwZzNuREZ3cU01aFc5bW4yaG9ycDcrTjIxcUlqNVBwR2t3R0FOTEd4alZqaHNYSVlEdXhhMm5KTUxWcHhNUVVaRkR4MDVreUwyMmQrMmU0OTg0OEZVRGU2S1IzZytwTDBsZWJuMlNvajRjYi9ZbnhETk5oRjd3RDZwZ2VuRmQ3WjNjWVNUd1VRd1FUVDhIVjhHWGpibVdJbXpRc3h0R3V6YUJoKzlVYmswMlZ5NWVnQU5Cb3NHOVpLQkJFT3JMNTZDOFFNNEhuTkwwdXQwRDFIQmgxSzErekh5SXlpMmFQbStxRWp3WDdDb0FVQldkTzBqTmNaUktXOUttMkc4TjIvLzBBZElxVlc5SnUraU5PRzNJTG9IK1AyOFhFSjlXdkF1VkE1YmhRU2hJeHZoT2pNK1l6aHFGdnduN0J2MGVwM3dBVE11MXJDT0xQYlhGSTd0ejkrOC9aemp2MkFBdnZSYW1rPSZtKzlTMitmQ3BDQWVlV290bEs1NjlRV2JWTUE9'
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
                'authority': 'www.pinterest.co.uk',
                'accept': 'application/json, text/javascript, */*, q=0.01',
                'x-pinterest-appstate': 'active',
                'x-app-version': 'a2a392a',
                'x-requested-with': 'XMLHttpRequest',
                'x-pinterest-experimenthash': '8ce911ccc491eeaff4cd32514fc52d66c7f980b0d9f5cbff9ec37ab242afc3f527b2c9e0b71af1574b7b6c3ff0710bca87328e0af67802887d9278b546134edc',
                'user-agent': 'Chrome/81.0.4044.138',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-mode': 'cors',
                'sec-fetch-dest': 'empty',
                'referer': 'https://www.pinterest.co.uk/',
                'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
                'cookie': 'csrftoken=34d8c022b199d4258a6f48e00a1a9aa3; bei=false; cm_sub=denied; logged_out=True; fba=True; g_state={"i_p":1588835383497,"i_l":2}; ujr=1; fbm_274266067164=base_domain=.www.pinterest.co.uk; _auth=1; _pinterest_sess=TWc9PSZ1WUxsbE5zaW1qOUltc1ppV2d3UTZ2emdBRGlOdEJ4dlptU2dvMHB2SlIzN01rVDlxcEFna21ocWNoMGZJT2dBZjR4Qk5yTVgwRlVUR2R2enNHRlVWRnBFYWtGYnkwK3VmZTJ3K2JHakZJMXNUeEZHVHFFaFE4ZFpyZy9FRjBGNnB2S0JEZCtsd3ZhL0xyazBWd0I3d3dJRFRORTFUOHJrYUxmTjF2NnMvK1l0UmZlM004NEdaTi9MTDJLalg5RFY4SG5vV05Md2hNdGJJZHFWelVsTTZyUDlRYld1SmUxZkh0eG9RSitoMGh4VGpWcGVkUGprV1pnRVFmL3hlOWQ4L2JueFd4dnZqZzUxd2FxUDVZTVNCd3lDVS9aZ2VkRlRlOU1WSC8zWTIwWkNtNnhGMHk0RUgzV0hIVURWOGNyZ00rcHd3VExtMmZWeFFxNk02bE1WVklJQnZlMVBHZWFkVEhyRHlrU2dXdmtaTzkvQmlGd050RlNZYzFWV1N5bThWdWs1cGNsS0xLQW5CUWoxTHpuQ1VNQWVtaFVtdGROWHEwcHpySmVrb09uTEdKYkFoTnA3cEo0THNMT25nWWYxejliQTY5M2xvbENUNHpVclNLT05rT2gxMlJTYWtjYTRnVGgycTJ6SmdIWWVOV2U1QjZxbEFHUVNrU1FMbk15VlptVHU2VVVFNXZ4ZGdhRXBHcTB6U2pzVU9sV3JYMjJBRnNwWVd2czQ2K1ovOHdtVnBRUThYWkh4WjlzdE5pUjNzUVBKWldNM21SaWp1akJ5YmFkSjFuVnlDV1JtbzRLUzZxVm1pSkNkaVN2RkFDQi9mY3R1bXczRVArZFYxS1JtNHJYaVFqSmZxaHg2TGVkOE9wYjl2SkpYU2JPRnZBYkhteTlFNGptOXBmRjR4dlJTN0VJZWNBUTdhSUV1elowV3ZYU0dDeUVpOWZ0YitoSUdYQWQyWVVvWmNlT3Q1K0pRNnZOcWYwWlJDVm5YSWNtcTQ1a2NjNGRBTG1hdmhSOE40QnZCN1pUR2ZmVVJGcHJLTXN6Y2xKeGN3ZHpwVWlxMkVSY2g4V1Y2cGlYTUMrT1RsNTFSZytOVTVFeE84Q2hVdW9PcUZMM3VpS3JjWGRVeW0yQWhuTklBNDlaTzhPbnF2aDJyOGxBb1FicCtlN1Qvc2l1UHpJWWdHeDhaaXBHNUtIQUpTZ0hsamdKVkpoNkRjb3hOR3Z3a1YrQVFMYzd3SFFmRzZMTTJVdTZBM2IwNUsyRnVzNkJnM3JqNVVvUFhrSnhoQTQ1Wk9sWXJORHcyZ25BMWxyWGFPT2VWUnZsTVJ2S3dOZGE3ZysvbjAyaHdLcHozSUFRbXJrOEl2ODZpNThKdGFRcXB3MUx5VGd2dzBadmsrQ2tQbFE3RytBc2VYd0Z5aTd6RzVnREI3U2NiZVQxTk9jMjh6eXErbHdNZTN4TzdyelVGNCszY3F6TTIrUFRHMUU4aWVTSzZVbStXZ2tLZ21Va0E3VmlTSlFKN0pqRmlURGFnaTlXY3gxaERKSXRYeDA3R25oZDVWUW9OYmhYaFdHZ3dScCtmek1EUzJkcGF3bzIwa29lcHloMGQ2ZW12YjhWZXFlUmdhWTFka0R1WFVOSUdpQlYvYU9jdWdYSDF3elVLd3c2R25UZFMxT3hDSnF3SUFPVzNPc1JaeTJoR1psZlhpdk0yTzNyM0Z6TVpxalE2WUtlcjRjWVdsZ3J0V3JGY1RqN0FtRWF5K0lrTHo0TUk3R3EyUU12eTJFSkVCM1NubDIzQnN6S2VzK0R3OEpOdEwwSXBOTFlwNm1YdS9HYnhhN2ZLMjlUQ0xKTHJRTWx0OWVHaFVEMDhTQmxVQ083WWlpYmYrbVpZJnVhM3BLN0dYL2NYdlFmb1drQXEvM2h2WHNxcz0=; _routing_id="11b53b90-db40-4e10-9b81-b511e4736845"; sessionFunnelEventLogged=1'
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
                'authority': 'www.pinterest.co.uk',
                'accept': 'application/json, text/javascript, */*, q=0.01',
                'x-pinterest-appstate': 'active',
                'x-app-version': 'b4982f8',
                'x-requested-with': 'XMLHttpRequest',
                'x-pinterest-experimenthash': 'ee4a0545694b2b10cbd40923f509b0ba04c149fca39c75638ab25ec000ee9b482a28d4b2849ce2ef29d2caa0048e08ece68241c227753cb9580be666c6dbb8f7',
                'user-agent': 'Chrome/81.0.4044.138',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-mode': 'cors',
                'sec-fetch-dest': 'empty',
                'referer': 'https://www.pinterest.co.uk/',
                'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
                'cookie': 'csrftoken=34d8c022b199d4258a6f48e00a1a9aa3; bei=false; cm_sub=denied; logged_out=True; fba=True; g_state={"i_p":1588835383497,"i_l":2}; ujr=1; fbm_274266067164=base_domain=.www.pinterest.co.uk; _auth=1; _pinterest_sess=TWc9PSZ1WUxsbE5zaW1qOUltc1ppV2d3UTZ2emdBRGlOdEJ4dlptU2dvMHB2SlIzN01rVDlxcEFna21ocWNoMGZJT2dBZjR4Qk5yTVgwRlVUR2R2enNHRlVWRnBFYWtGYnkwK3VmZTJ3K2JHakZJMXNUeEZHVHFFaFE4ZFpyZy9FRjBGNnB2S0JEZCtsd3ZhL0xyazBWd0I3d3dJRFRORTFUOHJrYUxmTjF2NnMvK1l0UmZlM004NEdaTi9MTDJLalg5RFY4SG5vV05Md2hNdGJJZHFWelVsTTZyUDlRYld1SmUxZkh0eG9RSitoMGh4VGpWcGVkUGprV1pnRVFmL3hlOWQ4L2JueFd4dnZqZzUxd2FxUDVZTVNCd3lDVS9aZ2VkRlRlOU1WSC8zWTIwWkNtNnhGMHk0RUgzV0hIVURWOGNyZ00rcHd3VExtMmZWeFFxNk02bE1WVklJQnZlMVBHZWFkVEhyRHlrU2dXdmtaTzkvQmlGd050RlNZYzFWV1N5bThWdWs1cGNsS0xLQW5CUWoxTHpuQ1VNQWVtaFVtdGROWHEwcHpySmVrb09uTEdKYkFoTnA3cEo0THNMT25nWWYxejliQTY5M2xvbENUNHpVclNLT05rT2gxMlJTYWtjYTRnVGgycTJ6SmdIWWVOV2U1QjZxbEFHUVNrU1FMbk15VlptVHU2VVVFNXZ4ZGdhRXBHcTB6U2pzVU9sV3JYMjJBRnNwWVd2czQ2K1ovOHdtVnBRUThYWkh4WjlzdE5pUjNzUVBKWldNM21SaWp1akJ5YmFkSjFuVnlDV1JtbzRLUzZxVm1pSkNkaVN2RkFDQi9mY3R1bXczRVArZFYxS1JtNHJYaVFqSmZxaHg2TGVkOE9wYjl2SkpYU2JPRnZBYkhteTlFNGptOXBmRjR4dlJTN0VJZWNBUTdhSUV1elowV3ZYU0dDeUVpOWZ0YitoSUdYQWQyWVVvWmNlT3Q1K0pRNnZOcWYwWlJDVm5YSWNtcTQ1a2NjNGRBTG1hdmhSOE40QnZCN1pUR2ZmVVJGcHJLTXN6Y2xKeGN3ZHpwVWlxMkVSY2g4V1Y2cGlYTUMrT1RsNTFSZytOVTVFeE84Q2hVdW9PcUZMM3VpS3JjWGRVeW0yQWhuTklBNDlaTzhPbnF2aDJyOGxBb1FicCtlN1Qvc2l1UHpJWWdHeDhaaXBHNUtIQUpTZ0hsamdKVkpoNkRjb3hOR3Z3a1YrQVFMYzd3SFFmRzZMTTJVdTZBM2IwNUsyRnVzNkJnM3JqNVVvUFhrSnhoQTQ1Wk9sWXJORHcyZ25BMWxyWGFPT2VWUnZsTVJ2S3dOZGE3ZysvbjAyaHdLcHozSUFRbXJrOEl2ODZpNThKdGFRcXB3MUx5VGd2dzBadmsrQ2tQbFE3RytBc2VYd0Z5aTd6RzVnREI3U2NiZVQxTk9jMjh6eXErbHdNZTN4TzdyelVGNCszY3F6TTIrUFRHMUU4aWVTSzZVbStXZ2tLZ21Va0E3VmlTSlFKN0pqRmlURGFnaTlXY3gxaERKSXRYeDA3R25oZDVWUW9OYmhYaFdHZ3dScCtmek1EUzJkcGF3bzIwa29lcHloMGQ2ZW12YjhWZXFlUmdhWTFka0R1WFVOSUdpQlYvYU9jdWdYSDF3elVLd3c2R25UZFMxT3hDSnF3SUFPVzNPc1JaeTJoR1psZlhpdk0yTzNyM0Z6TVpxalE2WUtlcjRjWVdsZ3J0V3JGY1RqN0FtRWF5K0lrTHo0TUk3R3EyUU12eTJFSkVCM1NubDIzQnN6S2VzK0R3OEpOdEwwSXBOTFlwNm1YdS9HYnhhN2ZLMjlUQ0xKTHJRTWx0OWVHaFVEMDhTQmxVQ083WWlpYmYrbVpZJnVhM3BLN0dYL2NYdlFmb1drQXEvM2h2WHNxcz0=; sessionFunnelEventLogged=1; _routing_id="9490e57c-60cd-4399-a1df-8686ee5f3793"'
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
                    'authority': 'www.pinterest.co.uk',
                    'x-pinterest-appstate': 'background',
                    'x-app-version': 'a2a392a',
                    'x-pinterest-experimenthash': '17c966373f5e02a1fb56cfa5a8949700e41ac667be854f62a78b182fecdd4d1e6b18fda301e66055952e2e3c535d1eee20871d23f8cd835332c0b7e30f2e2ab4',
                    'x-b3-traceid': 'e04e819ae7c29e6c',
                    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
                    'content-type': 'application/x-www-form-urlencoded',
                    'accept': 'application/json, text/javascript, */*, q=0.01',
                    'x-b3-spanid': 'a13045aa27628c74',
                    'x-requested-with': 'XMLHttpRequest',
                    'x-csrftoken': '34d8c022b199d4258a6f48e00a1a9aa3',
                    'origin': 'https://www.pinterest.co.uk',
                    'sec-fetch-site': 'same-origin',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-dest': 'empty',
                    'referer': 'https://www.pinterest.co.uk/',
                    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
                    'cookie': 'csrftoken=34d8c022b199d4258a6f48e00a1a9aa3; bei=false; cm_sub=denied; logged_out=True; fba=True; g_state={"i_p":1588835383497,"i_l":2}; ujr=1; fbm_274266067164=base_domain=.www.pinterest.co.uk; _auth=1; _pinterest_sess=TWc9PSZ1WUxsbE5zaW1qOUltc1ppV2d3UTZ2emdBRGlOdEJ4dlptU2dvMHB2SlIzN01rVDlxcEFna21ocWNoMGZJT2dBZjR4Qk5yTVgwRlVUR2R2enNHRlVWRnBFYWtGYnkwK3VmZTJ3K2JHakZJMXNUeEZHVHFFaFE4ZFpyZy9FRjBGNnB2S0JEZCtsd3ZhL0xyazBWd0I3d3dJRFRORTFUOHJrYUxmTjF2NnMvK1l0UmZlM004NEdaTi9MTDJLalg5RFY4SG5vV05Md2hNdGJJZHFWelVsTTZyUDlRYld1SmUxZkh0eG9RSitoMGh4VGpWcGVkUGprV1pnRVFmL3hlOWQ4L2JueFd4dnZqZzUxd2FxUDVZTVNCd3lDVS9aZ2VkRlRlOU1WSC8zWTIwWkNtNnhGMHk0RUgzV0hIVURWOGNyZ00rcHd3VExtMmZWeFFxNk02bE1WVklJQnZlMVBHZWFkVEhyRHlrU2dXdmtaTzkvQmlGd050RlNZYzFWV1N5bThWdWs1cGNsS0xLQW5CUWoxTHpuQ1VNQWVtaFVtdGROWHEwcHpySmVrb09uTEdKYkFoTnA3cEo0THNMT25nWWYxejliQTY5M2xvbENUNHpVclNLT05rT2gxMlJTYWtjYTRnVGgycTJ6SmdIWWVOV2U1QjZxbEFHUVNrU1FMbk15VlptVHU2VVVFNXZ4ZGdhRXBHcTB6U2pzVU9sV3JYMjJBRnNwWVd2czQ2K1ovOHdtVnBRUThYWkh4WjlzdE5pUjNzUVBKWldNM21SaWp1akJ5YmFkSjFuVnlDV1JtbzRLUzZxVm1pSkNkaVN2RkFDQi9mY3R1bXczRVArZFYxS1JtNHJYaVFqSmZxaHg2TGVkOE9wYjl2SkpYU2JPRnZBYkhteTlFNGptOXBmRjR4dlJTN0VJZWNBUTdhSUV1elowV3ZYU0dDeUVpOWZ0YitoSUdYQWQyWVVvWmNlT3Q1K0pRNnZOcWYwWlJDVm5YSWNtcTQ1a2NjNGRBTG1hdmhSOE40QnZCN1pUR2ZmVVJGcHJLTXN6Y2xKeGN3ZHpwVWlxMkVSY2g4V1Y2cGlYTUMrT1RsNTFSZytOVTVFeE84Q2hVdW9PcUZMM3VpS3JjWGRVeW0yQWhuTklBNDlaTzhPbnF2aDJyOGxBb1FicCtlN1Qvc2l1UHpJWWdHeDhaaXBHNUtIQUpTZ0hsamdKVkpoNkRjb3hOR3Z3a1YrQVFMYzd3SFFmRzZMTTJVdTZBM2IwNUsyRnVzNkJnM3JqNVVvUFhrSnhoQTQ1Wk9sWXJORHcyZ25BMWxyWGFPT2VWUnZsTVJ2S3dOZGE3ZysvbjAyaHdLcHozSUFRbXJrOEl2ODZpNThKdGFRcXB3MUx5VGd2dzBadmsrQ2tQbFE3RytBc2VYd0Z5aTd6RzVnREI3U2NiZVQxTk9jMjh6eXErbHdNZTN4TzdyelVGNCszY3F6TTIrUFRHMUU4aWVTSzZVbStXZ2tLZ21Va0E3VmlTSlFKN0pqRmlURGFnaTlXY3gxaERKSXRYeDA3R25oZDVWUW9OYmhYaFdHZ3dScCtmek1EUzJkcGF3bzIwa29lcHloMGQ2ZW12YjhWZXFlUmdhWTFka0R1WFVOSUdpQlYvYU9jdWdYSDF3elVLd3c2R25UZFMxT3hDSnF3SUFPVzNPc1JaeTJoR1psZlhpdk0yTzNyM0Z6TVpxalE2WUtlcjRjWVdsZ3J0V3JGY1RqN0FtRWF5K0lrTHo0TUk3R3EyUU12eTJFSkVCM1NubDIzQnN6S2VzK0R3OEpOdEwwSXBOTFlwNm1YdS9HYnhhN2ZLMjlUQ0xKTHJRTWx0OWVHaFVEMDhTQmxVQ083WWlpYmYrbVpZJnVhM3BLN0dYL2NYdlFmb1drQXEvM2h2WHNxcz0=; sessionFunnelEventLogged=1; _routing_id="f3cb5c1d-3513-495b-9018-0b13d8a9eaea"',
                    'Content-Type': 'application/x-www-form-urlencoded'
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
                    'authority': 'www.pinterest.co.uk',
                    'x-pinterest-appstate': 'active',
                    'x-app-version': 'a59ed29',
                    'x-requested-with': 'XMLHttpRequest',
                    'user-agent': 'Chrome/81.0.4044.138 Safari/537.36',
                    'content-type': 'application/x-www-form-urlencoded',
                    'accept': 'application/json, text/javascript, */*, q=0.01',
                    'x-pinterest-experimenthash': '1877a9b978cc56aa918cfaaca60245cb86f370d795d0df6a787cc9de22aab6c548dee6f6fcceb591bc69204f832b9d0cdf06126fb2045e23a2113ae040a90d7d',
                    'x-csrftoken': '34d8c022b199d4258a6f48e00a1a9aa3',
                    'origin': 'https://www.pinterest.co.uk',
                    'sec-fetch-site': 'same-origin',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-dest': 'empty',
                    'referer': 'https://www.pinterest.co.uk/',
                    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
                    'cookie': 'csrftoken=34d8c022b199d4258a6f48e00a1a9aa3; bei=false; cm_sub=denied; logged_out=True; fba=True; ujr=1; fbm_274266067164=base_domain=.www.pinterest.co.uk; g_state={"i_p":1589952156306,"i_l":3}; _auth=1; _pinterest_sess=TWc9PSZTWmh6dmVZc3RwUmNiMTJCYXg3TnBvRnBWQnQ1QTFWU3lTM0NBTThPOHRzY0dDbkxsaWhxRmwxQWc3cGJyc2hCcTFFM3ZQOVJUbUc1S0lmWFNEc0ljM24wY1NTZ1lWcW9FRENUc0ZuUURxTFFKbzJuQ0hTZi9ma3VtN1dZWUtlaGZuaUs3b1ppT0lnRXp4YWt4OHhIRWlScWpMZE55UHQycXlrMnR3c0Z2Y1FLdWZkeHpqM2Y3RUkzd2RKWTFPWVdpbG9rWVQ5UzZLM2k5MDBUNGptVk1aUXl6UTIyYmp2ZmVJRUgwVU44MFJCR254RDFudTV0VjUzR2lzQnhxcmF6aWR4ZHBmdXhCTTVndEQ2MkI3ejRTY200ZnJScWs5dU9mZEN6OUx0cWs1bURNbllqTFQ2WWZnSmNjdXc1Q2pzMHAyaVFHQzFNZDlyS0tzY1BSMWpyaHRrVTY2SnBrZHhxLzl1ZExpbVd1c2gybnNsZHRzSDZJN3RzZnBRZ01JaG4zcnNVRnNXMGZRb1Y0djJ2Mld2VnF5V1NIendmZDZVUEd2eEJvVmJvUmc1NXduMDlaODk4VTlWSFRKSkVtVStIT3UzWnlWSm1SRllEQnZhM3U1bEZRT25OQmRyMWpyZzRheEUveklUc2V3aE0rZ3prb3psZ25uL0JvUjFkTGJLNmtLMSswWGc0dG5SQzA3MmE2dGpwUzJsSU81bmdxZ1FpWjVSL1piSjhVdXZTWE9xY09jUmVHZWxTaU5sVjcvRkdZd25tZXFDWWZTUjd0MVNWakJtUS9DTXNNbDRWbXhlb09wQWtQTVZDbllJVjFiaGRRSUx6eGxDWUViSEw4QmpKeGNVcGFDNDd1QkJzd1VqTFcycW95Wldkcnpsbm96U3BpSlNtVUR1MnJ2L0JpYlFKTE0zUy9ORU9VVURQK0p6NW81RFZ0c2llRGlQamNaRjZoamw5QWFJRlEza0QrdG8zTDJSM3Y0Y0JzZFd6a050Vk1KR0JHSlhlZmdDRUtiRXJtMHJhN3RYakFCNTJ6d3dCUHhnM1NmQWI3aDAyRUhzS0NhbDJLS2VsNHllc1d4YzVWejlYbWhjK3hhaHIvOG1IS2loL3M4anREbnhJMldEdVZja1Jpb0crWE1HVnd2clNRREs3cGlxa21mUEtZWG5PblU3UGVOWVF0VGp6c2hUUE5EeExDOHZoaUIxZXByeXhFeXdFblVyYmxaclhkQTRzM3BjTG5Oc3lxRWhuc04ramhsQ1AwS0xCcVJ0N2gvSmZMKzAvVXdnVnhrSzBpYkRtRmUwampHRjB1Y3BNbE5YbjdSc0V5Q2NHNzBlRkhUUm5Lc3pkYW5mZUxMazBTazBuKy95KzhmL1RFV1M1TXA3a1RxSHllWjBxK2tJeDZWTG9kOHp4ZnZ5Rnp5Umkyc3BNVzJEMDI0dk1TVko3UHo0S21Kd29rVlpVYnVhVEh3QUV2bTdtZ2hEQ1kyOFloSU9LU05oVExOMWhhbElhSkgvMGtXbEM5VkVOSHR0a3RtblpWTHlFOFZDN3lEQzhQUGxnWERMTUZhZEhOalU5dmhMWU00MTF5T1NQZVE2RUJmUi96aC8wb2dIazJHeVlIMVJHQzIrZWR4ZjI5UUYySkhaTms5eXV1TS9NTngxYUlzTXI1cVNseGFBTGY1L0dmeTFIeGFGVy9oY0hCVXVqdDBtdUxhKzZia0dEdzczK1NLamVVS0ppbWgzTmFJdEtXVzZwK0JSaVQrNzdlME41YWRaeU5QVXBQd25HdlV3dUxZTnRGV1JCZnREZnRHVTM5cWswUXBTN3p1c3R3UmFTMkgySnorUWdRZVVFWnNGSDhySThyN25EaG83QjAvOHB2ckJsSm52cHVhTGk5Wk5oekNRSkZCMGVLM0YvR25ySGJvVWRsQk95T0RNTVYyQXR4VVNJSGJLQjNrWDN4dTJlT3J5YThveVY5R2hQUG4vZzlacER6YjdKMGc9PSY2S3JNUW9JeUMrRXYvTjZsY1hWR0dPQi9zZE09; sessionFunnelEventLogged=1; _routing_id="cd08e9c5-a15c-4f33-824d-d748ea3e2404"',
                    'Content-Type': 'application/x-www-form-urlencoded'
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