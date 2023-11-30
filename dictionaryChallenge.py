##DICTIONARY CHALLENGE
##Create a dictionary.
airportDict={
    'AirportCode': 'AOC',
    'AirportName':'Altenburg Nobitz Airport',
    'AirportMunicipality':'Altenburg',

    }
print(airportDict)

##Use the get() method on a dictionary.
x=airportDict.get('AirportCode')
print(x)
    
##Change a value within a dictionary.

airportDict['AirportName']='Leipzig Altenburg Airport'
print(airportDict)
##Add an item to a dictionary.
airportDict['AirportCountry']=['Germany']
print(airportDict)
##Create a nested dictionary.
peopledict={1:{'IDNo': 1,'Color':'green','Name':'Foxtrot Oscar'},
            2:{'IDNo':2,'Color':'teal','Name':'Alfa Tango'},
            3:{'IDNo':3,'Color':'aquamarine','Name':'India Juliet'},
            4:{'IDNo':4,'Color':'mauve','Name':'Mike November'}}
print(peopledict)
print(peopledict[4]['Name'])
##Use the fromkeys() method on a dictionary.
x=('alpha','bravo','charlie')
y=1
thisdict=dict.fromkeys(x,y)
print(thisdict)
