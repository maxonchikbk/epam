import React, { Fragment, useState, useEffect } from 'react';
import './App.css';

const App = () => {
    useEffect(() => {
        const getAPI = () => {
            // Change this endpoint to whatever local or online address you have
            // Local PostgreSQL Database
            const API = 'http://172.19.183.247/getcovid/?entry_id=RUS';

            fetch(API)
                .then((response) => {
                    console.log(response);
                    return response.json();
                })
                .then((data) => {
                    console.log(data);
                    setLoading(false);
                    setApiData(data);
                });
        };
        getAPI();
    }, []);
    const [apiData, setApiData] = useState([]);
    const [loading, setLoading] = useState(true);
    return (
        <Fragment>
            <header>
                <h1>Covid statistics</h1>
            </header>
            <div className="form-container">
                <h2>Choose country</h2>
                <div>

                </div>  
                <form method="GET" action="http://172.19.183.247/getcovid/">
                    <div>
                        <input type="text" name="entry_id" required />
                    </div>
                    <div>
                        <button type="submit">Apply</button>
                    </div>
                </form>
            </div>
            <main>
                {(
                    <table>
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
                                    <td>
                                        {country_code}
                                    </td>
                                    <td>
                                         {date_value}
                                    </td>
                                    <td>
                                         {confirmed}
                                    </td>
                                    <td>
                                         {deaths}
                                    </td>
                                    <td>
                                         {stringency_actual}
                                    </td>
                                    <td>
                                         {stringency}
                                    </td>
                              </tr>
                              
                           );  
                        })}
                      </tbody>  
                    </table>
                )}
            </main>
        </Fragment>
    );
};

export default App;

