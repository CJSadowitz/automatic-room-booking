import random

eventNames = [
  'some event name',
  'another event name'  
]

specialEventNames = [
  'some special event name',
  'another special event name'
]
a = int(random.random()*100) % len(eventNames) # randomly get a name from eventNames
