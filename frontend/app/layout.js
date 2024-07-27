import { Inter } from "next/font/google";
import React from 'react';
import "./globals.css";
import Navbar from "@/components/Navbar";
import Footer from "@/components/Footer";

const inter = Inter({ subsets: ["latin"] });

export const metadata = {
  title: "ClimateCompass",
  description: "The all-in-one solution for climate migrants",
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body className={inter.className}>   
        <Navbar></Navbar> 
        {children}
      </body>
    </html>
  );
}
