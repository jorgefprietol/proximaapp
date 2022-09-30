import React, {useState} from 'react';
import logo from '../images/logo.png';
import arrow from '../images/chevron-down-solid.svg';
function Navbar() {

    const [nav,setnav] = useState(false);

    const changeBackground = () => {
        if(window.scrollY >= 50) {
            setnav(true);
        }else{
            setnav(false);
        }
    }
window.addEventListener('scroll', changeBackground);
  return (
    <nav className={nav ? 'nav active' : 'nav'}>
        <a href='#' className='logo'>
            <img src={logo} alt='' /><span className='new'>PROXIMA</span>
        </a>
        <input type='checkbox' className='menu-btn' id='menu-btn'/>
        <label className='menu-icon' for='menu-btn'>
            <span className='nav-icon'></span>
        </label>
        <ul className='menu'>
            <li><a href='#'>About Us</a></li>
            <li><a href='#'>Nearshoring <img src={arrow} className='imgicon'/></a></li>
            <li><a href='#'>Insurtech <img src={arrow} className='imgicon'/></a></li>
            <li><a href='#'>Careers</a></li>
            <li><a href='#' className='active'>Contact Us</a></li>
        </ul>
    </nav>
  );
}

export default Navbar;
