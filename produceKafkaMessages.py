from kafka import KafkaProducer
from kafka.errors import KafkaError
import time
import random

# Toggle User Input Prompts
takeInput = 'N'

# Function to Get User Input
def getUserInput(question, defaultValue):
 try:
  newValue = int(input(question) or defaultValue)
 except:
  newValue = defaultValue
 return(newValue)

# Create KafkaProducer Object
producer = KafkaProducer(bootstrap_servers='localhost:9092')
topicName = 'test'

if takeInput == 'Y':
 # Get User Input
 numsToGen = getUserInput("How many samples would you like? (25): ", 25)
 minNumToGen = getUserInput("Minimum Value? (0): ", 0)
 maxNumToGen = getUserInput("Maximum Value? (25): ", 25)
else:
 # Default Values if Input Toggled Off
 numsToGen = 25
 minNumToGen = 0
 maxNumToGen = 25

# Generate Psuedo Random Numbers and Send to Kafka
for i in range(0, numsToGen):
 rval = random.randint(minNumToGen, maxNumToGen)
 rval = bytes(str(rval), "ascii")
 producer.send(topicName, rval)
 time.sleep(2)