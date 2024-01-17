import React, { useState } from 'react';
import axios from 'axios';

function HomePage() {
    const [id, setId]  = useState();
    const [data, setData] = useState();

    const fetchData = () => {
        const apiUrl = "http://localhost:8000/movements/account-type"
        
        axios.get(apiUrl, { params: { id } })
        .then(response => {
            setData(response.data);
        })
        .catch(error => {
            console.error("Error fetching data", error);
        });
    };

    return (
        <div>
            <h1>Hello, World!</h1>
            <input type='int' value={id} onChange={(e) => setId(e.target.value)}/>
            <button onClick={fetchData}>Fetch Data</button>
            <p>{data && data.account_type_name}</p>
        </div>
    );
}

export default HomePage;