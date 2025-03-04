import json
from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

def load_articles():
    with open('static/articles.json', 'r') as file:
        return json.load(file)

@app.route('/')
def home():
    viral_video_url = "https://youtube.com/shorts/jYQ3g4j1pqQ?si=4XYQDjDLzgBcctpa"
    stream_data = [
        {"title": "IShowSpeed’s WWE Royal Rumble 2025 Chaos", "video_id": "example_video_id_1"},
        {"title": "Match for Hope 2025 Soccer Madness with IShowSpeed", "video_id": "example_video_id_2"}
    ]
    articles = load_articles()
    articles['home'] = [
        {
            "title": "Streamers: IShowSpeed’s Super Bowl Stunt Goes Viral",
            "image": "sped1.jpg",
            "description": "IShowSpeed crashed Super Bowl LIX sidelines on February 9, 2025, trending with 10 million YouTube views and X buzz. Teens obsessed, adults stunned—watch now!",
            "link": "https://www.youtube.com/@IShowSpeed/streams",
            "added_time": "2025-03-03 18:00:00 PST"
        },
        {
            "title": "Families: LaBrant Fam’s New Baby Drama",
            "image": "lab.jpg",
            "description": "LaBrant Family’s February 2025 baby vlog hit 12 million YouTube views, sparking X gossip. Teens swoon, adults debate—check it out!",
            "link": "https://www.youtube.com/@TheLaBrantFam/videos",
            "added_time": "2025-03-03 18:01:00 PST"
        },
        {
            "title": "Political: YouTube Pundits Debate Mayor Adams’ Case",
            "image": "adam.jpg",
            "description": "YouTube stars debated Mayor Adams’ corruption case from February 26, 2025, with millions of views and X buzz. Teens pick sides, adults analyze—watch now!",
            "link": "https://www.youtube.com/results?search_query=mayor+adams+2025",
            "added_time": "2025-03-03 18:02:00 PST"
        },
        {
            "title": "Viral: Kai Cenat’s Batman Madness Hits 10M Views",
            "image": "kaiv.png",
            "description": "Kai Cenat’s February 2025 Batman skit on Twitch hit 10 million YouTube views, trending on X. Teens meme, adults laugh—pure viral gold!",
            "link": "https://youtube.com/shorts/jYQ3g4j1pqQ?si=4XYQDjDLzgBcctpa",
            "added_time": "2025-03-03 18:03:00 PST"
        }
    ]
    return render_template('index.html', streams=stream_data, viral_video_url=viral_video_url, articles=articles)

@app.route('/streamers')
def streamers():
    viral_video_url = "https://youtube.com/shorts/jYQ3g4j1pqQ?si=4XYQDjDLzgBcctpa"
    stream_data = [
        {"title": "IShowSpeed’s WWE Royal Rumble 2025 Chaos", "video_id": "https://youtube.com/shorts/PiU6dQrg4TY?si=srNZuspHY8d0cVeA"},
        {"title": "Match for Hope 2025 Soccer Madness with IShowSpeed", "video_id": "https://youtu.be/4YBYbXWl0-A?si=Gtg6uc3hz2P828Ihxample_video_id_2"}
    ]
    articles = load_articles()
    articles['streamers'] = [
        {
            "title": "IShowSpeed’s Wildest Stream Moments of 2025",
            "image": "sped1.jpg",
            "description": "IShowSpeed’s Super Bowl LIX stunt on February 9, 2025, trends on YouTube with 10 million views. His streams hit 30 million subs—teens rave, adults debate. Added on 2025-03-03 18:04:00 PST!",
            "link": "https://www.youtube.com/@IShowSpeed/streams",
            "latest_highlights": True
        },
        {
            "title": "Ninja’s 24-Hour Gaming Marathon Hits 8M Views",
            "image": "nij.jpg",
            "description": "Ninja’s March 3, 2025, 24-hour gaming marathon on YouTube hit 8 million views, trending on X. Teens cheer, adults debate burnout—watch now! Added on 2025-03-03 18:05:00 PST!",
            "link": "https://www.youtube.com/@ninja/videos",
            "latest_highlights": True
        }
    ]
    return render_template('index.html', streams=stream_data, viral_video_url=viral_video_url, articles=articles)

