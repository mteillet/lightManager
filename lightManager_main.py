# lightManager_main.py
import os
import re


# MAIN ONLY FOR DEBUGGING PURPOSES
def main():
    #readDictionnary()
    initDictionnary()

# CHECKING IF THERE IS A LIB/LIGHT FOLDER AND RETURN THE FOUND LIGHTS IF THERE IS A .MGS IN ITS  FOLDER
def scanDir():
    ####    INIT THE SEARCH FOR THE LIB FOLDER
    # Check if the LIB/LIGHT FOLDER CAN BE FOUND
    listDir = os.listdir()
    lightFolder = []
    for i in listDir:
        if i == "LIB":
            lightDir = os.listdir(i)
            for x in lightDir:
                if x == "LIGHT":
                    print('path to LIB/LIGHT/ has been found')
                    lightFolder.append(i)
                    lightFolder.append(x)
    try:
        pathToLightFolder = lightFolder[0] + '/' + lightFolder[1]
    except:
        print("COULD NOT LOCATE THE LIB/LIGHT/ folder location")

    # List the directories in the LIB/LIGHT FOLDER IF THEY CONTAIN A .MGS FILE
    listLights = os.listdir(pathToLightFolder)
    for i in listLights:
        temp = i.split('.')
        if len(temp) != 1:
            listLights.pop(listLights.index(i))
    correctLight = []

    for i in listLights:
        file = (os.listdir(pathToLightFolder + "/" + i))
        for x in file:
            match = re.search('\.mgs$', x)
            if match:
                print('Correct light has been found -- ', x)
                correctLight.append(pathToLightFolder + "/" + i + "/" + x)

    return(correctLight)

def createDictionnary(correctLight):
    print('####    DICTIONNARY INIT    ####')
    # Creating a dictionnary of the parsed lights
    lightDictionnary = {}
    dictionnaryList = []

    # Splitting the correctLight list 
    current = 0
    for i in correctLight:
        # Splitting the list to get the correct elements
        splittedTemp = (correctLight[current].split('/'))
        print(splittedTemp)
        # Keeping a variable in order to have somewhere to write the dicts to
        outputFolder = str(splittedTemp[0] + '/' + splittedTemp[1] + '/')
        lightDictionnary['fullPath'] = i
        lightDictionnary['name'] = splittedTemp[(len(splittedTemp)-2)] 
        lightDictionnary['mgs'] = splittedTemp[(len(splittedTemp)-1)] 
        
        #### CHECKING IF AN ICON EXISTS IN THE FOLDER BEFORE CREATING IT IN THE DICT
        rootLightFolder = ('/'.join(splittedTemp[:-1]))
        lgtDir= os.listdir(rootLightFolder)
        '''
        Icon toggle because there could be many files, and it needs to still be true if there's a
        single one which is an icon
        '''
        iconToggle = False
        for i in lgtDir:
            match = re.search('\.jpeg$',i)
            if match:
                lightDictionnary['icon'] = str(rootLightFolder)+'/'+i
                iconToggle = True
        # Adding an empty icon attribute to the dictionnary if there is no icon
        if iconToggle == False:
            lightDictionnary['icon'] = None

        dictionnaryList.append(lightDictionnary)
        # Resetting the lightDictionnary, otherwise it writes the same output every time
        lightDictionnary = {}
        current += 1
        
    # Output the list of dictionnaries to a lightDictionnaries File in the output folder
    outputFile = outputFolder + 'lightDictionnaries.json'
    with open(outputFile, 'w') as json:
        for i in dictionnaryList:
            print(i, file=json)
    
def readDictionnary():
    # First check if the dictionnary can be accessed
    pathToDic = 'LIB/LIGHT/lightDictionnaries.json'
    lightDict = []
    
    try:
        with open(pathToDic, 'r') as json:
            for i in json:
                lightDict.append(eval(i[:len(i)-1]))
        json.close()
        print('FOUND THE LIGHT DICTIONNARY')
        return(lightDict)
    except:
        print('COULD NOT FIND THE LIGHT LIBRARY JSON FILE : ' + pathToDic) 
        initDictionnary()

def checkIcon(i, dictionnary):
    print('CHECK IF ICON EXISTS')

def initDictionnary():
    correctLight = scanDir()
    createDictionnary(correctLight)

def getDictBasedOnName(name, dictionnary):
    for i in dictionnary:
        if name == i['name']:
            print('MATCHED ' + name + ' TO ' + str(i['name']))
            return(i)
        else:
            pass

if __name__ == "__main__":
    main()
