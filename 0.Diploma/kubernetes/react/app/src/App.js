import React, { Fragment, useState, useCallback } from 'react';
import './App.css';

function useInput(initialState) {
    const [state,setState] = useState(initialState);

    const setInput = (event) => {
        // console.dir(event);
        if (event) {
            if (event.currentTarget !== undefined) {
                setState(event.currentTarget.value);
            } else {
                setState(event);
            }
        }
    };
    // console.dir(state);
    return [state,setInput];
}

const App = () => {
    const [entry_id, setid] = useInput('');    
    const [apiData, setApiData] = useState([]);
    const getAPI = useCallback((event) => {
        event.preventDefault();

        const API = `/get/?entry_id=${entry_id}`;            
        
        // console.log(API);
            fetch(API)
                .then((response) => {
                    return response.json();
                })
                .then((data) => {                    
                    setApiData(data);
                });
    }, [entry_id]);

    return (
        <Fragment>
            <header>
                <h1>Covid statistics</h1>
            </header>
            <div className="form-container">
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
                {(
                  <table>                    
                    <thead>
                        <tr>
                            {/* <th>Country</th> */}
                            <th>Date</th>
                            <th>Confirmed</th>
                            <th>Deaths</th>
                            <th>Stringency actual</th>
                            <th>Stringency</th>
                        </tr>
                    </thead>
                            <tbody>
                            {apiData.map((field, index) => {
                                // const country_code = field[1];
                                const date_value = field[2];
                                const confirmed = field[3];
                                const deaths = field[4];
                                const stringency_actual = field[5];
                                const stringency = field[6];         

                            return (
                                <tr key={index}>
                                    {/* <td>{country_code}</td> */}
                                    <td>{date_value}</td>
                                    <td>{confirmed}</td>
                                    <td>{deaths}</td>
                                    <td>{stringency_actual}</td>
                                    <td>{stringency}</td>
                                    
                                </tr>
                            );
                        })}
                        </tbody>
                    </table>
                )}                
        </Fragment>
    );
};

export default App;