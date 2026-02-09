import fitz 
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
os.environ["GROQ_API_KEY"] = GROQ_API_KEY

client = ChatGroq(
  api_key=GROQ_API_KEY,
  model="qwen/qwen3-32b",  
  temperature=0.5
)

def extract_text_from_pdf(uploaded_file):
  """
  Extracts text from a PDF file.

  Args:
      uploaded_file(str): The path to the PDF file.
  Returns:
      str: The extracted text.

  """
  doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
  
  text = ""
  for page in doc:
    text += page.get_text()
  return text

def ask_llm(prompt):
  """
  Sends a prompt to the llm ans return the responses.

  Args:
      prompt(str): The prompt to send to the groq api.
      
  Returns:
      str: The response from the Groq
  """
  response = client.invoke(prompt)
  
  return response.content
