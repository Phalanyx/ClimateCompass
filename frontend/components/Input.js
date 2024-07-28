"use client";

import { useState } from 'react';

function Input() {
    const [searchValue, setSearchValue] = useState('');
    const [response, setResponse] = useState('');
    const handleInputChange = (event) => {
        setSearchValue(event.target.value);
    };

    const handleButtonClick = () => {

        axios.post('http://127.0.0.1:8000/api', {
            lat: searchValue,
            lon: searchValue
        }).then((response) => {
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