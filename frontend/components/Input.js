"use client";

import { useState } from 'react';
import axios from 'axios';
function Input() {
    const [searchValue, setSearchValue] = useState('');
    const [response, setResponse] = useState('');
    const handleInputChange = (event) => {
        setSearchValue(event.target.value);
    };

    const handleButtonClick = () => {
        var val = {lat: 15.1666665 , lon: 47.2500001}
        console.log(val)
        axios.post('http://127.0.0.1:8000/main/api/', val).then(response => {
            setResponse(response.data);
            console.log(response.data);
        }).catch((error) => {
            console.log(error);
        });

    };

    return (
        <div>
            <h1>Address</h1>
            <input type="text" value={searchValue} onChange={handleInputChange}/>
            <button onClick={handleButtonClick}>Search</button>
        </div>
    );
}

export default Input