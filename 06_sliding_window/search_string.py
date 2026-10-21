def search_string(text, pattern):
        
    for i in range(len(text) - len(pattern) + 1):
        matching_text = text[i:i+len(pattern)]

        if matching_text == pattern:
            return i
        
    return -1
        

print(search_string("reactive", "xyz"))
print(search_string("reactive", "active"))
print(search_string("Hello World", "World"))
