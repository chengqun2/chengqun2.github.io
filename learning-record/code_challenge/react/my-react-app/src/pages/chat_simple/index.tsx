import { useState, useRef } from 'react';
import React from 'react';
import './index.css';

const Chat: React.FC = () => {
    const [chatResponse, setChatResponse] = useState<string>('')
    const textareaRef = useRef<HTMLTextAreaElement>(null);
    const handleSubmit = async () => {
        try {
            const inputText = textareaRef.current?.value || '';
            const url = 'http://localhost:11434/api/generate'
            const response = await fetch(url, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    "model": "deepseek-r1:1.5b",  
                    "prompt": inputText,
                    "stream": true
                }),
            });

            const reader = response.body?.getReader();
            let accumulatedResponse = '';

            if (reader) {
                while (true) {
                    const { done, value } = await reader.read();
                    if (done) break;

                    // Convert the Uint8Array to text
                    const chunk = new TextDecoder().decode(value);
                    const lines = chunk.split('\n').filter(line => line.trim());
                    
                    for (const line of lines) {
                        const data = JSON.parse(line);
                        accumulatedResponse += data.response;
                        setChatResponse(accumulatedResponse);
                    }
                }
            }
        } catch (error) {
            console.error('Error:', error);
        }
    };
    return (
        <div>
            <div className="input-box-container"
                onKeyDown={(e) => {
                    if (e.key === 'Enter' && !e.shiftKey) {
                        e.preventDefault();
                        handleSubmit();
                    }
                }}>
                <div className="input-box-container-input">
                    <textarea
                        ref={textareaRef}
                        placeholder="Ask something"
                        defaultValue="">
                    </textarea>
                </div>
                <div className='button-container'>
                    <button className='button-send'
                        onClick={handleSubmit}
                    >
                        Send
                    </button>
                </div>
            </div>
            <div className='answer-box-contaner' 
                 ref={(el) => {
                     if (el) {
                         el.scrollTop = el.scrollHeight;
                     }
                 }}>
                <div className="chat-response" 
                     dangerouslySetInnerHTML={{ 
                         __html: chatResponse
                             .replace(/\n/g, '<br/>')
                             .replace(/#{4,}/g, '')
                             .replace(/###\s(.*?)\n/g, '<h3>$1</h3>')
                             .replace(/##\s(.*?)\n/g, '<h2>$1</h2>')
                             .replace(/#\s(.*?)\n/g, '<h1>$1</h1>')
                     }} 
                />
            </div>
        </div>
        
    );
};

export default Chat;