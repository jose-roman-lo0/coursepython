# Positional arguments vs keyword arguments
def message_intro(text, my_type):
    print(text,my_type)
    
# positional use
message_intro("Please introduce an", "integer")
# vs keyword use
message_intro(my_type="integer", text="Please introduce an")