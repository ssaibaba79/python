
tweet =  input("Enter your tweet\n")
size = len(tweet)
MAX_LEN = 140

if size > MAX_LEN :
    print(f'Your {size} tweet is {size - MAX_LEN} chars longer than the allowed {MAX_LEN} chars')
else:
    print('Your tweet is good')