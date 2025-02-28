from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    # Viral Video of the Week (static for Kai Cenat and Lil Rodney's Batman moment)
    viral_video_url = "https://youtube.com/shorts/jYQ3g4j1pqQ?si=4XYQDjDLzgBcctpa"
    
    # Static stream data for IShowSpeed
    stream_data = [
        {"title": "IShowSpeed’s WWE Royal Rumble 2025 Chaos", "video_id": "example_video_id_1"},
        {"title": "Match for Hope 2025 Soccer Madness with IShowSpeed", "video_id": "example_video_id_2"}
    ]

    return render_template('index.html', streams=stream_data, viral_video_url=viral_video_url)

@app.route('/streamers')
def streamers():
    # Reuse the same data for streamers as the home page
    viral_video_url = "https://youtube.com/shorts/jYQ3g4j1pqQ?si=4XYQDjDLzgBcctpa"
    stream_data = [
        {"title": "IShowSpeed’s WWE Royal Rumble 2025 Chaos", "video_id": "example_video_id_1"},
        {"title": "Match for Hope 2025 Soccer Madness with IShowSpeed", "video_id": "example_video_id_2"}
    ]
    return render_template('index.html', streams=stream_data, viral_video_url=viral_video_url)

@app.route('/podcasters')
def podcasters():
    return render_template('index.html')

@app.route('/music')
def music():
    return render_template('index.html')

@app.route('/families')
def families():
    return render_template('index.html')

@app.route('/political')
def political():
    return render_template('index.html')

@app.route('/viral')
def viral():
    return render_template('index.html')

if __name__ == '__main__':
    # For local development
    app.run(debug=True, host='0.0.0.0', port=8000)
else:
    # For production on Render
    app.run(host='0.0.0.0', port=8000)