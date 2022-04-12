from flask_restful import Resource, reqparse
from API.config import cur1,connection1




parser = reqparse.RequestParser()



class GetUserData(Resource):
    def __init__(self):
        parser.add_argument('customerId')
        parser.add_argument('firstName')
        parser.add_argument('lastName')
        parser.add_argument('dateOfBirth')
        parser.add_argument('email')
        parser.add_argument('phoneNo')
        parser.add_argument('gender')
        parser.add_argument('address')

    def get(self):
        args = parser.parse_args()
        print(f'args {args}')
        try:
        
            cur1.execute("SELECT * FROM userdetails")
            row = cur1.fetchall()
            data =[]
            if len(row) > 0:
                for i in row:
                    data.append({
                        "customerId":i[1],
                        "firstName":i[2],
                        "lastName":i[3],
                        "dateOfBirth":str(i[4]),
                        "email":i[5],
                        "phoneNo":i[6],
                        "gender":i[7],
                        "address":i[8]
                    })
                return {
                    "statusCode":200,
                    "data":data
                }
                
            else:
                return {
                    "statusCode":500,
                    "data":"no data found"
                }
                       
        except Exception as e:
            return {
                "statusCode":500,
                "data":str(e)
            }
   
    def post(self):
        args=  parser.parse_args()

        
        try:
           # print(f'args {args}')

            cur1.execute("INSERT INTO userdetails (customerId, firstName, lastName,dateOfBirth, email, phoneNo, gender, address) "
                        "VALUES (%s,%s,%s,%s,%s,%s,%s,%s) ",(str(args.customerId), str(args.firstName), str(args.lastName),args.dateOfBirth, str(args.email), str(args.phoneNo), str(args.gender), str(args.address)))

            connection1.commit()
            print('execution done')

            if cur1.rowcount > 0:
                return {
                    "statusCode":200,
                    "data": "data inserted successfully"
                    
                }
            else:
                return {
                    "statusCode":200,
                    "data": "data not Inserted"

                }

        except Exception as e:
            return {
                "statusCode":400,
                "data": e
            }