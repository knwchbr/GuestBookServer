import psycopg2
try:
    connection = psycopg2.connect(user='webadmin',
                                    password = 'BROfoy35669',
                                    host = 'node1444-kanokwan.app.ruk-com.cloud',
                                    port ='11028',
                                    database = 'postgres')
    connection.autocommit = True

    cursor = connection.cursor()

    sql = '''CREATE database TestDB'''

    cursor.execute(sql)
    print('Database created successfully.........')

except (Exception,psycopg2.Error) as error:
    print('Error while connecting to PostgreSQl',error)
finally:
    if(connection):
        cursor.close()
        connection.close()
        print('PostgreSQL connection is closeds')