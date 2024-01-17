import React, { useEffect, useState } from 'react';
import axios from 'axios';
import AccountTypes from './components/AccountTypes';
import AccountTypeLoadingComponent from './components/AccountTypeLoading';


function App() {
    const AccountTypeLoading = AccountTypeLoadingComponent(AccountTypes);
    const [appState, setAppState] = useState({
        loading: false,
        accountTypes: null,
    });

    useEffect(() => {
        setAppState({ loading: true });
        const apiUrl = "http://127.0.0.1:8000/api/account-types";
        
        axios.get(apiUrl)
            .then((response) => {
                console.log(response.data);
                response.data.json();
            })
            .then((accountTypes) => {
                setAppState({ loading: false, accountTypes: accountTypes });
            });
    }, [setAppState]);

    return (
        <div className='App'>
            <h1>Latest account types</h1>
            <AccountTypeLoading isLoading={appState.loading} accountTypes={appState.accountTypes}/>
        </div>
    );
}

export default App;