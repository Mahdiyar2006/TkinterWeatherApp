import tkinter
import tkinter as tk
import tkinter.messagebox as mb
import requests
import urllib.request


def check_internet(host='https://google.com'):
    try:
        urllib.request.urlopen(host)
        return True
    except:
        mb.showerror('Error', 'You are offline')
        return False


def get_weather(q):
    if check_internet():
        api_url = "http://45.147.77.122/api/weather?city=" + q
        response = requests.get(api_url)
        return response.json()
    return False


window = tk.Tk()
window.configure(bg='white')
window.geometry("390x50")

frameCity = tk.Frame(bg='white')
frameButton = tk.Frame(bg='white', border=10)
lblCity = tk.Label(master=frameCity, text="City:", bg='white', borderwidth=10)
txtCity = tk.Entry(master=frameCity, width=37)


def get_city():
    return txtCity.get()


def show_temp():
    weather = get_weather(get_city())
    if weather != False:
        try:
            city = weather["data"][0]["city_name"]
            temp = str(weather["data"][0]["temp"])
            msg = 'Temp in ' + city + " is " + temp + " now."
        except:
            msg = "City not find"
        mb.showinfo('Temp', msg)


button = tk.Button(master=frameButton, text="   Get   ", command=show_temp)

lblCity.pack(side=tk.LEFT)
txtCity.pack(side=tk.LEFT)
frameCity.pack(side=tk.LEFT)
frameButton.pack(side=tk.RIGHT)
button.pack()

window.mainloop()
