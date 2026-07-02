def duplicate_messages(n, timestamps, messages, k):
    delivered = {}
    result = []
       
    for i in range(n):
        message = messages[i] 
        current_time = timestamps[i]

        if message not in delivered or (current_time - delivered[message]) >= k:
            result.append(message)
            delivered[message] = current_time
    
    return result 

print(duplicate_messages(6, [1, 4, 5, 10, 11, 14], ["hello", "bye", "bye", "hello", "bye", "hello"], 5))
           
