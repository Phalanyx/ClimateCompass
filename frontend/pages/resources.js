
import '../app/globals.css'
import React from 'react'
import Image from 'next/image';
import compass from '../images/compass.svg';
import { Inter } from 'next/font/google';

const inter = Inter({ subsets: ['latin'] });

const resources = () => {
  return (
    <>
 <section className='bg-blue-frostedLight'>

 <nav class="sticky top-0 z-50 border-gray-200 bg-blue-frostedLight">
  <div class="max-w-screen-xl flex flex-wrap items-center justify-between mx-auto p-4">
    <a href=".." class="flex items-center space-x-3 rtl:space-x-reverse">
      <Image
        src={compass}
        alt="Compass"
        width={75}
        height={75}
        className="bg-transparent"
      />
      <span class="text-base self-center font-semibold whitespace-nowrap dark:text-black">Climate Compass</span>
    </a>
    <button data-collapse-toggle="navbar-solid-bg" type="button" class="inline-flex items-center p-2 w-10 h-10 justify-center text-sm text-gray-500 rounded-lg md:hidden hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-200 dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:ring-gray-600" aria-controls="navbar-solid-bg" aria-expanded="false">
      <span class="sr-only">Open main menu</span>
      <svg class="w-5 h-5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 17 14">
        <path stroke="currentColor" strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M1 1h15M1 7h15M1 13h15"/>
      </svg>
    </button>
    <div class="hidden w-full md:block md:w-auto" id="navbar-solid-bg">
      <ul class="flex flex-col font-medium mt-4 rounded-lg bg-gray-50 md:space-x-8 rtl:space-x-reverse md:flex-row md:mt-0 md:border-0 md:bg-transparent dark:bg-gray-800 md:dark:bg-transparent dark:border-gray-700">
        <li>
          <a href="#climatemap" class="block py-2 px-3 md:p-0 text-gray-900 rounded hover:bg-gray-100 md:hover:bg-transparent md:border-0 md:hover:text-blue-700 dark:text-white md:dark:hover:text-blue-500 dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent" aria-current="page">Climate Map</a>
        </li>
        <li>
          <a href="#migration" class="block py-2 px-3 md:p-0 text-gray-900 rounded hover:bg-gray-100 md:hover:bg-transparent md:border-0 md:hover:text-blue-700 dark:text-white md:dark:hover:text-blue-500 dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent">Migration Services</a>
        </li>
        <li>
          <a href="#moveto" class="block py-2 px-3 md:p-0 text-gray-900 rounded hover:bg-gray-100 md:hover:bg-transparent md:border-0 md:hover:text-blue-700 dark:text-white md:dark:hover:text-blue-500 dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent">Moving to this Area?</a>
        </li>
      </ul>
    </div>
  </div>
</nav>


 <div class="flex flex-1 w-full flex-col items-center justify-center text-center px-4 sm:mt-28 mt-20">
    <h1 className="mx-auto max-w-4xl font-display text-5xl font-bold tracking-normal text-slate-900 sm:text-7xl">
        <span className="relative whitespace-nowrap text-blue-Figma">
            <svg aria-hidden="true" viewBox="0 0 418 42" className="absolute top-2/3 left-0 h-[0.58em] w-full fill-blue-Figma/70" preserveAspectRatio="none"><path d="M203.371.916c-26.013-2.078-76.686 1.963-124.73 9.946L67.3 12.749C35.421 18.062 18.2 21.766 6.004 25.934 1.244 27.561.828 27.778.874 28.61c.07 1.214.828 1.121 9.595-1.176 9.072-2.377 17.15-3.92 39.246-7.496C123.565 7.986 157.869 4.492 195.942 5.046c7.461.108 19.25 1.696 19.17 2.582-.107 1.183-7.874 4.31-25.75 10.366-21.992 7.45-35.43 12.534-36.701 13.884-2.173 2.308-.202 4.407 4.442 4.734 2.654.187 3.263.157 15.593-.78 35.401-2.686 57.944-3.488 88.365-3.143 46.327.526 75.721 2.23 130.788 7.584 19.787 1.924 20.814 1.98 24.557 1.332l.066-.011c1.201-.203 1.53-1.825.399-2.335-2.911-1.31-4.893-1.604-22.048-3.261-57.509-5.556-87.871-7.36-132.059-7.842-23.239-.254-33.617-.116-50.627.674-11.629.54-42.371 2.494-46.696 2.967-2.359.259 8.133-3.625 26.504-9.81 23.239-7.825 27.934-10.149 28.304-14.005.417-4.348-3.529-6-16.878-7.066Z"></path></svg>
            <span className="relative">Climate Compass</span>
        </span>   
    </h1>

    <h2 className="mt-10 mx-auto max-w-4xl font-display text-3xl font-bold tracking-normal text-slate-900 sm:text-4xl flex items-center text-left">
      Results for (YOUR COUNTRY)
    </h2>
    <p class="mx-auto mt-12 max-w-xl text-lg text-slate-700 leading-7">Here, you will find the most
      <span className="font-bold"> essential </span> climate details about your
      specified location.</p>
      <nav className=" bg-black rounded-xl text-white font-medium px-4 py-3 sm:mt-10 mt-8 hover:bg-black/80">
        <p className="flex space-x-6 items-center justify-center">
          <a href="#climatemap" className="hover:underline font-mono flex items-center justify-center f">Climate Map</a>
          <a href="#migration" className="hover:underline font-mono flex items-center justify-center">Climate Migration Services</a>
          <a href="#moveto" className="hover:underline font-mono flex items-center justify-center">Thinking of moving to this area?</a>

        </p>
      </nav>
  </div>


<div className="relative opacity-75">

<h2 className="mt-5 text-2xl bg-white border border-black text-blue-900 font-semibold px-16 py-6 rounded-full hover:bg-blue-100 transition duration-300 text-center flex items-center justify-center">
          Climate Map
          <span className='ml-2'>
          <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#000000" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s-8-4.5-8-11.8A8 8 0 0 1 12 2a8 8 0 0 1 8 8.2c0 7.3-8 11.8-8 11.8z"/><circle cx="12" cy="10" r="3"/></svg>
          </span></h2>
      <div className="mt-10">
        <section id="climatemap" className="min-h-screen">
        <div className="w-full h-screen bg-gray-500 flex items-center justify-center">
  <div className="bg-blue-frostedLight w-full h-full border-black border ">
    <p className="text-center">Extremely Large Box For Data Pipe</p>
  </div>
</div>

        </section>
  

        <section id="migration" className="min-h-screen mt-10">
        <h2 className="bg-white border mt-5 text-2xl border-black text-blue-900 font-semibold px-16 py-6 rounded-full hover:bg-blue-100 transition duration-300 text-center flex items-center justify-center">
          Climate Migration Services
          <span className='ml-2'>
          <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#000000" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M16.2 7.8l-2 6.3-6.4 2.1 2-6.3z"/></svg>
          </span></h2>

          <div class="p-4 mx-auto mt-10 w-full">
    <details class="mb-2 w-full">
        <summary class="text-2xl bg-gray-200 p-4 rounded-lg cursor-pointer shadow-md mb-4 w-full">
            <span class="font-semibold">Government Aid and Policies</span>
        </summary>
        <div class="shadow-2xl bg-white w-full h-96 mx-auto my-8 p-6 rounded-lg flex items-start justify-left">
        <div className="bg-white w-full">
  <p className="text-black text-2xl font-bold">Put AI output here</p>
</div>
        </div>
    </details>
</div>

<div class="p-4 mx-auto w-full">
    <details class="mb-2 w-full">
        <summary class="text-2xl bg-gray-200 p-4 rounded-lg cursor-pointer shadow-md mb-4 w-full">
            <span class="font-semibold">Climate Shelters Nearby</span>
        </summary>
        <div class="shadow-2xl bg-white w-full h-96 mx-auto my-8 p-6 rounded-lg flex items-start justify-left">
        <div className="bg-white w-full">
  <p className="text-black text-2xl font-bold">Put AI output here</p>
</div>
        </div>
    </details>
</div>

<div class="p-4 mx-auto w-full">
    <details class="mb-2 w-full">
        <summary class="text-2xl bg-gray-200 p-4 rounded-lg cursor-pointer shadow-md mb-4 w-full">
            <span class="font-semibold">Recommended Areas for Relocation</span>
        </summary>
        <div class="shadow-2xl bg-white w-full h-96 mx-auto my-8 p-6 rounded-lg flex items-start justify-left">
        <div className="bg-white w-full">
  <p className="text-black text-2xl font-bold">Put AI output here</p>
</div>
        </div>
    </details>
</div>

<div class="p-4 mx-auto w-full">
    <details class="mb-2 w-full">
        <summary class="text-2xl bg-gray-200 p-4 rounded-lg cursor-pointer shadow-md mb-4 w-full">
            <span class="font-semibold">Nearby Essentials</span>
        </summary>
        <div class="shadow-2xl bg-white w-full h-96 mx-auto my-8 p-6 rounded-lg flex items-start justify-left">
        <div className="bg-white w-full">
        <p className="text-black text-2xl font-bold">
  <span className='font-light'>This will include food banks,
  gas stations, counselling services, and nearby ServiceCanada locations.</span></p>
  <p className='mb-20 text-black text-2xl font-bold'>
  Put AI output here
  </p>
</div>
        </div>
    </details>
</div>


<div class="p-4 mx-auto w-full">
    <details class="mb-2 w-full">
        <summary class="text-2xl bg-gray-200 p-4 rounded-lg cursor-pointer shadow-md mb-4 w-full">
            <span class="font-semibold">Emergency Contacts</span>
        </summary>
        <div class="shadow-2xl bg-white w-full h-96 mx-auto my-8 p-6 rounded-lg flex items-start justify-left">
        <div className="bg-white w-full">
  <p className="text-black text-2xl font-bold">
  Put AI output here</p>
</div>
        </div>
    </details>
</div>


        </section>

        <section id="moveto" className="min-h-screen">
          
        <h2 className="mt-5 text-2xl bg-white border border-black text-blue-900 font-semibold px-16 py-6 rounded-full hover:bg-blue-100 transition duration-300 text-center flex items-center justify-center">
          Thinking of Moving to this Area?
          <span className='ml-2'>
          <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#000000" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 9v11a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V9"/><path d="M9 22V12h6v10M2 10.6L12 2l10 8.6"/></svg>
          </span></h2>

          <div className="relative mt-10 bg-white w-11/12 h-screen flex flex-col items-center justify-center rounded-lg mx-auto">
  <p className="absolute top-0 left-0 m-4 text-black text-lg font-bold">
  <span className='font-light'>
        Here you will find the climate practices in your desired area, as well
        as if your area has been historically susceptible to climate disasters.
      </span>
       Put AI output here.
  </p>
</div>
        </section>

        <section id="furtherinfo" className="min-h-screen">
        <div className="flex justify-center items-center bg-blue-500 p-4">
      <Image
        src={compass}
        alt="Compass"
        width={100}
        height={100}
        className="bg-transparent"
      />
    </div>


        </section>
      </div>
    </div>
      
      
      
      </section>
      
      </>
  ) 
}

export default resources