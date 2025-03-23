import os
import requests  # Import the requests library for HTTP requests
from dotenv import load_dotenv

load_dotenv()


# Define the API URL for Ollama
OLLAMA_URL = os.getenv("OLLAMA_URL", "http://127.0.0.1:11434/api/chat")

# Create a list to store the conversation history
conversation_history = []

def ask_question(question):
    """
    Function to send a message to the DeepSeek model and receive a response.
    It maintains the conversation history for context.

    Parameters:
    question (str): The user's question.

    Returns:
    str: The model's response.
    """
    
    headers = {
        "Content-Type": "application/json"  # Define JSON as the content type
    }

    # Add the user's message to the conversation history
    conversation_history.append({"role": "user", "content": question})

    # Prepare the API request payload
    data = {
        "model": "deepseek-r1:latest",  # Specify the model to use
        "messages": conversation_history,  # Send the entire conversation history
        "stream": False  # Disable streaming mode
    }

    try:
        # Send the HTTP POST request to the Ollama API
        response = requests.post(OLLAMA_URL, json=data, headers=headers)
        response.raise_for_status()  # Raise an error if the request fails

        # Extract the model's response from the API response
        model_response = response.json()["message"]["content"]

        # Add the model's response to the conversation history
        conversation_history.append({"role": "assistant", "content": model_response})

        return model_response  # Return the model's response
    except requests.exceptions.RequestException as e:
        return f"Error connecting to Ollama API: {e}"

# Start a chat loop to keep the conversation going
print("🗣️ Chat with DeepSeek in Python (Type 'exit' to end)")
while True:
    question = input("You: ")  # Get user input
    if question.lower() == "exit":  # Exit condition
        break
    answer = ask_question(question)  # Call the function to get the response
    print("DeepSeek:", answer)  # Display the model's response
