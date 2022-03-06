import mysql.connector

# CUSTOMER

def addCustomer(customer_id, name, gender, ph_no, email, password, bookdatetime):
    stadium = mysql.connector.connect(host="localhost", user="root", password="lmaogg69", database="stadium")
    cur = stadium.cursor()
    query = "INSERT INTO customer (customer_id, name, gender, ph_no, email, password, booking_date_time) VALUES ( %s,%s,%s,%s,%s,%s,%s )"
    cur.execute(query , (customer_id, name, gender, ph_no, email, password, bookdatetime))
    stadium.commit()
    print(cur.rowcount, "record inserted.")
    stadium.close()
   

def viewCustomer():
    stadium = mysql.connector.connect(host="localhost", user="root", password="lmaogg69", database="stadium")
    cur = stadium.cursor()
    query = "SELECT * FROM customer"
    cur.execute(query)
    result = cur.fetchall()
    stadium.close()
    return result

def deleteCustomer(id):
    stadium = mysql.connector.connect(host="localhost", user="root", password="lmaogg69", database="stadium")
    cur = stadium.cursor()
    cur.execute("DELETE FROM customer WHERE customer_id = %s", (id))
    stadium.commit()
    result = cur.fetchall()
    for x in result:
        print(x)
    stadium.close()

# MATCHES

def addMatches(match_id, duration, home, away):
    stadium = mysql.connector.connect(host="localhost", user="root", password="lmaogg69", database="stadium")
    cur = stadium.cursor()
    sql = "INSERT INTO matches (match_id, duration, home, away) VALUES ( %s,%s,%s,%s )"
    cur.execute(sql, match_id, duration, home, away)
    stadium.commit()
    result = cur.fetchall()
    stadium.close()
    return result

def viewMatches():
    stadium = mysql.connector.connect(host="localhost", user="root", password="lmaogg69", database="stadium")
    cur = stadium.cursor()
    query = "SELECT * FROM matches"
    cur.execute(query)
    result = cur.fetchall()
    stadium.close()
    return result

def deleteMatches():
    stadium = mysql.connector.connect(host="localhost", user="root", password="lmaogg69", database="stadium")
    cur = stadium.cursor()
    cur.execute("DELETE FROM matches WHERE match_id = %s", (id))
    stadium.commit()
    result = cur.fetchall()
    stadium.close()
    return result

# TICKETS

def addticket(ticket_id, seat_no, match_no, matchdatetime, price, veg, nonveg, snacks):
    stadium = mysql.connector.connect(host="localhost", user="root", password="lmaogg69", database="stadium")
    cur = stadium.cursor()
    query = "INSERT INTO tickets (ticket_id, seat_no, match_no, match_date_time, price, veg, non-veg, snacks) VALUES ( %s,%s,%s,%s,%s,%s,%s,%s )"
    cur.execute(query, (ticket_id, seat_no, match_no, matchdatetime, price, veg, nonveg, snacks))
    stadium.commit()
    result = cur.fetchall()
    stadium.close()
    return result


def viewticket():
    stadium = mysql.connector.connect(host="localhost", user="root", password="lmaogg69", database="stadium")
    cur = stadium.cursor()
    query = "SELECT * FROM tickets"
    cur.execute(query)
    result = cur.fetchall()
    stadium.close()
    return result


def deleteticket(id):
    stadium = mysql.connector.connect(host="localhost", user="root", password="lmaogg69", database="stadium")
    cur = stadium.cursor()
    query = "DELETE FROM ticket WHERE ID = %s"
    cur.execute(query, id)
    stadium.commit()
    result = cur.fetchall()
    stadium.close()
    return result

# STADIUM

def viewstadium():
    stadium = mysql.connector.connect(host="localhost", user="root", password="lmaogg69", database="stadium")
    cur = stadium.cursor()
    query = "SELECT * FROM stadium"
    cur.execute(query)
    result = cur.fetchall()
    stadium.close()
    return result

# DISCOUNT

def addiscount(matchno, offerid):
    stadium = mysql.connector.connect(host="localhost", user="root", password="lmaogg69", database="stadium")
    cur = stadium.cursor()
    query = "INSERT INTO discounts (match_no, offer_id) VALUES ( %s,%s )"
    cur.execute(query, (matchno, offerid))
    stadium.commit()
    result = cur.fetchall()
    stadium.close()
    return result


def viewiscount():
    stadium = mysql.connector.connect(host="localhost", user="root", password="lmaogg69", database="stadium")
    cur = stadium.cursor()
    query = "SELECT * FROM discounts"
    cur.execute(query)
    result = cur.fetchall()
    stadium.close()
    return result


def deletediscount(id):
    stadium = mysql.connector.connect(host="localhost", user="root", password="lmaogg69", database="stadium")
    cur = stadium.cursor()
    query = "DELETE FROM discounts WHERE ID = %s"
    cur.execute(query, id)
    stadium.commit()
    result = cur.fetchall()
    stadium.close()
    return result

# SEARCH FUNCTION

def SearchMatchData(match_id="",ticket_id="", match_no=""):  
    stadium = mysql.connector.connect(host="localhost", user="root", password="lmaogg69", database="stadium")
    cur = stadium.cursor()
    cur.execute("SELECT * FROM matches, tickets WHERE match_id = ? OR ticket_id = ? OR match_no = ?",(match_id, ticket_id, match_no))
    rows=cur.fetchall()
    stadium.close()    
    return rows