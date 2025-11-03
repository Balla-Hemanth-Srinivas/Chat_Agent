# Chat Agent with Tools 🤖

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![Python](https://img.shields.io/badge/python-v3.7+-blue.svg)](https://www.python.org/)

A powerful, conversational AI chat agent built with the Groq API, featuring integrated tools for web searching, calculations, time retrieval, Wikipedia summaries, weather checks, and unit conversions. This project demonstrates tool-calling capabilities in AI agents, allowing dynamic interactions beyond basic chat.

## ✨ Features

- **Conversational AI**: Powered by Groq's Llama 3.1 model for natural language responses
- **Tool Integration**: Automatically calls tools based on user queries:
  - 🔍 Web Search: Fetch real-time information from the web using DuckDuckGo
  - 🧮 Calculator: Perform simple math expressions
  - 🕒 Current Time: Get the local date and time
  - 📚 Wikipedia Search: Retrieve summaries from Wikipedia
  - 🌤️ Weather Lookup: Check current weather for any city (requires OpenWeatherMap API key)
  - 📏 Unit Conversion: Convert between units (e.g., length, weight, temperature)
- **User-Friendly**: Displays numbered action options before each input for easy reference
- **Free and Accessible**: Uses free-tier APIs where possible; no cost for basic usage
## 📋 Requirements

- Python 3.7 or higher
- Internet connection for API calls
- API keys:
  - Groq API key (required)
  - OpenWeatherMap API key (optional, for weather tool)

## 🚀 Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/chat-agent-tools.git
   cd chat-agent-tools
   ```

2. **Create a Virtual Environment** (recommended)
   ```bash
   # Create virtual environment
   python -m venv venv

   # Activate virtual environment
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```


4. **Set Up API Keys**

   - **Groq API Key**: 
     - Sign up at [console.groq.com](https://console.groq.com)
     - Replace `"your_groq_api_key_here"` in `chat_agent.py`
   
   - **OpenWeatherMap API Key** (optional):
     - Sign up at [openweathermap.org](https://openweathermap.org)
     - Replace `"your_openweathermap_api_key_here"` in `tools.py`

## 🎮 Usage

1. **Run the agent**
   ```bash
   python chat_agent.py
   ```

2. **Try these example queries**:
   - 🔍 `"Search for latest AI news"`
   - 🧮 `"Calculate 5 + 3 * 2"`
   - 🕒 `"What time is it?"`
   - 📚 `"Tell me about Python"`
   - 🌤️ `"What's the weather in London?"`
   - 📏 `"Convert 100 meters to feet"`
   - 💬 Or just chat: `"Tell me a joke"`

3. Type `quit` to exit

## 💡 Example Interaction

```plaintext
Chat Agent: Hi! I'm a conversational AI with tools. Ask me anything, or type 'quit' to exit.

Available actions you can ask for:
1) web_search: Search the web (e.g., 'Search for latest AI news')
2) calculate: Do math (e.g., 'Calculate 5 + 3 * 2')
...

You: What time is it?
Chat Agent: The current time is 2023-10-05 14:30:00
```
## 📁 Project Structure

```plaintext
.
├── chat_agent.py     # Main script for the chat agent and tool handling
├── tools.py          # Definitions for all tool functions
└── requirements.txt  # List of Python dependencies
```

## 🤝 Contributing

Contributions are always welcome! Here's how you can help:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

For major changes, please open an issue first to discuss what you would like to change.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Powered by [Groq](https://groq.com) for fast AI inference
- Tools use free APIs from:
  - [DuckDuckGo](https://duckduckgo.com)
  - [Wikipedia](https://wikipedia.org)
  - [OpenWeatherMap](https://openweathermap.org)
