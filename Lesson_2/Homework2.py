num_str = 125
print(type(num_str))
num_str = str(num_str)
print(type(num_str))

message = "Hi my name is Python!"
message = message.replace("i" , "1")
message = message.replace("y" , "0")
print(message)

split_test = "This is a split test"
split_test = split_test.split( )
split_join = " ".join(split_test)
print(split_join,split_test)
print(len(split_join))
