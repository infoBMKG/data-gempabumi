import requests
import xml.etree.ElementTree as ET
import json

baseURL = "https://data.bmkg.go.id/DataMKG/TEWS/"
autogempaURL = baseURL+"autogempa.xml"
gempaterkiniURL = baseURL+"gempaterkini.xml"
gempadirasakanURL = baseURL+"gempadirasakan.xml"


def autogempa():
    dataXML = requests.get(autogempaURL).text
    root = ET.fromstring(dataXML)
    
    dataJSON = {}
    
    #Ada 12 parameter gempa
    
    #Parameter 0-2
    for x in range(0,3):
        dataJSON[root[0][x].tag] = root[0][x].text
    #Mengubah key dan element/value parameter 2
    dataJSON[root[0][3][0].tag] = root[0][3][0].text #Mengubah key "point" menjadi key "coordinates" . Mengubah element/value dari "None" menjadi koordinat yang sesuai
    
    #Parameter 4-12
    for x in range(4,len(root[0])):
        dataJSON[root[0][x].tag] = root[0][x].text
    
    dataJSON[root[0][11].tag] = baseURL+root[0][11].text #Mengubah nama file "ABC.jpg" menjadi url file "https://example.com/ABC.jpg"
    
    return json.dumps(dataJSON)
    #return dataJSON #Return sebagai dictionary

def gempaterkini():
    dataXML = requests.get(gempaterkiniURL).text
    root = ET.fromstring(dataXML)

    dataJSON = {}
    gempa = {}
    
    for x in range(0,15): # Ada 15 list gempa terkini
        
        #Ada 10 parameter gempa
        
        #Parameter 0-2
        for y in range(0,3):
            gempa[root[x][y].tag] = root[x][y].text
        #Mengubah key dan element/value parameter 2
        gempa[root[x][3][0].tag] = root[x][3][0].text #Mengubah key "point" menjadi key "coordinates" . Mengubah element/value dari "None" menjadi koordinat yang sesuai
        
        #Parameter 3-9
        for y in range(4,10):
            gempa[root[x][y].tag] = root[x][y].text
        
        #Memasukkan 15 dict gempa menjadi 1 dict dataJSON
        dataJSON["gempa{0}".format(x)] = dict(gempa)
    
    return json.dumps(dataJSON) #Return sebagai JSON
    #return dataJSON #Return sebagai dictionary

def gempadirasakan():
    dataXML = requests.get(gempadirasakanURL).text
    root = ET.fromstring(dataXML)

    dataJSON = {}
    gempa = {}
    
    for x in range(0,15): # Ada 15 list gempa dirasakan
        
        #Ada 10 parameter gempa
        
        #Parameter 0-2
        for y in range(0,3):
            gempa[root[x][y].tag] = root[x][y].text
        #Mengubah key dan element/value parameter 2
        gempa[root[x][3][0].tag] = root[x][3][0].text #Mengubah key "point" menjadi key "coordinates" . Mengubah element/value dari "None" menjadi koordinat yang sesuai
        
        #Parameter 3-9
        for y in range(4,10):
            gempa[root[x][y].tag] = root[x][y].text
        
        #Memasukkan 15 dict gempa dirasakan menjadi 1 dict dataJSON
        dataJSON["gempa{0}".format(x)] = dict(gempa)
    
    return json.dumps(dataJSON) #Return sebagai JSON
    #return dataJSON #Return sebagai dictionary    
