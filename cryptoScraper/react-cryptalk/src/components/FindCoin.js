import React, {useState} from 'react';
import {Button, Form, Input, Header} from 'semantic-ui-react'

export const FindCoin = () => {
    const [searchedCoin, setSearchedCoin] = useState("");
    const [toDelete, setToDelete] = useState("");
    var foundName = useState("X");
    return (
        <Form>
            <Form.Field>
                <Input placeholder="Coin ticker"
                       value={searchedCoin}
                       onChange={e => setSearchedCoin(e.target.value)}
                />
            </Form.Field>
            <Form.Field>
                <Button
                onClick={async () => {
                    console.log(foundName);
                    console.log("/getcoin?id=" + searchedCoin);
                    const response = await fetch("/getcoin?id=" + searchedCoin);
                    const data = await response.json();
                    setSearchedCoin(data.Name)
                    if (response.ok) {
                        console.log(foundName);

                    }
                }}>
                </Button>
                <Header>
                    {searchedCoin}
                </Header>
            </Form.Field>

            <Form.Field>
                <Input placeholder="Coin ID to delete"
                       value={toDelete}
                       onChange={e => setToDelete(e.target.value)}
                />
            </Form.Field>
            <Form.Field>
                <Button
                    onClick={async () => {
                        const response = await fetch("/deletecoin?id=" + toDelete, { method: 'DELETE'});
                        const data = await response.json();
                        if (response.ok) {
                            console.log(foundName);

                        }
                    }}>
                </Button>

            </Form.Field>

        </Form>
    );
};