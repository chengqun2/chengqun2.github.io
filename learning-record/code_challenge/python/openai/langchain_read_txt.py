import os
from dotenv import load_dotenv
from langchain_deepseek import ChatDeepSeek

load_dotenv()

# Ensure the DeepSeek API key is set
if not os.getenv("DEEPSEEK_API_KEY"):
    raise EnvironmentError("Please set the DEEPSEEK_API_KEY environment variable.")

# Initialize the DeepSeek chat model
llm = ChatDeepSeek(
    model="deepseek-chat",  # Specify the DeepSeek model
    temperature=0.7,        # Adjust the creativity of the responses
    max_tokens=500,         # Limit the response length
    max_retries=2           # Retry on failure
)

# Function to read input text from a file
def read_input_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

# Read the content from 'input.txt'
input_text = read_input_file("knowledge_base.txt")

# Define the prompt for the model
prompt = f"Please analyze the following text and provide a summary:\n\n{input_text}"

# Send the prompt to the DeepSeek model and get the response
response = llm.invoke(prompt)

# Print the model's response
print("Generated Summary:\n")
print(response)
