from iNStagram.file_io.fileio import lees_stationgegevens

__author__ = 'Freek'


#we gaan er nu vanuit dat het bestand al is opgeslagen anders kun je de andere functies gebruiken
def geef_station(stationnaam):
    """
    Geeft de bijbehorende station dict uit de lijst van alle stations (in de NS API)
    :param stationnaam: geef ofwel kort, middel als lange stationnaam om de bijbehorende station te identificeren
    :type stationnaam: str
    :return: station dict met namen en locatie
    :rtype: dict
    """
    stations = lees_stationgegevens()
    for station in stations:
        if stationnaam in station["namen"].values():
            return station



if __name__ == '__main__':
    station = geef_station("Hilversum Sportpark")#hij weet dat t n dict is..!
    print(station["locatie"])


auth_details_ns = ('freek.zandwijk@student.hu.nl', '0gZFU8fHjROwswm1XxvG5H4AY8LKVWwadMbc78h7T1J8n18hE6n5FQ')
response_ns = requests.get('http://webservices.ns.nl/ns-api-stations-v2', auth=auth_details_ns)
response_instagram = requests.get('https://api.instagram.com/v1/media/search?lat=48.858844&lng=2.294351&access_token=2371137240.1677ed0.f05412253449452f86d9a51828da4d7d')

def verwerk_ns(response):
    """Maak van de response een document dat kan worden uitgelezen."""
    bestand = open('stations.xml', 'w')
    bestand.write(str(response_ns.text))
    bestand.close()


startscherm = Tk()
startscherm.title('Foto of video in de buurt!')
startscherm.minsize(width=790, height=600,)
achtergrondlabel = Label(startscherm, bg='yellow')
achtergrondlabel.place(x=0, y=0)

e = Entry(master=startscherm, fg='white')
e.place(x=93,y=480)

def nieuwe_window():
    """Sluit het venster en open een ander venster."""
    startscherm.withdraw()
    linkscherm = Tk()
    linkscherm.title('Instagram links')
    linkscherm.minsize(width=990, height=700)
    linkscherm.configure(bg='yellow')
    def teruggaan():
        """Sluit het venster en open een ander venster."""
    linkscherm.withdraw()
    startscherm.deiconify()
    terugknop = Button(master=linkscherm, text='Terug', width=20, height=3, bg='blue', fg='white', command=teruggaan)
    terugknop.place(x=607, y=490)
    linkscherm.focus_set()



def verwerk_instagram():
    """Haal gegevens van op instagram recent geposte media op"""
    response_instagram = requests.get('https://api.instagram.com/v1/media/search?lat=48.858844&lng=2.294351&access_token=2371137240.1677ed0.f05412253449452f86d9a51828da4d7d')
    data = response_instagram.json(response_instagram.text)


def vraag_station_aan_gebruiker():
    """"Open een venster met een veld voor input.
    De gebruiker vult station in"""
    pass

def vergelijk_met_instagram():
    """Haal de gegevens lat en long van het ingevulde station op.
    Vergelijk de gegevens via Instagram of er iets in de buurt is gepost.
     Zet de URLs van alle media binnen een straal van 1 kilometer in
      de GUI zodat men deze kan overnemen"""
    station = e.get()
    bestand1 = open('instagram.json', 'r')
    bestand2 = open('stations.xml', 'r')
    xml_string = bestand2.read()
    dict_met_stations = xmltodict.parse(xml_string)
    t = []
    for station in dict_met_stations:
        lat = station["Lat"]
        lng = station["Lon"]

            for links in bestand1:
                if links ["Lat"]["Lon"] ==  station["Lat"]["Lon"]:
                    t.append(links)




    pass

def maak_overzicht():
    """"Kijk naar hoeveel media is gepost en wanneer.
    Scheid de media op basis van het type zoals
    foto of video."""
    pass

def extra_url_in_browser_of_gui():
    """Als er op een link wordt geklikt,
    open een browser of geef deze weer in de GUI.
    Wanneer de media in de GUI wordt weergeven kan men
    dit ook weer sluiten om terug te gaan."""
    pass

def vergelijk_met_instagram():
    """Haal de gegevens lat en long van het ingevulde station op.
    Vergelijk de gegevens via Instagram of er iets in de buurt is gepost.
     Zet de URLs van alle media binnen een straal van 1 kilometer in
      de GUI zodat men deze kan overnemen"""
    station = e.get()
    bestand1 = open('instagram.json', 'r')
    bestand2 = open('stations.xml', 'r')
    xml_string = bestand2.read()
    dict_met_stations = xmltodict.parse(xml_string)
    t = []
    for station in dict_met_stations:
        lat = station["Lat"]
        lng = station["Lon"]

            for links in bestand1:
                if links ["Lat"]["Lon"] ==  station["Lat"]["Lon"]:
                    t.append(links)


def verwerk_instagram():
    """Haal gegevens van op instagram recent geposte media op"""
    response_instagram = requests.get('https://api.instagram.com/v1/media/search?lat=48.858844&lng=2.294351&access_token=2371137240.1677ed0.f05412253449452f86d9a51828da4d7d')
    data = response_instagram.json(response_instagram.text)

"%-30s %s %s %s %s" %