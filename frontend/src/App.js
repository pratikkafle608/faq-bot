import React, { useState, useRef, useEffect } from 'react';
import { Send, Bot, User } from 'lucide-react'; // Importing icons from lucide-react

function App() {
  // State to store all messages in the chat (user and bot)
  const [messages, setMessages] = useState([]);
  // State to store the current input value from the user
  const [input, setInput] = useState('');
  // Ref to automatically scroll to the bottom of the chat
  const messagesEndRef = useRef(null);

  // Function to scroll to the latest message
  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  // Effect to scroll to bottom whenever messages state updates
  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  // Function to handle sending a message
  const handleSendMessage = async (e) => {
    e.preventDefault(); // Prevent default form submission behavior (page reload)
    if (input.trim() === '') return; // Don't send empty messages

    // Add user's message to the chat
    const newUserMessage = { text: input, sender: 'user' };
    setMessages((prevMessages) => [...prevMessages, newUserMessage]);
    setInput(''); // Clear the input field

    try {
      // Show a "typing" indicator or placeholder for the bot's response
      const botTypingMessage = { text: 'Bot is typing...', sender: 'bot', id: 'typing-indicator' };
      setMessages((prevMessages) => [...prevMessages, botTypingMessage]);

      // Make a POST request to your Python backend
      const response = await fetch('http://127.0.0.1:5000/ask', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ question: input }), // Send the user's question
      });

      // Check if the response was successful
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const data = await response.json(); // Parse the JSON response from the backend

      // Remove the typing indicator
      setMessages((prevMessages) => prevMessages.filter(msg => msg.id !== 'typing-indicator'));

      // Add bot's response to the chat
      const newBotMessage = { text: data.answer, sender: 'bot' };
      setMessages((prevMessages) => [...prevMessages, newBotMessage]);

    } catch (error) {
      console.error("Error fetching bot response:", error);
      // Remove typing indicator if an error occurred
      setMessages((prevMessages) => prevMessages.filter(msg => msg.id !== 'typing-indicator'));
      // Display an error message to the user
      setMessages((prevMessages) => [...prevMessages, { text: 'Oops! Something went wrong. Please try again later.', sender: 'bot', isError: true }]);
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100 flex items-center justify-center p-4">
      <div className="w-full max-w-md bg-white rounded-xl shadow-2xl overflow-hidden flex flex-col h-[80vh]">
        {/* Chat Header */}
        <div className="bg-gradient-to-r from-blue-600 to-indigo-700 text-white p-4 flex items-center justify-center rounded-t-xl shadow-md">
          <Bot className="mr-2" size={24} />
          <h1 className="text-xl font-semibold">A&M-Texarkana FAQ Bot</h1>
        </div>

        {/* Messages Display Area */}
        <div className="flex-1 p-4 overflow-y-auto custom-scrollbar">
          {messages.length === 0 && (
            <div className="text-center text-gray-500 mt-10">
              <p>Type a question to get started!</p>
              <p className="text-sm">e.g., "What is the university name?", "How to make payment?"</p>
            </div>
          )}
          {messages.map((msg, index) => (
            <div
              key={index}
              className={`flex items-start mb-4 ${
                msg.sender === 'user' ? 'justify-end' : 'justify-start'
              }`}
            >
              {msg.sender === 'bot' && (
                <div className="flex-shrink-0 mr-2">
                  <Bot className="text-blue-500" size={20} />
                </div>
              )}
              <div
                className={`max-w-[75%] p-3 rounded-xl shadow-md ${
                  msg.sender === 'user'
                    ? 'bg-blue-500 text-white rounded-br-none'
                    : 'bg-gray-100 text-gray-800 rounded-bl-none'
                } ${msg.isError ? 'bg-red-200 text-red-800' : ''}`}
              >
                {/* Render text with line breaks for bot answers */}
                {msg.text.split('\n').map((line, i) => (
                  <p key={i}>{line}</p>
                ))}
              </div>
              {msg.sender === 'user' && (
                <div className="flex-shrink-0 ml-2">
                  <User className="text-indigo-500" size={20} />
                </div>
              )}
            </div>
          ))}
          <div ref={messagesEndRef} /> {/* Element to scroll into view */}
        </div>

        {/* Input Form */}
        <form onSubmit={handleSendMessage} className="p-4 bg-gray-50 border-t border-gray-200 flex items-center rounded-b-xl shadow-inner">
          <input
            type="text"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            placeholder="Ask a question..."
            className="flex-1 p-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 transition duration-200 mr-2"
          />
          <button
            type="submit"
            className="bg-blue-600 hover:bg-blue-700 text-white p-3 rounded-lg shadow-lg transition duration-300 ease-in-out transform hover:scale-105 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2 flex items-center justify-center"
          >
            <Send size={20} />
            <span className="ml-2 hidden sm:inline">Send</span>
          </button>
        </form>
      </div>
    </div>
  );
}

export default App;
