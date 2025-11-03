import os
from groq import Groq

# Set your Groq API key (get it from https://console.groq.com/)
os.environ["GROQ_API_KEY"] = "your_groq_api_key_here"

# Initialize the Groq client
client = Groq()

def search_agent():
    print("Search Engine AI Agent: Ask me a question, and I'll 'search' for an answer. Type 'quit' to exit.")
    
    while True:
        query = input("Your Query: ")
        if query.lower() == "quit":
            print("Search Engine AI Agent: Goodbye!")
            break
        
        # Craft a prompt for search engine-like answers
        prompt = f"Answer the following question as a search engine would, providing a concise and factual response: {query}"
        
        try:
            # Generate response using Groq's API with an updated free model
            chat_completion = client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ],
                model="llama-3.1-8b-instant",  # Updated free model (fast and good for QA)
            )
            
            # Extract and print the answer
            answer = chat_completion.choices[0].message.content
            print(f"Search Result: {answer}")
            print("-" * 50)  # Separator for readability
        
        except Exception as e:
            print(f"Error: {e}. Please check your API key or try again later.")

# Run the agent
if __name__ == "__main__":
    search_agent()
