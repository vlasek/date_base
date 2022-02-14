import edit
import control
import create
import search
import log

def db_change():
    zapis = get_zapis_inline()
    return(zapis)

def read_db():               
     with open('db.csv', 'r') as data:
        return data.readlines()


def get_zapis_inline():
    z=input()
    return z
    
get_zapis_inline()
print(read_db())
