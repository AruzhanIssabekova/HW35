import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="python_db"
)

mycursor = mydb.cursor()

def show_contacts(cursor):
    sql_query = "SELECT * FROM contacts" # SQL
    cursor.execute(sql_query)
    contacts_all = cursor.fetchall()
    
    return contacts_all

def create_contact(user_data):
    global mydb
    global mycursor
    
    u_data = user_data.split(' ')
    
    l_name = u_data[0]
    f_name = u_data[1]
    m_name = ''
    if len(u_data) == 3: m_name = u_data[2]

    sql_query = "INSERT INTO contacts (l_name, f_name, m_name) VALUES (%s, %s, %s)" # SQL
    contact_data = (l_name, f_name, m_name)
    
    mycursor.execute(sql_query, contact_data)
    mydb.commit()


def update_contact(contact_id, new_data):
    u_data = new_data.split(' ')
    l_name = u_data[0]
    f_name = u_data[1]
    m_name = '' if len(u_data) == 2 else u_data[2]

    sql_query = "UPDATE contacts SET l_name = %s, f_name = %s, m_name = %s WHERE contact_id = %s"
    contact_data = (l_name, f_name, m_name, contact_id)

    mycursor.execute(sql_query, contact_data)
    mydb.commit()


def delete_contact(contact_id):
    sql_query = "DELETE FROM contacts WHERE contact_id = %s"
    contact_data = (contact_id,)

    mycursor.execute(sql_query, contact_data)
    mydb.commit()