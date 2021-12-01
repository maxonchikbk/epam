import React, { Fragment, useState, useCallback } from 'react';
import './App.css';

function useInput(initialState) {
    const [state,setState] = useState(initialState);

    const setInput = (event) => {
        console.dir(event);
        if (event) {
            if (event.currentTarget !== undefined) {
                setState(event.currentTarget.value);
            } else {
                setState(event);
            }
        }
    };
    console.dir(state);
    return [state,setInput];
}

const App = () => {
    const [entry_id, setid] = useInput('');    
        const getAPI = useCallback(() => {
            const API = `/get/?entry_id=${entry_id}`;            
                                   
            fetch(API)
                .then((response) => {
                    console.log(response);
                    return response.json();
                })
                .then((data) => {
                    console.log(data);
                    setApiData(data);
                });
        },        
    [entry_id]);

    const [apiData, setApiData] = useState([]);
    return (
        <Fragment>
            <header>
                <h1>Covid statistics</h1>
            </header>
            <div className="form-container">
                <form method="GET" action="/getall">
                        <button type="submit">Get all data</button>
                        </form>
                <h2>Choose country</h2>
                <form>
                    <div>
                        <input type="text" required name="entry_id" value={entry_id} onChange={setid} />
                    </div>
                    <div>
                        <button onClick={getAPI}>Apply</button>
                    </div>
                </form>
            </div>
            <table>
                {(
                      <tbody>
                                <th>Country</th>
                                <th>date</th>
                                <th>confirmed</th>
                                <th>deaths</th>
                                <th>stringency_actual</th>
                                <th>stringency</th>
                            {apiData.map((field) => {
                                const country_code = field[0];
                                const date_value = field[2];
                                const confirmed = field[1];
                                const deaths = field[3];
                                const stringency_actual = field[4];
                                const stringency = field[5];         

                            return (
                                <tr>
                                    <td>{country_code}</td>
                                    <td>{date_value}</td>
                                    <td>{confirmed}</td>
                                    <td>{deaths}</td>
                                    <td>{stringency_actual}</td>
                                    <td>{stringency}</td>
                                </tr>
                            );
                        })}
                        </tbody>
                )}
                </table>
        </Fragment>
    );
};

export default App;