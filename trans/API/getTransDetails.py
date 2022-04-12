from flask_restful import Resource, reqparse
from API.config import cur,connection
import datetime



parser = reqparse.RequestParser()



class GetTransdata(Resource):
    def __init__(self):
        parser.add_argument('customerId')
        parser.add_argument('purchaseDate')
        parser.add_argument('purchasedAmt')
        parser.add_argument('paidAmt')
       
    def get(self):
        args = parser.parse_args()
        print(f'args {args}')
        try:
            if args.customerId:
              
                cur.execute("SELECT * FROM usertrans WHERE customerId=%s",(args.customerId))
                parchasedAmt = 0
                paidAmt = 0
                balanceAmt = 0
                row = cur.fetchall()

                if len(row) > 0:
                    for i in row:
                        parchasedAmt += i[3]
                        paidAmt += i[4]
                        balanceAmt += i[5]
                    
                    return {
                        "statusCode":200,
                        "data":[parchasedAmt,paidAmt,balanceAmt]
                    }
                    
                else:
                    return {
                        "statusCode":500,
                        "data":"no data found"
                    }
            elif args.purchaseDate:
    
                cur.execute("SELECT * FROM usertrans WHERE purchaseDate >=%s",(args.purchaseDate))
            else:
          
                cur.execute("SELECT * FROM usertrans")
            row = cur.fetchall()

            data = []

            if len(row) > 0:
                for i in row:
                    data.append({
                        "customerId":i[1],
                        "parchaseDate":str(i[2]),
                        "parchasedAmt":i[3],
                        "paidamt":i[4],
                        "balanceAmt":(int(i[3])-int(i[4]))
                    })
                print(f'data {data}')
                
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
            print(f'args {args}')
            now = datetime.datetime.now()
            print(f'now {now}')

            cur.execute("INSERT INTO usertrans (customerId,purchaseDate,purchasedamt,paidamt, balanceAmt) "
                        "VALUES (%s,%s,%s,%s,%s) ",(str(args.customerId), args.purchaseDate, str(args.purchasedAmt), str(args.paidAmt), (int(args.purchasedAmt)-int(args.paidAmt))))

            connection.commit()
            print('execution done')

            if cur.rowcount > 0:
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