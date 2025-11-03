import os
from groq import Groq
from tools import web_search, calculate, get_current_time, wikipedia_search, get_weather, convert_units

# Set your Groq API key
os.environ["GROQ_API_KEY"] = "GROQ_API_KEY"

# Initialize Groq client
client = Groq()

# Define available tools for Groq
tools = [
    {
        "type": "function",
        "function": {
            "name": "web_search",
            "description": "Search the web for real-time information.",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {"type": "string", "description": "The search query."}
                },
                "required": ["query"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "calculate",
            "description": "Perform simple math calculations.",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {"type": "string", "description": "The math expression, e.g., '2 + 3 * 4'."}
                },
                "required": ["expression"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_current_time",
            "description": "Get the current date and time.",
            "parameters": {"type": "object", "properties": {}}
        }
    },
    {
        "type": "function",
        "function": {
            "name": "wikipedia_search",
            "description": "Search Wikipedia for a summary on a topic.",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {"type": "string", "description": "The topic to search on Wikipedia."}
                },
                "required": ["query"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get current weather for a city.",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {"type": "string", "description": "The city name, e.g., 'London'."}
                },
                "required": ["city"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "convert_units",
            "description": "Convert between units, e.g., length or temperature.",
            "parameters": {
                "type": "object",
                "properties": {
                    "value": {"type": "number", "description": "The value to convert."},
                    "from_unit": {"type": "string", "description": "The unit to convert from, e.g., 'meters'."},
                    "to_unit": {"type": "string", "description": "The unit to convert to, e.g., 'feet'."}
                },
                "required": ["value", "from_unit", "to_unit"]
            }
        }
    }
]


def chat_agent():
    print("Chat Agent: Hi! I'm a conversational AI with tools. Ask me anything, or type 'quit' to exit.")
    messages = []  # Store conversation history
    
    while True:
        # Display available actions/options before prompting (now numbered)
        print("\nAvailable actions you can ask for:")
        print("1) web_search: Search the web (e.g., 'Search for latest AI news')")
        print("2) calculate: Do math (e.g., 'Calculate 5 + 3 * 2')")
        print("3) get_current_time: Get the current time (e.g., 'What time is it?')")
        print("4) wikipedia_search: Get a Wikipedia summary (e.g., 'Tell me about Python')")
        print("5) get_weather: Check weather (e.g., 'What's the weather in London?')")
        print("6) convert_units: Convert units (e.g., 'Convert 100 meters to feet')")
        print("7) Or just chat normally for general questions!")
        
        user_input = input("You: ")
        if user_input.lower() == "quit":
            print("Chat Agent: Goodbye!")
            break
        
        # Add user message to history
        messages.append({"role": "user", "content": user_input})
        
        # Call Groq with tool support
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=messages,
            tools=tools,
            tool_choice="auto"  # Let AI decide if/which tool to use
        )
        
        # Check if the AI wants to call a tool
        tool_calls = response.choices[0].message.tool_calls
        if tool_calls:
            # Execute each tool call
            for tool_call in tool_calls:
                function_name = tool_call.function.name
                args = eval(tool_call.function.arguments)  # Parse JSON args safely
                
                # Tool execution based on actual function names (not numbers)
                if function_name == "web_search":
                    result = web_search(args["query"])
                elif function_name == "calculate":
                    result = calculate(args["expression"])
                elif function_name == "get_current_time":
                    result = get_current_time()
                elif function_name == "wikipedia_search":
                    result = wikipedia_search(args["query"])
                elif function_name == "get_weather":
                    result = get_weather(args["city"])
                elif function_name == "convert_units":
                    result = convert_units(args["value"], args["from_unit"], args["to_unit"])
                else:
                    result = "Unknown tool."
                
                # Add tool result to messages
                messages.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": result
                })
            
            # Get final response after tool use
            final_response = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=messages
            )
            ai_reply = final_response.choices[0].message.content
        else:
            # No tool needed, direct response
            ai_reply = response.choices[0].message.content
        
        # Add AI reply to history and print
        messages.append({"role": "assistant", "content": ai_reply})
        print(f"Chat Agent: \n{ai_reply}")
        print("-" * 50)


# Run the agent
if __name__ == "__main__":
    chat_agent()