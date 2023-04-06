passwords = { "Alice": "passw0rd"  , "Bob": "1234", "Charlie": "love123" } 
logins = { "Alice": 1, "Bob": 20, "Charlie": 3 }

def login(user,passw):
	if user in passwords :
		if passwords[str(user)]==str(passw):
			logins[str(user)]+=1
			print("Login succesful. " +str(user)+ " logged in " + str(logins[str(user)]) + " times")
			#print(logins[str(user)])
		else:
			print("Login unsuccesful. Bad password")		
	else:		
		print("Login unsucessful. Bad username") 

login("Bob", "bad_password")
login("Jane", "1234")
login("Alice", "passw0rd")
login("Alice", "passw0rd")

input()