import axios from "axios";

const url=`http://api.weatherapi.com/v1/current.json?key=209a73b018fa4fcb919191527240609&q=London&aqi=no`;

 async function getweather(){
    try{
        const response = await axios.get(url);
        console.log(response.data);
    }
    catch(error){
        console.error(error);
    }
}

getweather();