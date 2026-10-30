# Verify the table exists
cursor = connection.execute('Select * from tasks')
print("Tables:", cursor.fetchall())


print("Rows: ", cursor.fetchmany(2))

print(cursor.fetchone())

connection.close()

print("Database initialized successfully:", db_path)
