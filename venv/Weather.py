from tkinter import *
import googlemaps
import json
import urllib.parse
import urllib.request

def show_weather():
    name_place = entryName.get()
    gm = googlemaps.Client(key='AIzaSyB5GBK4ZHMqsmvSV6yWwE9gUw-T26MXnlM')
    geocode_result = gm.geocode(name_place)
    # print(json.dumps(geocode_result,indent=4))
    lttude = geocode_result[0]['geometry']['location']['lat']
    lngtude = geocode_result[0]['geometry']['location']['lng']


    values={'lat':lttude,'lon':lngtude,'appid':'c57ddae96b37c9e72ec74923a606230a'}
    data = urllib.parse.urlencode(values)
    #print(data)
    #data = data.encode('utf-8')
    #req = urllib.request.Request(url,data)
    #resp = urllib.request.urlopen(req)
    url = "http://api.openweathermap.org/data/2.5/weather?%s" %data
    #resp = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?lat=30.8039183&lon=76.0333885&appid=c57ddae96b37c9e72ec74923a606230a')
    resp = urllib.request.urlopen(url)
    d = resp.read()
    #print(d)
    #print('----------------------------------------')
    data = d.decode('utf-8')
    #print(data)
    #print('----------------------------------------')
    jdata = json.loads(data)
    lt = jdata['coord']['lat']
    ln = jdata['coord']['lon']
    des = jdata['weather'][0]['description']
    max_t = jdata['main']['temp_max']
    min_t = jdata['main']['temp_min']
    name = jdata['name']
    #print(jdata)
    #print('----------------------------------------')
    w_des = ''' Name of entered palce = {},
    lat = {} and lon = {}
    condition of data = {},
    maximum temprature = {},
    minimum tempreture = {}'''.format(name,lt,ln,des,max_t,min_t)
    msg = Message(root, text=w_des, font=('times', 10, 'italic')).pack()


root = Tk()

root.geometry('500x400')
root.title('Weather Info....')
# root.config(background='Sky Blue')

lbl = "Weather Information Of The Place You Enter in the Entry Box."
msg = Message(root, text=lbl)
msg.config(font=('times', 16, 'italic'), width='400', fg='Red')
msg.pack()

lblName = Label(root, text="Enter The Name of Place:::", bd=20, font="Times 24")
lblName.pack()

entryName = Entry(root, width='50', bd=5)
entryName.pack()

spacer1 = Label(root, bd=5).pack()

btnSubmit = Button(root, text="Submit", bg='brown', fg='white', pady=8, padx=15, bd=5, command=show_weather)
btnSubmit.pack()

root.mainloop()

