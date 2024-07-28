
import '../app/globals.css'
import React from 'react'

const resources = () => {
  return (
    <>
 <section style={{ background: '#E6E6E6' }}>

<div className="w-full h-10 bg-green-Figma border-2 rounded-md my-4 p-2 flex items-center justify-center">
  <p className="text-center font-extrabold text-2xl text-white">
    Climate Compass: Results for ____
  </p>
</div>

      
<div className="w-full bg-green-Figma border-2 rounded-md my-4 p-2 flex items-center justify-center">
  <p className="text-center text-white text-xl">
    Here, you will find the most <span className='font-extrabold'> essential</span> climate details
    about your specified location. 
  </p>
</div>

<div className="relative">
      <nav className=" bg-green-Figma text-white p-4 rounded-md shadow-lg">
        <p className="flex space-x-5 items-center justify-center">
          <span className='font-mono'> Redirect to: </span>
          <a href="#climatemap" className="hover:underline font-mono flex items-center justify-center f">Climate Map</a>
          <a href="#migration" className="hover:underline font-mono flex items-center justify-center">Climate Migration Services</a>
          <a href="#moveto" className="hover:underline font-mono flex items-center justify-center">Thinking of moving to this area?</a>
          <a href="#furtherinfo" className="hover:underline font-mono flex items-center justify-center">Further Info</a>
        </p>
      </nav>

      <div className="mt-10">
        <section id="climatemap" className="min-h-screen">
          <h2 className="text-2xl font-bold flex items-center justify-center">Climate Map</h2>
          <div className="bg-gray-50 w-full h-96 mx-auto my-8 p-6 rounded-lg shadow-lg flex items-center justify-center">
  <p className="text-white text-2xl font-bold">The Map goes here</p>
</div>
        </section>
        
        <section id="migration" className="min-h-screen">
        <h2 className="text-2xl font-bold flex items-center justify-center">Climate Migration Services</h2>

<div className="bg-gray-50 w-full h-96 mx-auto my-8 p-6 rounded-lg shadow-lg flex items-start justify-left">
  <p className="text-white text-2xl font-bold">Government Aid and Policies:</p>
</div>
<div className="bg-gray-50 w-full h-96 mx-auto my-8 p-6 rounded-lg shadow-lg flex items-start justify-left">
  <p className="text-white text-2xl font-bold">Climate Shelters Nearby:</p>
</div>
<div className="bg-gray-50 w-full h-96 mx-auto my-8 p-6 rounded-lg shadow-lg flex items-start justify-left">
  <p className="text-white text-2xl font-bold">Recommended Areas for Relocation:</p>
</div>
<div className="bg-gray-50 w-full h-96 mx-auto my-8 p-6 rounded-lg shadow-lg flex items-start justify-left">
  <p className="text-white text-2xl font-bold">Nearby Essentials: <span className='font-light'>This will include food banks,
    gas stations, counselling services, and nearby ServiceCanada locations.</span></p>
</div>

<div className="bg-gray-50 w-full h-96 mx-auto my-8 p-6 rounded-lg shadow-lg flex items-start justify-left">
  <p className="text-white text-2xl font-bold">Emergency Contacts:</p>
  
</div>
        </section>

        <section id="moveto" className="min-h-screen">
        <h2 className="text-2xl font-bold flex items-center justify-center">Thinking of Moving to this area?</h2>
        <div className="bg-gray-50 w-full h-96 mx-auto my-8 p-6 rounded-lg shadow-lg flex items-start justify-left">
  <p className="text-white text-2xl font-bold">Here you will find the climate practices in your desired area, as well
    as if your area has been historically susceptible to climate disasters.</p>
  
</div>
        </section>

        <section id="furtherinfo" className="min-h-screen">
        <h2 className="text-2xl font-bold flex items-center justify-center">Further</h2>
          <p>Content for section 4...</p>
        </section>
      </div>
    </div>
      
      
      
      </section>
      
      </>
  ) 
}

export default resources