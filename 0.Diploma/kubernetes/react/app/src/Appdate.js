import React, { Fragment, useState, useEffect } from 'react';
import './App.css';

const Appdate = () => {
    useEffect(() => {
        const getAPI = () => {
            // Change this endpoint to whatever local or online address you have
            // Local PostgreSQL Database
            const API = '/get/?entry_id=RUS';

            fetch(API)
                .then((response) => {
                    console.log(response);
                    return response.json();
                })
                .then((data) => {
                    console.log(data);
                    setApiData(data);
                });
        };
        getAPI();
    }, []);
    const [apiData, setApiData] = useState([]);
    return (
        <Fragment>
            <header>
                <h1>Covid statistics by date</h1>
            </header>        
                {(
                    <main>
                        <th>Country</th>
                        <th>date</th>
                        <th>confirmed</th>
                        <th>deaths</th>
                        <th>stringency_actual</th>
                        <th>stringency</th>

                    {apiData.map((field) => {
                        const country_code = field[1];
                        const date_value = field[2];
                        const confirmed = field[3];
                        const deaths = field[4];
                        const stringency_actual = field[5];
                        const stringency = field[6];
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
                        </main>
                )}
            
        </Fragment>
    );
};

export default Appdate;

