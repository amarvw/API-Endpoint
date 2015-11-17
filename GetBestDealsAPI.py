
import pypyodbc
import json
import sys
import collections
from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)


## function to connect to the database
def connection_function():
    connection_string = 'DRIVER={SQL Server};SERVER=172.16.16.170,49333;DATABASE=HQAssignment;UID=sa;PWD=Passwd@321'
    connection = pypyodbc.connect(connection_string)
    return(connection)

##function to get the required data for the given paramenters
def get_data(hotelId,checkInDate,checkOutDate):
    conn = connection_function()                                    
    SQL = """SELECT offer.offer_id
                ,offer.hotel_id
                ,priOffer.checkin_date
                ,priOffer.checkout_date
                ,priOffer.sellings_price
                ,curr.code
                FROM bi_data.valid_offers AS offer (NOLOCK)
                INNER JOIN primary_data.offer AS priOffer (NOLOCK)
                        ON offer.offer_id = priOffer.id
                INNER JOIN primary_data.lst_currency curr (NOLOCK)
                        ON priOffer.currency_id = curr.id
                WHERE offer.hotel_id = """ + str(hotelId) +""" 
                AND priOffer.checkin_date = '"""  + checkInDate + """'
                AND priOffer.checkout_date =  '""" +checkOutDate  +"""'"""    
    cursor = conn.cursor().execute(SQL)                               ##get all the data in a cursor
    rows = cursor.fetchall()                                          ## put all the records in the "rows" variable

    objects_list = []                                                 ##create the array object to hold the data
    for row in rows:
        d = collections.OrderedDict()
        d['offer_id'] = row[0]
        d['hotel_id'] = row[1]
        d['checkin_date'] = row[2]
        d['checkout_date'] = row[3]
        d['sellings_price'] = row[4]
        d['code'] = row[5]        
    objects_list.append(d)
 
    j = json.dumps(objects_list,separators=(',', ': '))                 ##form the JSON string
    
    conn.close()
    return(j)

class getHotel(Resource):
    def get(self,hotelId,checkInDate,checkOutDate):             
        j = get_data(hotelId,checkInDate,checkOutDate)                  ##call to the get_data function
        return(j)

api.add_resource(getHotel, '/offer/best-deal/<hotelId>/<checkInDate>/<checkOutDate>')       ##add respurce

if __name__ == "__main__":
    app.run(debug=True)


    






    
