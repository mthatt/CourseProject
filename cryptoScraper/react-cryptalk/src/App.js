import React, { useState, useEffect } from 'react';
import logo from './logo.svg';
import './App.css';
import {Coins} from "./components/Coins";
import {FindCoin} from "./components/FindCoin";
import { Container } from "semantic-ui-react";

function CoinPage() {
    const [coins, setCoins] = useState([]);

    useEffect(() => {
        fetch('/getcoins').then(res => res.json()).then(data => {
            setCoins(data);
        });
    }, []);

    return (
        <div className="App">
            <Container style={{marginTop: 30}}>
                <FindCoin />
                <Coins coins = {coins}/>
            </Container>
        </div>
    );
}

export default CoinPage;