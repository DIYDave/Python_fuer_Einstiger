import requests, json, time
import PySimpleGUI as sg

def make_window():
    sg.theme("DarkRed1") # "DarkGrey11"
    menu_def = [['&Application', ['E&xit']],['&Help', ['&About']] ]
    col1 =  [[sg.Menu(menu_def, key='-MENU-')],
            [sg.Text('Videos:')], #, relief=RELIEF_SUNKEN
            [sg.Text('Abos:')],
            [sg.Text('Views:')]]
            
    col2 =  [[sg.Text(k="-VIDCOUNT-", text="-", background_color="DimGray", auto_size_text=False, size=(6,1), justification="right")],
            [sg.Text(k="-SUBCOUNT-", text="-", background_color="DimGray", auto_size_text=False, size=(6,1), justification="right")],
            [sg.Text(k="-VIEWCOUNT-", text="-", background_color="DimGray", auto_size_text=False, size=(6,1), justification="right")]]

    layout = [[sg.Column(col1),sg.Column(col2)],[sg.Text(k='TIME')]]          
    return sg.Window('YT Stat', layout,  finalize=True,no_titlebar=True,grab_anywhere=1)


def get_statistics():
    parameters = {
        'part' : 'statistics',
        'key' :"xXxX",      # Add your own key here
        'id' : "yYyY"      # Add a Youtube channel ID here
        }
    response = requests.get("https://www.googleapis.com/youtube/v3/channels", params=parameters)
    json_dict= json.loads(response.text)
    stat_dict = {}
    stat_dict['viewCount'] = json_dict['items'][0]['statistics']['viewCount']
    stat_dict['subscriberCount'] = json_dict['items'][0]['statistics']['subscriberCount']
    stat_dict['videoCount'] = json_dict['items'][0]['statistics']['videoCount']
    return stat_dict


def main():
    window = make_window()
    window.TKroot.wm_attributes("-topmost", 1)
    timeout = 0
    while True:
        event, values = window.read(timeout)
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        stat_dict = get_statistics()
        window["-VIDCOUNT-"].update(stat_dict['videoCount'])
        window["-SUBCOUNT-"].update(stat_dict['subscriberCount'])
        window["-VIEWCOUNT-"].update(stat_dict['viewCount'])
        window['TIME'].update(time.asctime())
        timeout = 600000        # Refresh every 10 minutes
        
if __name__ == '__main__':
     main()
