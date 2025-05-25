from typing import Annotated
from google import genai
from google.genai.types import GenerateContentResponse
from dotenv import load_dotenv
from fastapi import Depends
import os

load_dotenv()

GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

client = genai.Client(api_key=GEMINI_API_KEY)

def get_gemini_response():
  return client.models.generate_content(
    model="gemini-2.0-flash", contents="Explain how AI works in a few words"
  )

GeminiDep = Annotated[GenerateContentResponse, Depends(get_gemini_response)]