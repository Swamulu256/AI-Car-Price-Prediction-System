🚗 AI Car Price Prediction System
Live Demo

An end-to-end machine learning web application that predicts the resale price of used cars based on historical data and market-driven features. The system combines a robust ML pipeline with a production-grade Flask backend and an enterprise-style UI designed for real-world usability and interviews.

🔍 Project Overview
Estimating the resale value of used cars is a common real-world problem influenced by multiple factors such as car age, mileage, fuel type, ownership history, brand value, and transmission type.

This project solves that problem using supervised machine learning regression, enhanced with:

Feature scaling
Target encoding for high-cardinality categorical features
Post-prediction constraints to enforce real-world realism
A modern, interactive web interface
✨ Key Features
🎥 Auto-Demo Mode One-click automated demo that generates realistic, randomized inputs within safe feature ranges and instantly predicts results — ideal for interviews and quick showcases.

📊 Prediction Confidence Score A heuristic-based confidence percentage calculated from prediction deviation and feature stability, providing transparency to users.

🎨 Enterprise Dark UI Modern, responsive, recruiter-friendly interface with animations and clear visual hierarchy.

🧠 Production-Safe ML Output Post-processing logic prevents negative or unrealistic price predictions, mimicking real-world ML deployment practices.

🧠 Machine Learning Pipeline
Data Preprocessing

Handling numerical and categorical features
Normalization using StandardScaler
Brand feature encoded using Target Encoding
Model Training

Regression-based model trained on historical car resale data
Optimized for generalization across brands and price ranges
Post-Prediction Processing

Prediction clamping to realistic value ranges
Confidence estimation after correction
🛠️ Tech Stack
Programming Language: Python
Backend: Flask
Machine Learning: Scikit-learn
Data Processing: Pandas, NumPy
Model Persistence: Joblib
Frontend: HTML, CSS (Custom Dark UI)
📁 Project Structure
ai-car-price-prediction-system/
│
├── app.py
├── reg_model.pkl
├── scaler.pkl
├── target_encode.pkl
│
├── templates/
│   └── index.html
│
└── static/
    └── styles.css
🚀 How to Run Locally
1️⃣ Clone the Repository
git clone https://github.com/amareshtoxico/ai-car-price-prediction-system.git
cd ai-car-price-prediction-system
2️⃣ Create & Activate Virtual Environment
python -m venv .venv
.venv\Scripts\activate   # Windows
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Run the Application
python app.py
5️⃣ Open in Browser
http://127.0.0.1:5000/
🎥 Auto-Demo Mode (Interview Tip)
Click “🎥 Run Auto Demo” to:

Auto-fill the form with realistic values
Submit automatically
Instantly display prediction + confidence
Perfect for live demos without manual input.

📌 Why This Project Stands Out
Realistic ML deployment considerations (output constraints)
Clean separation of ML, backend, and frontend
Interview-ready demo functionality
Scalable architecture for future enhancements
📈 Future Enhancements
Feature importance visualization (SHAP)
Model performance dashboard
User authentication
Cloud deployment with CI/CD
REST API for external consumption


<h1 align="center">🚗 AI Car Price Prediction System</h1>

<p align="center">
  A Machine Learning based web application that predicts car prices using key features such as brand, year, mileage, fuel type, and transmission.
</p>

<hr>

<h2> Project Overview</h2>
<p>
This project uses Machine Learning algorithms to estimate the resale price of a car.
It helps users make data-driven decisions while buying or selling used cars.
</p>

<h2> Features</h2>
<ul>
  <li>Predicts car prices instantly</li>
  <li>User-friendly web interface</li>
  <li>Trained ML regression model</li>
  <li>Fast and accurate predictions</li>
</ul>

<h2>🛠️ Technologies Used</h2>
<ul>
  <li><b>Frontend:</b> HTML, CSS, JavaScript</li>
  <li><b>Backend:</b> Python (Flask)</li>
  <li><b>Machine Learning:</b> Scikit-learn</li>
  <li><b>Libraries:</b> NumPy, Pandas</li>
</ul>

<h2> Project Structure</h2>
<pre>
AI-Car-Price-Prediction-System
│
├── app.py
├── reg_model.pkl
├── car_data.csv
├── templates/
│   └── index.html
├── static/
│   └── style.css
├── requirements.txt
└── README.md
</pre>

<h2>⚙️ How It Works</h2>
<ol>
  <li>User enters car details</li>
  <li>Data is sent to the ML model</li>
  <li>Model predicts the price</li>
  <li>Result is displayed on the web page</li>
</ol>

<h2> Installation & Usage</h2>
<pre>
pip install -r requirements.txt
python app.py
</pre>

<p>
Open your browser and go to:
<b>http://127.0.0.1:5000</b>
</p>

<h2> Machine Learning Model</h2>
<ul>
  <li>Regression-based model</li>
  <li>Trained on real car price data</li>
  <li>Handles missing values and feature encoding</li>
</ul>

<h2> Future Enhancements</h2>
<ul>
  <li>Add more car features</li>
  <li>Improve prediction accuracy</li>
  <li>Deploy using cloud platforms</li>
</ul>

<h2> Contributing</h2>
<p>
Contributions are welcome! Feel free to fork this repository and submit pull requests.
</p>

<h2> License</h2>
<p>
This project is licensed under the MIT License.
</p>

<hr>

<p align="center">
  ⭐ If you like this project, give it a star on GitHub!
</p>



📜 License

T
