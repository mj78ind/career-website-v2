from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://r1l8vf6mwcz1057m3jn2:pscale_pw_z0m1BZUNzd3ZKHun0OSsu09VhbtUAUCWFRa36bLOONG@aws.connect.psdb.cloud/mayankcareers?charset=utf8mb4"

engine = create_engine(db_connection_string, 
                      connect_args={
                        "ssl": {
                          "ssl_ca": "/etc/ssl/cert.pem"
                        }
                      })