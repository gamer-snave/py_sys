spam = {'color': 'red', 'age': 42}

# print(spam.items())
print(spam.get('age', 0))
import pprint

spam.setdefault('color', 'black')
message = "It was a bright cold day in April, and the clocks were striking thirteen."
count={}
for character in message:
    count.setdefault(character, 0)
    count[character]=count[character]+1
pprint.pformat(count)



    