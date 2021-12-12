import React from 'react';
import 'semantic-ui-css/semantic.min.css';
import {List, Header, Rating} from "semantic-ui-react";


export const Coins = ({coins}) => {
    return (
        <List>
            {coins.map(coin => {
                return (
                    <List.Item key={coin.name}>
                        <Header>{coin.name}</Header>
                        <Rating rating={coin.score} maxRating={30} disabled />
                    </List.Item>
                );
            })}
        </List>
    );
};