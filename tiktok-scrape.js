const TikTokScraper = require('tiktok-scraper');

async function scrapeHashtagVideos(hashtag) {
    try {
        const options = {
            number: 3, // number of videos you want to scrape
            download: true, // set to true if you want to download the videos
            filepath: './videos/', // location where the videos will be saved
            filetype: 'mp4', // format of the saved video
            proxy: '', // use a proxy if needed
        };

        const posts = await TikTokScraper.hashtag(hashtag, options);
        console.log(`Downloaded ${posts.collector.length} videos for hashtag #${hashtag}.`);
    } catch (error) {
        console.error(`Error scraping videos for hashtag #${hashtag}: ${error}`);
    }
}

// replace 'yourHashtagHere' with the desired hashtag
scrapeHashtagVideos('anime');
