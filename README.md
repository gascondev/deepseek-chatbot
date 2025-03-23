# 🗣️ DeepSeek Chatbot with Ollama API  

A simple Python chatbot that interacts with the **DeepSeek** model via the **Ollama API**. It maintains a conversation history to provide context-aware responses.  

## 🚀 Features  
- Interacts with the **DeepSeek** model.  
- Maintains **conversation history** for better context.  
- Uses **environment variables** for API configuration.  

## 📦 Installation  

1. **Clone the repository**  
   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
   ```

2. **Create a virtual environment (optional but recommended)**  
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the `.env` file**  
   Create a `.env` file in the root directory and add:  
   ```env
   OLLAMA_URL=http://127.0.0.1:11434/api/chat
   ```

## ▶️ Usage  

Run the chatbot with:  
```bash
python main.py
```

Type your messages in the terminal and receive responses from the **DeepSeek** model.  
To exit, type **"exit"**.  

## 🛠 Dependencies  
- Python 3.x  
- `requests`  
- `python-dotenv`  

Install them with:  
```bash
pip install requests python-dotenv
```

## 📜 License  
This project is licensed under the **MIT License**.  
 
