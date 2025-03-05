import React, { useState, useRef } from "react";
import ReactMarkdown from 'react-markdown';
import "./index.css";

const Chat: React.FC = () => {
    const [messages, setMessages] = useState<{ text: string; user: boolean }[]>([]);
    const [input, setInput] = useState("");
    const [isLoading, setIsLoading] = useState(false);
    const chatMessagesRef = useRef<HTMLDivElement>(null);

    const sendMessage = async () => {
        if (input.trim() === "" || isLoading) return;

        setMessages(prevMessages => [...prevMessages, { text: input, user: true }]);
        setInput("");
        setIsLoading(true);

        try {
            const response = await fetch('/api/v1/chat-messages', {
                method: 'POST',
                headers: {
                    "Authorization": "Bearer app-h5HAMxK3x0mIcqpNct8Lq2p8",
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    "inputs": {},
                    "query": input,
                    "response_mode": "streaming",
                    "conversation_id": "",
                    "user": "Ernest",
                    "files": [] // Optional: Add files array if needed
                }),
            });

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            

            const reader = response.body?.getReader();
            let partialLine = '';
            let botResponse = '';

            if (reader) {
                while (true) {
                    const { done, value } = await reader.read();
                    if (done) break;

                    // Convert the chunk to text and combine with any partial line from previous chunk
                    const chunk = new TextDecoder().decode(value);
                    const lines = (partialLine + chunk).split('\n');
                    
                    // Save the last partial line for next chunk
                    partialLine = lines.pop() || '';

                    for (const line of lines) {
                        if (line.startsWith('data:')) {
                            try {
                                // Remove 'data:' prefix and parse JSON
                                const jsonStr = line.slice(5).trim();
                                if (jsonStr) {
                                    const data = JSON.parse(jsonStr);
                                    if (data.event === 'message') {
                                        botResponse += data.answer || '';
                                        // Update the last bot message or add a new one
                                        setMessages(prev => {
                                            const updated = [...prev];
                                            if (updated.length > 0 && !updated[updated.length - 1].user) {
                                                updated[updated.length - 1] = { 
                                                    text: botResponse, 
                                                    user: false 
                                                };
                                            } else {
                                                updated.push({ 
                                                    text: botResponse, 
                                                    user: false 
                                                });
                                            }
                                            return updated;
                                        });
                                    } else if (data.event === 'error') {
                                        throw new Error(data.message || 'Stream error');
                                    }
                                }
                            } catch (e) {
                                console.error('Error parsing SSE data:', e);
                            }
                        }
                    }
                }
            }
        } catch (error) {
            console.error('Error:', error);
            setMessages(prev => [...prev, { 
                text: `Error: ${error instanceof Error ? error.message : 'An unknown error occurred'}`, 
                user: false 
            }]);
        } finally {
            setIsLoading(false);
        }
    };

    return (
        <div className="chat-container">
            <header className="chat-header">Chat Robot</header>
            <div className="chat-messages" ref={chatMessagesRef}>
                {messages.map((msg, index) => (
                    <div key={index} className={`message ${msg.user ? "user" : "bot"}`}>
                        {msg.user ? (
                            msg.text
                        ) : (
                            <ReactMarkdown>{msg.text}</ReactMarkdown>
                        )}
                    </div>
                ))}
            </div>
            <div className="chat-input-container">
                <input
                    type="text"
                    value={input}
                    onChange={(e) => setInput(e.target.value)}
                    className="chat-input"
                    placeholder={isLoading ? "Waiting for response..." : "Ask anything"}
                    disabled={isLoading}
                    onKeyDown={(e) => e.key === "Enter" && !isLoading && sendMessage()}
                />
                <button 
                    onClick={sendMessage} 
                    className="send-button"
                    disabled={isLoading}
                >
                    {isLoading ? "..." : "➤"}
                </button>
            </div>
        </div>
    );
};

export default Chat;