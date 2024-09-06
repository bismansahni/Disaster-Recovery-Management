// import axios from "axios";

// const url=`http://api.weatherapi.com/v1/current.json?key=209a73b018fa4fcb919191527240609&q=85281&aqi=no`;

//  async function getweather(){
//     try{
//         const response = await axios.get(url);
//         console.log(response.data);
//     }
//     catch(error){
//         console.error(error);
//     }
// }

// getweather();



import axios from 'axios';
import { writeFileSync } from 'fs';

const place="Delhi"

const url = `http://api.weatherapi.com/v1/current.json?key=209a73b018fa4fcb919191527240609&q=${place}&aqi=no`;

const getWeather = async () => {
    try {
        const response = await axios.get(url);
        const weatherData = response.data;

        // Save the response to a JSON file
        writeFileSync('weather_data.json', JSON.stringify(weatherData, null, 2));
        console.log('Weather data saved to weather_data.json');
    } catch (error) {
        console.error('Error fetching weather data:', error);
    }
};

getWeather();
