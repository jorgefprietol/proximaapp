import React, { useState,useEffect } from 'react';

export default function Contentbody() {
  const [ditto, setDitto] = useState();
  const [loaded, setLoaded] = useState(false);

  const List = (props) => (
    <ul>
        {
            props.items.map((item, i) => {
                return <li key={i}><p>{i+1} - {item.date} - ${item.close}</p></li>
            })
        }
    </ul>
  )
  
  useEffect(() => {
    fetch('http://127.0.0.1:5000/currency')
    .then((res) => res.json())
    .then((data) => setDitto(data))
    .catch((err) => console.log(err))
    .finally(() => setLoaded(true));
  }, []);

  return <div>{loaded ? <div><h1>History from DB EUR-USD :</h1> <List items={ditto.EURUSDQuery} /> </div> : <h2>Loading...</h2>}</div>;
}