"use client";

import React from 'react';
import Image from 'next/image';
import image from '../images/image.svg';
import { useState } from 'react';
import Resources from "./Resources";
import axios from 'axios';
const Hero = () => {


  const [state , setState] = useState(0);
  const [newResp, setResponse] = useState({});
  

  const handleButtonClick = () => {

    var val = {address:"Jasper, Alberta"}
    console.log(val)
    axios.post('http://127.0.0.1:8000/main/api/', val).then(response => {
        console.log(response.data);
        const data = response.data;
        setResponse(data);
        setState(1);
    }).catch((error) => {
        console.log(error);
    });


};

  
return (
  !state ?
  
    <section className="bg-blue-frostedLight">
      <div className="grid max-w-screen-xl px-4 pt-20 pb-8 mx-auto lg:gap-8 xl:gap-0 lg:py-16 lg:grid-cols-12 lg:pt-28">
        <div className="mr-auto place-self-center lg:col-span-7">
          <h1 className="max-w-2xl mb-4 text-4xl font-extrabold leading-none tracking-tight md:text-5xl xl:text-6xl text-black">
            Climate Compass
          </h1>
          <p className="max-w-2xl mb-6 font-light text-gray-800 lg:mb-8 md:text-lg lg:text-xl">
            Welcome to Climate Compass, a website where, given your location, we can show you...
          </p>

      
  <div className="flex relative rounded-md w-full px-4 max-w-xl">
    <input
      type="text"
      name="q"
      id="query"
      placeholder="Where you located/planning on locating?"
      className="w-full p-3 rounded-md rounded-r-none border-2 border-gray-300 placeholder-gray-500 dark:placeholder-gray-300 dark:bg-gray-500 dark:text-gray-300 dark:border-none"
    />
    <button onClick={handleButtonClick}
      className="inline-flex items-center gap-2 bg-blue-frostedDark text-white text-lg font-semibold py-3 px-6 rounded-r-md"
    > 
      <span>Search</span>
      <span className="hidden md:block">
        <svg
          className="text-gray-200 h-5 w-5 p-0 fill-current"
          xmlns="http://www.w3.org/2000/svg"
          viewBox="0 0 56.966 56.966"
          width="512px"
          height="512px"
        >
          <path
            d="M55.146,51.887L41.588,37.786c3.486-4.144,5.396-9.358,5.396-14.786c0-12.682-10.318-23-23-23s-23,10.318-23,23  s10.318,23,23,23c4.761,0,9.298-1.436,13.177-4.162l13.661,14.208c0.571,0.593,1.339,0.92,2.162,0.92  c0.779,0,1.518-0.297,2.079-0.837C56.255,54.982,56.293,53.08,55.146,51.887z M23.984,6c9.374,0,17,7.626,17,17s-7.626,17-17,17  s-17-7.626-17-17S14.61,6,23.984,6z"
          />
        </svg>
      </span>
      </button>
  </div>


        </div>
        <div className="hidden lg:mt-0 lg:col-span-5 lg:flex border border-black">
  <Image
    src={image}
    alt="Compass"
    layout="responsive"
    width={500}
    height={500}
    className="w-full h-auto max-w-full"
  />
</div>

      </div>
    </section>

    :
    <div>
    <Resources type={newResp.type.episode_type} refuge={newResp.refuge} news={newResp.news}></Resources>
    </div>
  );
};

export default Hero;
