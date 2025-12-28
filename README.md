# Currency Converter Web App

A **web-based currency converter** that allows users to convert between multiple currencies in real-time. The application fetches live exchange rates from a reliable API and performs accurate conversions, making it useful for travelers, online shoppers, and finance enthusiasts.

## Overview

This app provides a simple and **user-friendly interface** to convert currencies quickly. By leveraging live data from exchange rate APIs, it ensures that conversions reflect current market rates. Users can select the source and target currencies, input the amount, and get instant results.

## Key Features

* **Real-Time Conversion:** Fetches live exchange rates for accurate conversions.
* **Multiple Currencies Supported:** Convert between a wide range of global currencies.
* **User-Friendly Interface:** Simple web interface that works on both desktop and mobile browsers.
* **Quick and Responsive:** Instant conversion results without delay.

## How It Works

1. The user selects a **source currency** and a **target currency**.
2. The user enters the amount to convert.
3. The app queries a **live exchange rate API** and calculates the converted value.
4. The result is displayed immediately on the page.

## Tech Stack

* **Backend:** Python with Flask framework
* **API Integration:** REST API for fetching real-time currency exchange rates
* **Frontend:** HTML, CSS, Bootstrap for responsive design

## Installation and Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/mrjawadd/currencyConverter.git
   cd currencyConverter
   ```
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:

   ```bash
   python app.py
   ```
4. Open your browser and visit:

   ```
   http://127.0.0.1:5000
   ```
5. Select the currencies, enter the amount, and click **Convert** to see the result.

## Potential Improvements

* **Historical Trends:** Add graphs to visualize currency trends over time.
* **Multi-Language Support:** Allow users to switch between different languages.
* **Offline Mode:** Cache latest exchange rates to perform conversions when offline.
* **Enhanced UI:** Include charts, conversion history, and favorite currency pairs.

## Use Cases

* Travelers checking exchange rates before trips.
* Online shoppers dealing with international currencies.
* Finance students or enthusiasts analyzing real-time currency movements.

## GitHub

[Currency Converter](https://github.com/mrjawadd/currencyConverter)