@app.route('/podcasters')
def podcasters():
    articles = load_articles()
    articles['podcasters'] = [
        {
            "title": "Joe Rogan’s AI Ethics Debate on YouTube Explodes",
            "image": "joe.jpg",
            "description": "Joe Rogan’s March 3, 2025, podcast on AI ethics hit 3 million YouTube views, sparking X buzz. Teens intrigued, adults question implications—watch now! Added on 2025-03-03 18:06:00 PST!",
            "link": "https://www.youtube.com/@joerogan/videos"
        },
        {
            "title": "PBD Podcast’s Biden Policy Analysis Goes Viral",
            "image": "bid.jpg",
            "description": "PBD Podcast’s March 3, 2025, debate on Biden’s policy shift hit 2 million YouTube views, trending on X. Teens pick sides, adults analyze—check it out! Added on 2025-03-03 18:07:00 PST!",
            "link": "https://www.youtube.com/@PBDPodcast/videos"
        }
    ]
    return render_template('index.html', articles=articles)

@app.route('/music')
def music():
    articles = load_articles()
    articles['music'] = [
        {
            "title": "Afrobeats Explosion: Tems’ New Hit Tops YouTube Charts",
            "image": "tem.jpg",
            "description": "Tems’ March 3, 2025, Afrobeats single hit 5 million YouTube views, trending on X. Teens dance, adults stream—watch now! Added on 2025-03-03 18:08:00 PST!",
            "link": "https://www.youtube.com/@temsbaby/videos"
        },
        {
            "title": "Taylor Swift’s Surprise Drop Shocks YouTube",
            "image": "tay.jpg",
            "description": "Taylor Swift’s March 3, 2025, surprise album drop hit 10 million YouTube views, trending on X. Teens obsess, adults praise—check it out! Added on 2025-03-03 18:09:00 PST!",
            "link": "https://www.youtube.com/@taylorswift/videos"
        }
    ]
    return render_template('index.html', articles=articles)

@app.route('/families')
def families():
    articles = load_articles()
    articles['families'] = [
        {
            "title": "LaBrant Fam’s Twin Announcement Shocks YouTube",
            "image": "lab.jpg",
            "description": "LaBrant Family’s March 3, 2025, twin announcement vlog hit 15 million YouTube views, sparking X gossip. Teens swoon, adults debate—watch now! Added on 2025-03-03 18:10:00 PST!",
            "link": "https://www.youtube.com/@TheLaBrantFam/videos"
        },
        {
            "title": "Kardashian Family Vlog Drama Hits 8M Views",
            "image": "kim.jpg",
            "description": "Kardashians’ March 3, 2025, YouTube vlog on family drama hit 8 million views, trending on X. Teens swoon, adults analyze—check it out! Added on 2025-03-03 18:11:00 PST!",
            "link": "https://www.youtube.com/@kardashians/videos"
        }
    ]
    return render_template('index.html', articles=articles)

@app.route('/political')
def political():
    articles = load_articles()
    articles['political'] = [
        {
            "title": "YouTube Pundits Debate Mayor Adams’ Case Update",
            "image": "adam.jpg",
            "description": "YouTube stars debated Mayor Adams’ March 3, 2025, case update, hitting 3 million views and X buzz. Teens pick sides, adults analyze—watch now! Added on 2025-03-03 18:12:00 PST!",
            "link": "https://www.youtube.com/results?search_query=mayor+adams+2025+update"
        },
        {
            "title": "Bolsonaro’s YouTube Rally Speech Sparks Global Debate",
            "image": "bols.jpg",
            "description": "Jair Bolsonaro’s March 3, 2025, YouTube rally speech hit 4 million views, trending on X. Teens intrigued, adults skeptical—check it out! Added on 2025-03-03 18:13:00 PST!",
            "link": "https://www.youtube.com/@jairbolsonaro/videos"
        }
    ]
    return render_template('index.html', articles=articles)

@app.route('/viral')
def viral():
    articles = load_articles()
    articles['viral'] = [
        {
            "title": "Kai Cenat’s Superhero Challenge Hits 12M YouTube Views",
            "image": "kai.jpg",
            "description": "Kai Cenat’s March 3, 2025, superhero challenge on YouTube hit 12 million views, trending on X. Teens meme, adults laugh—watch now! Added on 2025-03-03 18:14:00 PST!",
            "link": "https://www.youtube.com/@KaiCenat/videos"
        },
        {
            "title": "MrBeast’s $2M Survival Challenge Goes Viral",
            "image": "bearst.jpg",
            "description": "MrBeast’s March 3, 2025, $2M survival challenge hit 20 million YouTube views, sparking X buzz. Teens obsessed, adults amazed—check it out! Added on 2025-03-03 18:15:00 PST!",
            "link": "https://www.youtube.com/@MrBeast/videos"
        }
    ]
    return render_template('index.html', articles=articles)

@app.route('/health')
def health_check():
    return "OK", 200

if __name__ == '__main__':
    # For local development
    app.run(debug=True, host='0.0.0.0', port=8000)
else:
    # For production on Render
    app.run(host='0.0.0.0', port=8000)