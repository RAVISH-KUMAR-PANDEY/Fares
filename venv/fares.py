import googlemaps
from tkinter import *
from uber_rides.session import Session
from uber_rides.client import UberRidesClient


def Uber(lat_pick,lng_pick,lat_drop,lng_drop):
    session = Session(server_token='UdDKS3pOPxUrc7NFaTk9TVfcgI9CE8PfmQcL-_m8')
    client = UberRidesClient(session)
    response = client.get_price_estimates(
        start_latitude=lat_pick,
        start_longitude=lng_pick,
        end_latitude=lat_drop,
        end_longitude=lng_drop,
        seat_count=2
    )

    estimate = response.json.get('prices')
    print(estimate[0]['estimate'])
    return estimate[0]['estimate']



def onClick():

    gm = googlemaps.Client(key='AIzaSyB5GBK4ZHMqsmvSV6yWwE9gUw-T26MXnlM')

    str_pick = entryPick.get()
    str_drop = entryDrop.get()

    geocode_result_pickup = gm.geocode(str_pick)[0]
    geocode_result_drop = gm.geocode(str_drop)[0]

    lat_pick = geocode_result_pickup['geometry']['location']['lat']

    lng_pick = geocode_result_pickup['geometry']['location']['lng']

    lat_drop = geocode_result_drop['geometry']['location']['lat']

    lng_drop = geocode_result_drop['geometry']['location']['lng']


    add_drop = geocode_result_drop['formatted_address']
    add_pick = geocode_result_pickup['formatted_address']
    print("Pick from : ",add_pick)
    print("Drop At : ",add_drop)
    print("PICK UP LAT LON")
    print(lat_pick)
    print(lng_pick)
    print("DROP  POINT LAT LONG")
    print(lat_drop)
    print(lng_drop)
    fare=Uber(lat_pick,lng_pick,lat_drop,lng_drop)
    strout = "Your UberGo from {} to {} will cost you around {} .".format(add_pick,add_drop,fare)

    entryOutput["text"]=str(strout)

root = Tk()
root.config(background="yellow")

lblTitle = Label(root,text="CABS HATKE",font=("Helvetica", 25,"bold","underline"),foreground="red",)
lblTitle.pack()

entryxyz3 = Label(root,background="yellow",height=2,width=2)
entryxyz3.pack()


lblPickLoc = Label(root,text="Enter PickUp Location :",font=("Helvetica", 16,"bold"),foreground="blue")
lblPickLoc.pack()

entryxyz4 = Label(root,background="yellow",height=1,width=2)
entryxyz4.pack()


entryPick = Entry(root,font=("Helvetica", 16))
entryPick.configure({"background": "black","foreground":"white","width":"40"})
entryPick.pack()

entryxyz2 = Label(root,background="yellow",height=1,width=2)
entryxyz2.pack()


lblDropLoc = Label(root,text="Enter Drop Down Location :",font=("Helvetica", 16,"bold"),foreground="blue")
lblDropLoc.pack()

entryxyz6 = Label(root,background="yellow",height=1,width=2)
entryxyz6.pack()


entryDrop = Entry(root,font=("Helvetica", 16))
entryDrop.configure({"background": "black","foreground":"white","width":"40"})
entryDrop.pack()

entryxyz1 = Label(root,background="yellow",height=2,width=2)
entryxyz1.pack()


btnSubmit = Button(root,text="Compare Fares" ,command=onClick,font=("Helvetica", 16,"bold"),foreground="green",background="black")
btnSubmit.pack()

entryxyz = Label(root,background="yellow",height=2,width=2)
entryxyz.pack()

entryOutput = Label(root,height=100,width=200, wraplength=200 ,font=("Helvetica", 10,"bold"),foreground="red",background="yellow")
entryOutput.pack()



root.mainloop()
