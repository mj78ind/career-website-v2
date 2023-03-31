from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://r1l8vf6mwcz1057m3jn2:pscale_pw_z0m1BZUNzd3ZKHun0OSsu09VhbtUAUCWFRa36bLOONG@aws.connect.psdb.cloud/mayankcareers?charset=utf8mb4"

engine = create_engine(db_connection_string, 
                      connect_args={
                        "ssl": {
                          "ssl_ca": "/etc/ssl/cert.pem"
                        }
                      })

with engine.connect() as conn:
  result = conn.execute(text("select * from jobs"))
  print("type(result):", type(result))
  result_all = result.all()
  print("type(result.all()):", type(result_all))
  print("result.all():", result_all)
  print(result_all[0])
  first_result = result_all[0]
  print(" type(first_result):", type(first_result))

  column_names = result.keys() 
  first_result_dict = dict(zip(column_names, first_result))
  print(first_result_dict)
  print("type(first_result_dict)):", type(first_result_dict))

  
  

