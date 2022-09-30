import React from 'react';
import Navbar from './Navbar';

function Header() {
  return (
    <div id='main'>
        <Navbar/>
        <div className='name'>
            <h1 className='h1'>Unlock nearshore resources & insurtech capabilities</h1>
            <p className='details'>We deliver transformation</p>  
            <a href='#' className='cv-btn'>Discover How -></a>
        </div>

    </div>
  );
}

export default Header;