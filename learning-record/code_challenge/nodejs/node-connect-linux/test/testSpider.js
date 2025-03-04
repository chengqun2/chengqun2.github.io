const axios = require("axios");
const cheerio = require("cheerio");
const pretty = require("pretty");

async function getTitle(url) {
    try {
        // Fetch the HTML from the URL
        const { data } = await axios.get(url);
        // Load the HTML into cheerio
        const $ = cheerio.load(data);
        console.log(pretty($.html()));
        // Extract the title
        const title = $('title').text();
        return title;
    } catch (error) {
        console.error('Error fetching the title:', error);
        return null;
    }
}
// Example usage
getTitle('https://www.freecodecamp.org/news/how-to-scrape-websites-with-node-js-and-cheerio/').then(title => {
    console.log('Page title:', title);
});
