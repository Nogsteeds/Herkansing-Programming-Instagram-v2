from iNStagram.file_io.fileio import *
from iNStagram.api_requests.app_requests import request_instagram
from tkinter import *
import webbrowser

__author__ = 'Freek'

sla_stationsgegevens_op()
startscherm = Tk()
startscherm.title('Foto of video in de buurt!')
startscherm.minsize(width=790, height=600, )
startscherm.configure(bg='white')
infolabel = Label(startscherm, fg='blue', text='Voer een station in')
infolabel.place(x=0, y=0)

e = Entry(master=startscherm, fg='black')
e.place(x=93, y=480)

T = Text(startscherm, height=25, width=120, bg='white', fg='black')
T.pack()

def openHLink(event):
  #Pas links aan zodat deze in een browser geopend kunnen worden.
  start, end = T.tag_prevrange("hlink",
                               T.index("@%s,%s" % (event.x, event.y)))
  webbrowser.open_new(T.get(start, end))

T.tag_configure("hlink", foreground='blue', underline=1)
T.tag_bind("hlink", "<Control-Button-1>", openHLink)




def weergeef_instagram_links():
    """
    Kijk in de stations dict of het ingevulde station er in zit. Weergeef vervolgens de geposte instagram media.
    stationnaam: geef ofwel kort, middel als lange stationnaam om de bijbehorende station te identificeren
    :type stationnaam: string
    :type stations en instagram_data_dict: dict
    """
    T.delete(1.0, END)
    stationnaam = e.get()
    stations = lees_stationgegevens()
    for station in stations:
        if stationnaam in station["namen"].values():
            print("Station gevonden")
            lat, lon = station["locatie"]
            lat = float(lat)
            lon = float(lon)
            instagram_data_dict = request_instagram(lat, lon)
            for data in instagram_data_dict:
                import datetime
                regeltekst = "%-30s %s %s"%(data["plaatsnaam"],datetime.datetime.fromtimestamp(data["tijd"]), data["type"])
                T.insert(END, data["link"], "hlink", regeltekst + '\n')
    else:
     print("Geen station gevonden")



b = Button(master=startscherm, text="Zoek naar media", width=20, height=3, bg='blue', fg='white',
           command=weergeef_instagram_links)
b.place(x=93, y=500)

startscherm.mainloop()
