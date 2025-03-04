import { useState, useRef } from 'react';
import React from 'react';
import './index.css';

const Chat: React.FC = () => {
    const [chatResponse, setChatResponse] = useState<string>('')
    const textareaRef = useRef<HTMLTextAreaElement>(null);
    const handleSubmit = async () => {
        try {
            const inputText = textareaRef.current?.value || '';
            console.log(inputText)
            const url = 'http://localhost:11434/api/generate'
            fetch(url, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    "model": "deepseek-r1:1.5b",  
                    "prompt": inputText,
                    "stream": false
                }),
            })
            .then(response => response.json())
            .then(data => {
                console.log(data)
                setChatResponse(data.response)
            })
            .catch(error => console.error('Error:', error));
        } catch (error) {
            console.error('Error:', error);
        }
    };
    return (
        <div>
            <div className="input-box-container">
                <div className="input-box-container-input">
                    <textarea 
                        ref={textareaRef}
                        placeholder="Ask something"
                        defaultValue="">
                    </textarea>
                </div>
                <div style={{ position: 'relative', width: '100%' }}>
                    <button 
                        onClick={handleSubmit} 
                        style={{ 
                            backgroundColor: 'black', 
                            color: 'white', 
                            padding: '10px 20px', 
                            fontSize: '16px',
                            border: 'none',
                            borderRadius: '10px',
                            cursor: 'pointer',
                            position: 'absolute',
                            top: '10px',
                            right: '10px'
                        }}>
                        Send
                    </button>
                </div>
            </div>
            <div className='answer-box-contaner'>
                <p>{chatResponse}</p>
            </div>
        </div>
        
    );
};

export default Chat;