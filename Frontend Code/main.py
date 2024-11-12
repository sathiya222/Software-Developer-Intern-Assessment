# Create Operation
def create_registration(name, email, dob, phone):
 try:
 connection = create_connection()
 cursor = connection.cursor()
 query = "INSERT INTO Registration (Name, Email, DateOfBirth, PhoneNumber) VALUES (%s, %s, %s, %s)"
 cursor.execute(query, (name, email, dob, phone))
 connection.commit()
 print("Registration created successfully")
 except Error as e:
 print("Error:", e)
 finally:
 cursor.close()
 connection.close()
# Read Operation
def read_registration(id):
 try:
 connection = create_connection()
 cursor = connection.cursor()
 query = "SELECT * FROM Registration WHERE ID = %s"
 cursor.execute(query, (id,))
 result = cursor.fetchone()
 print("Registration Details:", result)
 except Error as e:
 print("Error:", e)
 finally:
 cursor.close()
 connection.close()
# Update Operation
def update_registration(id, name, email, dob, phone):
 try:
 connection = create_connection()
 cursor = connection.cursor()
 query = "UPDATE Registration SET Name = %s, Email = %s, DateOfBirth = %s, PhoneNumber = %s WHERE ID =
%s"
 cursor.execute(query, (name, email, dob, phone, id))
 connection.commit()
 print("Registration updated successfully")
 except Error as e:
 print("Error:", e)
 finally:
 cursor.close()
 connection.close()
# Delete Operation
def delete_registration(id):
 try:
 connection = create_connection()
 cursor = connection.cursor()
 query = "DELETE FROM Registration WHERE ID = %s"
 cursor.execute(query, (id,))
 connection.commit()
 print("Registration deleted successfully")
 except Error as e:
 print("Error:", e)
 finally:
 cursor.close()
 connection.close()