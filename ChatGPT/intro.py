##

from openai import OpenAI
client = OpenAI()
completion = client.chat.completions.create(
    model="gpt-4o",
    store=True,
    messages=[
        {"role": "user", "content": "write a haiku about ai"}
    ]
)
from openai import OpenAI

client = OpenAI(
  organization='org-oC0isseinuzIwpFktBi88729',
  project='$PROJECT_ID',
)
