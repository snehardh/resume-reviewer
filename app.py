import os
import requests
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent"
api_key = os.getenv("GOOGLE_API_KEY")
job_desc = "Software QA Engineer. Skills: manual testing, Python, JIRA, analytical skills"
resume = "John Doe. QA Tester 2 years. Skills: Manual testing, Python basics, JIRA."
prompt = "Review this resume for the job: " + job_desc + " Resume: " + resume
payload = {"contents": [{"parts": [{"text": prompt}]}]}
response = requests.post(url, params={"key": api_key}, json=payload)
data = response.json()
print(data["candidates"][0]["content"]["parts"][0]["text"])
print(data)
