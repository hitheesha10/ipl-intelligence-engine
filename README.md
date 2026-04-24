🏏 IPL Intelligence Engine

🔗 Live App: https://ipl-intelligence-engine.streamlit.app/

🚀 Overview

The IPL Intelligence Engine is an end-to-end cricket analytics and prediction system built using ball-by-ball IPL data (2008–2023).

It goes beyond traditional dashboards by combining:

📊 Data Analytics
🤖 Machine Learning
🎯 Match Strategy Insights
🎬 Interactive Match Storytelling

This project transforms raw cricket data into a decision-making system that explains and predicts match outcomes in real time.

🔥 Key Features
📈 Win Probability Engine
Predicts match outcome in real time
Ball-by-ball probability curve
Captures momentum shifts and turning points
🎯 Live Match Predictor
Input:
Runs required
Balls remaining
Wickets lost
Output:
Real-time win probability
⚔️ Player vs Player Comparison
Compare any two players across:
Total runs
Strike rate
Six-hitting ability
Identifies the better performer automatically
🎬 Smart Match Replay (WOW Feature)
Ball-by-ball replay system
AI-style commentary generation
Interactive match scrubbing (slider-based)
Displays:
Score progression
Events (4s, 6s, wickets)
Win probability changes
📊 Batting & Bowling Insights
Top performers by season
Phase-wise scoring analysis
Dot ball & wicket trends
🧠 Insight Engine
Automatically generates match insights like:
Dominant chasing trends
Defensive strength
Competitive match detection
🧬 Tech Stack
Python
Pandas / NumPy
Scikit-learn (ML model)
Matplotlib / Seaborn
Streamlit (interactive dashboard)
⚙️ Machine Learning
Model: Random Forest Classifier
Features used:
Runs to Get
Balls Remaining
Wickets Lost

👉 Used to predict chasing success probability

📁 Project Structure
ipl-intelligence-engine/
│
├── app.py
├── data/
│   └── ball_by_ball_ipl.csv
├── src/
│   ├── preprocess.py
│   ├── features.py
│   ├── model.py
│   └── utils.py
├── requirements.txt
└── README.md
▶️ Run Locally
# Clone repo
git clone https://github.com/yourusername/ipl-intelligence-engine.git

# Go to folder
cd ipl-intelligence-engine

# Activate virtual environment
source venv/bin/activate   # mac/linux
venv\Scripts\activate      # windows

# Install dependencies
pip install -r requirements.txt

# Run app
streamlit run app.py
🌍 Deployment

This project is deployed using Streamlit Cloud.

🔗 Live App:
https://ipl-intelligence-engine.streamlit.app/