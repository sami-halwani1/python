from openai import OpenAI
import json

client = OpenAI(
  api_key="Your_API_Key"
)

# response = client.chat.completions.create(
#   model="gpt-4o-mini",
#   store=True,
#   messages=[
#     {"role": "developer",
#      "content": "You are an SEO Specialist trying to improve a Software companies Website SEO. The company name is \'Majeks Software\'. Please provide me a List of 5 Blog Topics to improve their websites search engine ranking. Blog Topic should be formatted as a json file. Each Topic should include the topic title, topic_metaTitle, and topic_metaDescription."
#     }
#   ],
#   response_format={"type": "json_object"}
# )

# completion = client.chat.completions.create(
#   model="gpt-4o-mini",
#   store=True,
#   messages=[
#     {"role": "user",
#      "content": "Write me the full Blog Given the prompt.(Not a Structured Outline) The Blog MUST be 400 Words. Return the Blog in <HTML> Format: \"topic_title\": \"The Importance of Cybersecurity in Software Development\", \"topic_metaTitle\": \"Cybersecurity in Software Development | Majeks Software\", \"topic_metaDescription\": \"Understand the critical role cybersecurity plays in software development. Majeks Software discusses best practices and strategies to secure your applications.\""
#     }
#   ]
# )

# json_content = response.choices[0].message.content
# print(json_content)

# if isinstance(json_content, str):
#     json_data = json.loads(json_content)

# json_name = "openai_response.json"

# with open(json_name , 'w') as json_file:
#     json.dump(json_data, json_file, indent=4)



# print(f'JSON response saved as {json_name}')
json_name = "openai_response.json"
with open(json_name, 'r') as json_content:
    json_data = json.load(json_content)
# print(json_data)


# for topic in range(len(json_data['blogTopics'])):
#     print(f'Topic {topic}\n---------')
#     print(f'Title: {json_data['blogTopics'][topic]["topicTitle"]}')
#     print(f'MetaTitle: {json_data['blogTopics'][topic]["topic_metaTitle"]}')
#     print(f'MetaDescription: {json_data['blogTopics'][topic]["topic_metaDescription"]}')
#     print("---------\n")

# print(json_data['blogTopics'][0])

json_useCase = json_data['blogTopics'][0]

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  store=True,
  messages=[
    {"role": "user",
     "content": f"Write me the full Blog Given the prompt.(Not a Structured Outline) The Blog MUST be 400 Words. Return the Blog in <HTML> Format: {json_useCase}"
    }
  ]
)

print(completion.choices[0].message.content)