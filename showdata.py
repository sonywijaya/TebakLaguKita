import sqlite3
conn = sqlite3.connect('song_titles.db')
c = conn.cursor()
sqlID = "SELECT ID FROM song"
sqlTitle = "SELECT title FROM song"
sqlLoc = "SELECT location FROM song"
sqlCharID = "SELECT ID FROM character"
sqlCharTitle = "SELECT title FROM character"
sqlCharStat = "SELECT status FROM character"
sqlCCharLoc = "SELECT Clocation FROM character"
sqlBWCharLoc = "SELECT BWlocation FROM character"

def readID(n):
    i = 0
    data = [None]*14
    for row in c.execute(sqlID):
        data[i]=str(row).replace('(','').replace(')','').replace(',','').replace("'",'')
        i += 1
    return data[n-1]

def readTitle(n):
    i = 0
    data = [None]*14
    for row in c.execute(sqlTitle):
        data[i]=str(row).replace('(','').replace(')','').replace(',','').replace("'",'')
        i += 1
    return data[n-1]

def readLoc(n):
    i = 0
    data = [None]*14
    for row in c.execute(sqlLoc):
        data[i]=str(row).replace('(','').replace(')','').replace(',','').replace("'",'')
        i += 1
    return data[n-1]

def readCharID(n):
    i = 0
    data = [None]*3
    for row in c.execute(sqlCharID):
        data[i]=str(row).replace('(','').replace(')','').replace(',','').replace("'",'')
        i += 1
    return data[n-1]

def readCharTitle(n):
    i = 0
    data = [None]*3
    for row in c.execute(sqlCharTitle):
        data[i]=str(row).replace('(','').replace(')','').replace(',','').replace("'",'')
        i += 1
    return data[n-1]

def readCCharLoc(n):
    i = 0
    data = [None]*3
    for row in c.execute(sqlCCharLoc):
        data[i]=str(row).replace('(','').replace(')','').replace(',','').replace("'",'')
        i += 1
    return data[n-1]

def readBWCharLoc(n):
    i = 0
    data = [None]*3
    for row in c.execute(sqlBWCharLoc):
        data[i]=str(row).replace('(','').replace(')','').replace(',','').replace("'",'')
        i += 1
    return data[n-1]

def readCharStat(n):
    i = 0
    data = [None]*3
    for row in c.execute(sqlCharStat):
        data[i]=str(row).replace('(','').replace(')','').replace(',','').replace("'",'')
        i += 1
    return data[n-1]

def addScore(n):
    
    c.execute("INSERT INTO scores VALUES("+n+",(SELECT SUM(score) FROM scores))")
    conn.commit()

def getScore():
    for row in c.execute("SELECT total FROM scores"):
        total = str(row).replace('(','').replace(')','').replace(',','').replace("'",'')
    return total

def getLevelTarget():
    i = 0
    target = [None]*3
    for row in c.execute("SELECT targetpts FROM leveling"):
        target[i] = str(row).replace('(','').replace(')','').replace(',','').replace("'",'')
        i += 1
    return target

def getLevelName():
    i = 0
    lvlname = [None]*3
    for row in c.execute("SELECT name FROM leveling"):
        lvlname[i] = str(row).replace('(','').replace(')','').replace(',','').replace("'",'')
        i += 1
    return lvlname

def getLevel():
    currentScore = getScore()
    targetLevel = getLevelTarget()
    lvlName = getLevelName()
    i = 0
    for row in targetLevel:
        if int(currentScore) > int(targetLevel[i]):
            level = lvlName[i]
            c.execute("UPDATE character SET status=1 WHERE ID="+str(i+1)+"") 
        i +=1
    return str(level).replace('(','').replace(')','').replace(',','').replace("'",'')

def chooseChar(n):
    c.execute("INSERT INTO charchoosen VALUES("+str(n)+")")
    conn.commit()

def retrieveChar():
    for row in c.execute("SELECT ID FROM charchoosen"):
        selectedChar = str(row).replace('(','').replace(')','').replace(',','').replace("'",'')
    return selectedChar

def showMsg(n):
    i = 0
    msg = [None]*3
    for row in c.execute("SELECT sentence FROM character"):
        msg[i]=str(row).replace('(','').replace(')','').replace(',','').replace("'",'')
        i += 1
    return str(msg[n-1])
    
    
