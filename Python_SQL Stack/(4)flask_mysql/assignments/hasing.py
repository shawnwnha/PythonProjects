import md5 
password ="password"
hased_password = md5.new(password).hexdigest()
print hased_password