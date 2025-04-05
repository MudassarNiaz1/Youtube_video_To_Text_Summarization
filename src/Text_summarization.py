import os
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access API key
api_key = os.getenv("GROQ_API_KEY")

if api_key:
    print("API Key Loaded Successfully!")
    os.environ["GROQ_API_KEY"] = api_key  # Set the API key in environment variables
else:
    print("API Key Not Found!")

class Modelling:
    def __init__(self):
        self.model = init_chat_model("llama3-8b-8192", model_provider="groq")
    
    def split_text(self, text, max_tokens=5000):
        return [text[i:i + max_tokens] for i in range(0, len(text), max_tokens)]
    
    def model2(self, text):
        chunks = self.split_text(text)  
        summaries = []

        for chunk in chunks:
            message = self.model.invoke(f"Summarize this text: {chunk} in 50 to 200 words")
            summaries.append(message.content)

        final_summary = " ".join(summaries)  
        return final_summary
