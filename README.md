🌲 Forest Fire Prediction (FWI)

A machine learning project to predict the Fire Weather Index (FWI) using the Algerian Forest Fire Dataset.
The model is built with Ridge Regression and deployed using Flask for real-time predictions.

📊 Dataset

Source: UCI Algerian Forest Fire Dataset

Features: Temp, RH, Wind, Rain, Fire Weather Codes (FFMC, DMC, DC, ISI)

Target: FWI

⚙️ Installation
git clone https://github.com/Arjun-Mishra-29/Test-Forest-Fire-Analysis.git
cd Test-Forest-Fire-Analysis
pip install -r requirements.txt
python app.py


Then open http://127.0.0.1:5000/ in your browser.

📂 Project Structure
├── app.py          # Flask app
├── model.pkl       # Trained Ridge Regression model
├── templates/      # HTML files
├── data/           # Dataset
└── requirements.txt

📈 Results

Ridge Regression achieved good prediction accuracy

Example: R² ≈ 0.98, MAE ≈ 0.564

🚀 Future Work

Add more ML models

Integrate real-time weather API

✨ Developed by Arjun Mishra
