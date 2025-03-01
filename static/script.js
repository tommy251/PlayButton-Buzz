// script.js for PlayButtonBuzz - Streamers Section
document.addEventListener('DOMContentLoaded', () => {
    const streamersSection = document.getElementById('streamers');
    const apiKey = 'YOUR_YOUTUBE_API_KEY'; // Replace with your actual YouTube Data API key
    const channelId = 'UCJsC7GGpX6A0nfu2eTfEy0w'; // IShowSpeed's channel ID
    const apiUrl = `https://www.googleapis.com/youtube/v3/search?part=snippet&channelId=${channelId}&type=video&eventType=live&maxResults=5&key=${apiKey}`;

    // Function to fetch and display IShowSpeed's latest streams
    async function fetchStreams() {
        try {
            const response = await fetch(apiUrl);
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            const data = await response.json();
            const streams = data.items || [];

            if (streams.length > 0) {
                let streamHtml = '<h2 class="section-title">IShowSpeed’s Latest Stream Highlights</h2><ul class="stream-list">';
                streams.forEach(stream => {
                    const title = stream.snippet.title;
                    const videoId = stream.id.videoId;
                    const thumbnail = stream.snippet.thumbnails.medium.url;
                    streamHtml += `
                        <li class="stream-item">
                            <a href="https://www.youtube.com/watch?v=${videoId}" target="_blank" class="stream-link">
                                <img src="${thumbnail}" alt="${title}" class="post-image">
                                <span class="stream-title">${title}</span>
                            </a>
                        </li>`;
                });
                streamHtml += '</ul>';
                streamersSection.innerHTML = streamHtml;
            } else {
                streamersSection.innerHTML = '<p class="no-streams">No live streams available right now—check back soon.</p>';
            }
        } catch (error) {
            console.error('Error fetching streams:', error);
            streamersSection.innerHTML = '<p class="no-streams">Oops! Couldn’t load the latest streams—try again later or visit <a href="https://www.youtube.com/@IShowSpeed/streams" target="_blank" class="stream-link">IShowSpeed’s streams</a>.</p>';
        }
    }

    // Fetch streams when the page loads
    fetchStreams();
});