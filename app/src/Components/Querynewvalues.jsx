import React, { useState,useEffect } from 'react';
import Contentbody from './Contentbody';

export default function Querynewvalues() {
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
    fetch('http://127.0.0.1:5000/scrape_currency')
    .then((res) => res.json())
    .then((data) => setDitto(data))
    .catch((err) => console.log(err))
    .finally(() => setLoaded(true));
  }, []);

  return <div className='presentaion'>{loaded ? <div> 
    <h1>Values from Yahoo EUR-USD : <a href='javascript:location.reload();' className='cv-btn'>Update</a></h1> 
    { ditto.EURUSDInsert.length !== 0 ? <List items={ditto.EURUSDInsert} /> : <h2>No new data for the last 5 different days...</h2> } <Contentbody/> </div> : <h2>Loading...</h2>}</div>;
}