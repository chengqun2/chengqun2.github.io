import React, { useState, useEffect } from 'react';
import axios from 'axios';

interface UrlRecord {
    short_id: string;
    target_url: string;
}

const ShortenUrl: React.FC = () => {
    const [inputValue, setInputValue] = useState('');
    const [urlList, setUrlList] = useState<UrlRecord[]>([]);
    const [error, setError] = useState('');

    // Fetch all URLs when component mounts
    useEffect(() => {
        fetchUrls();
    }, []);

    const fetchUrls = async () => {
        try {
            const response = await axios.get('/urls');
            setUrlList(response.data);
        } catch (err) {
            setError('Failed to fetch URLs');
        }
    };

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        try {
            const response = await fetch('/shorten', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ target_url: inputValue }),
            });
            const data = await response.json();
            console.log(data)
            // Refresh the URL list
            fetchUrls();
            
            // Clear the input
            setInputValue('');
        } catch (err) {
            setError('Failed to shorten URL');
        }
    };

    return (
        <div>
            <form onSubmit={handleSubmit}>
                <input
                    type="text"
                    value={inputValue}
                    onChange={(e) => setInputValue(e.target.value)}
                    placeholder="Enter URL here"
                />
                <button type="submit">Submit</button>
            </form>

            {error && <p style={{ color: 'red' }}>{error}</p>}

            <div>
                <h2>Shortened URLs</h2>
                <ul>
                    {urlList.map((item, index) => (
                        <li key={index}>
                            Original: {item.target_url} <br/>
                            Shortened: {item.short_id}
                        </li>
                    ))}
                </ul>
            </div>
        </div>
    );
};

export default ShortenUrl;