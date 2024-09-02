// import Twitter from 'twitter-lite';

// const client = new Twitter({
//   consumer_key: process.env.TWITTER_CONSUMER_KEY,
//   consumer_secret: process.env.TWITTER_CONSUMER_SECRET,
//   access_token_key: process.env.TWITTER_ACCESS_TOKEN_KEY,
//   access_token_secret: process.env.TWITTER_ACCESS_TOKEN_SECRET,
// });

// export const fetchTweets = async (keyword, count = 10) => {
//   try {
//     const tweets = await client.get('search/tweets', {
//       q: keyword,
//       count: count,
//     });
//     return tweets.statuses;
//   } catch (error) {
//     console.error('Error fetching tweets:', error);
//     throw error;
//   }
// };



import fetch from 'node-fetch';

const fetchEarthquakeData = async () => {
  const url = 'https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2024-08-01&endtime=2024-08-26&minmagnitude=4';

  try {
    const response = await fetch(url);
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    const data = await response.json();
    console.log(data);
  } catch (error) {
    console.error('Error fetching earthquake data:', error);
  }
};

fetchEarthquakeData();
