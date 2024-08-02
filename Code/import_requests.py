
import requests
import json
import pandas as pd
#Insert the model url
url = "http://localhost:11434/api/chat"

#Read the csv file
df = pd.read_csv("Your csv file", header = 0, usecols=["reviewDescription"])
pd.options.display.max_colwidth = 1000 

#Inputting the reviews into the model
for i, row in df.iterrows():
   reviews = str(row)[17: -24]
   
   
   payload = json.dumps({
  "model": "llama2:7b-chat-q3_K_S",
  
      "messages": [
    {
      "role": "user",
      "content": " GIVING YOUR ANSWER IN A SINGLE WORD, NEVER GIVE ME MORE THAN ONE WORD(Do not give me multiple words), AND DO NOT USE EMOJIS, emotionally analyse this review:" + reviews + "without using words such as 'positive' and 'negative' and using emotion enducing words such as 'happy, sad, angry, mad, dissapointed, estatic' or any better word."
    }
  ],
  "stream": False
   })
   headers = {
  'Content-Type': 'application/json'
   }

   response = requests.request("POST", url, headers=headers, data=payload)
 
# Parse the JSON response
   response_json = response.json()

# Extract and print the content
   content = response_json.get('message', {}).get('content', '')
   print(content)
