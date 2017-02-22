import sqlite3
conn = sqlite3.connect('song_titles.db')
c = conn.cursor()

def tableCreate():
    c.execute("CREATE TABLE song(ID INT, title VARCHAR(30), location VARCHAR(30))")
    c.execute("CREATE TABLE character(ID INT, title VARCHAR(20), sentence VARCHAR(30), Clocation VARCHAR(30), BWlocation VARCHAR(30), status INT)")
    c.execute("CREATE TABLE scores(score INT, total INT)")
    c.execute("CREATE TABLE leveling(ID INT, name VARCHAR(20), reward VARCHAR(20), targetpts INT)")
    c.execute("CREATE TABLE charchoosen(ID INT)")
        
def dataEntry():
    c.execute("INSERT INTO song VALUES(1, 'Sinanggar Tullo', 'sounds/1.ogg')")
    c.execute("INSERT INTO song VALUES(2, 'Kampuang Nan Jauh di Mato', 'sounds/2.ogg')")
    c.execute("INSERT INTO song VALUES(3, 'Tokecang', 'sounds/3.ogg')")
    c.execute("INSERT INTO song VALUES(4, 'Kicir Kicir', 'sounds/4.ogg')")
    c.execute("INSERT INTO song VALUES(5, 'Jali Jali', 'sounds/5.ogg')")
    c.execute("INSERT INTO song VALUES(6, 'Lir Ilir', 'sounds/6.ogg')")
    c.execute("INSERT INTO song VALUES(7, 'Gundul Gundul Pacul', 'sounds/7.ogg')")
    c.execute("INSERT INTO song VALUES(8, 'Cik Cik Periook', 'sounds/8.ogg')")
    c.execute("INSERT INTO song VALUES(9, 'Ampar Ampar Pisang', 'sounds/9.ogg')")
    c.execute("INSERT INTO song VALUES(10, 'Anak Kambing Saya', 'sounds/10.ogg')")
    c.execute("INSERT INTO song VALUES(11, 'Angin Mamiri', 'sounds/11.ogg')")
    c.execute("INSERT INTO song VALUES(12, 'Rasa Sayange', 'sounds/12.ogg')")
    c.execute("INSERT INTO song VALUES(13, 'Yamko Rambe Yamko', 'sounds/13.ogg')")
    c.execute("INSERT INTO character VALUES(1, 'Ayah', 'Kamu Pasti Bisa!', 'images/ayah.png','images/ayah_bw.png', 1)")
    c.execute("INSERT INTO character VALUES(2, 'Dokter', 'Hal yang sangat mudah bagimu!', 'images/dokter.png', 'images/dokter_bw.png', 0)")
    c.execute("INSERT INTO character VALUES(3, 'Ilmuwan', 'Tidak sesulit membuat nuklir!', 'images/ilmuan.png', 'images/ilmuan_bw.png', 0)")
    c.execute("INSERT INTO leveling VALUES(1, 'Siaga', 'Karakter Ayah', 0)")
    c.execute("INSERT INTO leveling VALUES(2, 'Penggalang', 'Karakter Dokter', 300)")
    c.execute("INSERT INTO leveling VALUES(3, 'Penegak', 'Karakter Ilmuan', 600)")
    conn.commit()


tableCreate()
dataEntry()
