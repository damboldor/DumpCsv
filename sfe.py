# sfe.
import csv

FileName = ''
ListDb = []

def Load(file):
    '''
    Loads the file to facilitate the encoding process.
    '''
    global FileName
    FileName += file
    #print("Load.. " + FileName + " - OK.")

def Read():
    '''
    Puts data into an array: ListDb.
    '''
    with open(FileName, "r", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            ListDb.append(row)

def Write(*rw):
    '''
    Writes data to the end of the file.
    '''
    with open(FileName, "a", newline="") as file:
        rec = [*rw]
        writer = csv.writer(file)
        writer.writerow(rec)

def Update(t, *kv):
    '''
    Updates the data in the file.
    '''
    with open(FileName, "r", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            ListDb.append(row)
    with open(FileName, "w", newline="") as file:
        writer = csv.writer(file)
        ListDb[t] = [*kv]
        writer.writerows(ListDb)
