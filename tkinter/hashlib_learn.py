import hashlib

# Hashing a password:
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()
# In this function:
# - hashlib.sha256() creates a SHA-256 hash object
# - password.encode() converts the password string to bytes (necessary because hashing function works on byte data).
# - .hexdigest() returns the hash valuie as a hexadecimal string.

# By hashing the password before sstoreing them in the database, w3e can ensure that even if the data base is
# is compromised, the actual passwords remain secure. It is a critical practice for protecting user credentials.

# So what is hashlib? 
# Answer : hashlib is a built-in Python library that provides a common interface to many secure hash and message 
# digest algorithms. These algorithms take an input (or "message") and return a fixed-size string of bytes. 
# The output is typically a hexadecimal string that represents the hash of the input. The hashing process is one-way, 
# meaning it is computationally difficult to reverse the process and obtain the original input from the hash.
def create_db(): 
  conn = sqlite3.connect('users.db') # Connect to the SQLite database 'user.db'
  c = conn.cursor() # Create a curser object to interact with the database
  c.execute('''CREATE TABLE IF NOT EXISTS users ( 
                  username TEXT NOT NULL, 
                  password TEXT NOT NULL
                )
  ''') # Execute the SQL command to create the 'users' table if it doesn't exist
  conn.commit() # Commit  the changes to the database
  conn.close() # Close the connection to the database

def add_user(username, password): # Defines a function named add-user that takes two parametersd: username and password.
    conn = sqlite3.connect('users.db')  # Connect to the SQLite database 'users.db' if the database does not exist one will be created
    c = conn.cursor()  # Create a cursor object to interact with the database allows you to execute SQL Commands
    c.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hash_password(password)))  # Insert the username and 
  # hashed password into the 'users' table This line executes an SQL command to insert a new row into the users table with the provided 
  # username and the hashed password. The hash_password function is used to hash the password before storing it in the database for security purposes.
    conn.commit()  # Commit the changes to the database
    conn.close()  # Close the connection to the database
  
