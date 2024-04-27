import sqlite3


def connect ():
    conn=sqlite3.connect("Sandogh_Gharzolhasane.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS documents (user_number int , password int ,"+
    " l_agreement int ,l_bcert_nacard int ,l_pincome int , l_presidence int "+
    ", l_avr int ,g1_agreement int, g1_bcert_ncard int , g1_pincome int ,g1_avr int ,"+
    " g2_agreement int , g2_bcert_ncard int, g2_pincome int, g2_avr int)")
    cur.execute("CREATE TABLE IF NOT EXISTS warranty_documetns (user_number int ,"+
    " password int , l_wdtype text , l_wdamount int , l_confirm int , g1_wdtype text ,"+
    " g1_wdamount int , g1_confirm int , g2_wdtype text , g2_wdamount int , g2_confirm int)")
    cur.execute("CREATE TABLE IF NOT EXISTS inquiry (user_number int ,password int ,"+
    " taken int ,l_inquiry int , g1_inquiry int , g2_inquiry int )")
    conn.commit()
    cur.close()
    conn.close()


def doc_view():
    conn=sqlite3.connect("Sandogh_Gharzolhasane.db")
    cur=conn.cursor()
    cur=conn.execute("SELECT * FROM documents")
    rows=cur.fetchall()
    conn.close()
    return rows

def inq_view():
    conn=sqlite3.connect("Sandogh_Gharzolhasane.db")
    cur=conn.cursor()
    cur=conn.execute("SELECT * FROM inquiry")
    rows=cur.fetchall()
    conn.close()
    return rows

def wdoc_view():
    conn=sqlite3.connect("Sandogh_Gharzolhasane.db")
    cur=conn.cursor()
    cur=conn.execute("SELECT * FROM warranty_documetns")
    rows=cur.fetchall()
    conn.close()
    return rows

def insert_doc(user_number,password,l_agreement,l_bcert_nacard,l_pincome,l_presidence,l_avr,g1_agreement,g1_bcert_ncard,g1_pincome,g1_avr,g2_agreement,g2_bcert_ncard,g2_pincome,g2_avr):
    conn=sqlite3.connect("Sandogh_Gharzolhasane.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO documents VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(int(user_number),int(password),int(l_agreement),int(l_bcert_nacard),int(l_pincome),int(l_presidence),int(l_avr),int(g1_agreement),int(g1_bcert_ncard),int(g1_pincome),int(g1_avr),int(g2_agreement),int(g2_bcert_ncard),int(g2_pincome),int(g2_avr)))
    conn.commit()
    conn.close()
    doc_view()
    print(user_number)
    print(password)
    print(l_agreement)
    print(type(l_bcert_nacard))
    print(type(l_pincome))

def insert_wdoc(user_number ,password, l_wdtype,l_wdamount ,l_confirm , g1_wdtype , g1_wdamount , g1_confirm , g2_wdtype, g2_wdamount, g2_confirm):
    conn=sqlite3.connect("Sandogh_Gharzolhasane.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO warranty_documetns VALUES (?,?,?,?,?,?,?,?,?,?,?)",(user_number ,password, l_wdtype,l_wdamount ,l_confirm , g1_wdtype , g1_wdamount , g1_confirm , g2_wdtype, g2_wdamount, g2_confirm))
    conn.commit()
    conn.close()
    wdoc_view()

def insert_inq(user_number,password,taken,l_inquiry, g1_inquiry, g2_inquiry):
    conn=sqlite3.connect("Sandogh_Gharzolhasane.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO inquiry VALUES (?,?,?,?,?,?)",(user_number,password,taken,l_inquiry, g1_inquiry, g2_inquiry))
    conn.commit()
    conn.close()
    inq_view()


def search_doc(user_number="",password=""):
    conn=sqlite3.connect("Sandogh_Gharzolhasane.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM documents WHERE user_number=? and password=? ", (user_number,password))
    rows=cur.fetchall()
    conn.close()
    return rows


def search_wdoc(user_number="",password=""):
    conn=sqlite3.connect("Sandogh_Gharzolhasane.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM warranty_documetns WHERE user_number=? and password=? ", (user_number,password))
    rows=cur.fetchall()
    conn.close()
    return rows


def search_inq(user_number="",password=""):
    conn=sqlite3.connect("Sandogh_Gharzolhasane.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM inquiry WHERE user_number=? and password=? ", (user_number,password))
    rows=cur.fetchall()
    conn.close()
    return rows


def delete_doc(user_number,password):
    conn=sqlite3.connect("Sandogh_Gharzolhasane.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM documents WHERE user_number=? and password=?",(user_number,password))
    conn.commit()
    conn.close()


def delete_doc(user_number,password):
    conn=sqlite3.connect("Sandogh_Gharzolhasane.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM warranty_documetns WHERE user_number=? and password=?",(user_number,password))
    conn.commit()
    conn.close()


def delete_doc(user_number,password):
    conn=sqlite3.connect("Sandogh_Gharzolhasane.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM inquiry WHERE user_number=? and password=?",(user_number,password))
    conn.commit()
    conn.close()

def update_doc(user_number,password,l_agreement,l_bcert_nacard,l_pincome,l_presidence,l_avr,g1_agreement,g1_bcert_ncard,g1_pincome,g1_avr,g2_agreement,g2_bcert_ncard,g2_pincome,g2_avr):
    conn=sqlite3.connect("Sandogh_Gharzolhasane.db")
    cur=conn.cursor()
    cur.execute("UPDATE documents SET l_agreement=? ,l_bcert_nacard=? ,l_pincome=? ,l_presidence=? ,l_avr=? ,g1_agreement=? ,g1_bcert_ncard=? ,g1_pincome=? ,g1_avr=? ,g2_agreement=? ,g2_bcert_ncard=? ,g2_pincome=? ,g2_avr=? WHERE user_number=? and password=? ",(l_agreement,l_bcert_nacard,l_pincome,l_presidence,l_avr,g1_agreement,g1_bcert_ncard,g1_pincome,g1_avr,g2_agreement,g2_bcert_ncard,g2_pincome,g2_avr,user_number,password))
    conn.commit()
    conn.close()


def update_wdoc(user_number ,password, l_wdtype,l_wdamount ,l_confirm , g1_wdtype , g1_wdamount , g1_confirm , g2_wdtype, g2_wdamount, g2_confirm):
    conn=sqlite3.connect("Sandogh_Gharzolhasane.db")
    cur=conn.cursor()
    cur.execute("UPDATE warranty_documetns SET l_wdtype=? ,l_wdamount=? ,l_confirm=? , g1_wdtype=? , g1_wdamount=? , g1_confirm=? , g2_wdtype=?, g2_wdamount=? , g2_confirm=? WHERE user_number=? and password=?",( l_wdtype ,l_wdamount ,l_confirm , g1_wdtype , g1_wdamount , g1_confirm , g2_wdtype, g2_wdamount, g2_confirm, user_number, password))
    conn.commit()
    conn.close()

def update_inq(user_number,password,taken,l_inquiry, g1_inquiry, g2_inquiry):
    conn=sqlite3.connect("Sandogh_Gharzolhasane.db")
    cur=conn.cursor()
    cur.execute("UPDATE inquiry SET taken=? ,l_inquiry=? , g1_inquiry=? , g2_inquiry=? WHERE user_number=? and password=?",(taken,l_inquiry, g1_inquiry, g2_inquiry, user_number, password))
    conn.commit()
    conn.close()


connect()
