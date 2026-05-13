# 🔥 Calories Burnt Prediction API

![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Production%20API-green)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue)
![Machine Learning](https://img.shields.io/badge/ML-Regression-orange)
![Status](https://img.shields.io/badge/Status-Ready%20for%20Deployment-success)

---

## 🚀 Project Overview

This is an end-to-end Machine Learning system that predicts calories burned during exercise using user activity and physiological data.

Pipeline:

Data Processing → Model Training → Model Saving → FastAPI Deployment → Docker Containerization

---

## 🧠 System Architecture

Client (Postman / Web / Mobile App)  
↓  
FastAPI Server (app/main.py)  
↓  
Input Validation (Pydantic)  
↓  
Feature Processing (Pandas)  
↓  
Trained ML Model (CatBoost / XGBoost / RandomForest)  
↓  
Prediction Output  
↓  
JSON Response  

---

## 📊 Input Features

- Gender  
- Age  
- Height  
- Weight  
- Duration (minutes)  
- Heart Rate  
- Body Temperature  

---

## 🏗️ Tech Stack

- Python  
- FastAPI  
- Scikit-learn / CatBoost / XGBoost  
- Pandas, NumPy  
- Uvicorn  
- Docker  
- Joblib  

---

## 📁 Project Structure
```text
Calories_burnt/
│
├── app/
│   ├── main.py
│
├── model.pkl
├── notebooks/
│   ├── calories_burnt_prediction.ipynb
├── requirements.txt
├── Dockerfile
├── LICENSE
├── .gitignore
└── README.md
```

---

## ⚙️ How It Works

1. User sends JSON input to API  
2. FastAPI validates input  
3. Data is converted into DataFrame  
4. Preprocessing is applied (if needed)  
5. ML model generates prediction  
6. Response is returned as JSON  

---

## 🚀 Run Locally

### 1. Clone Repository

git clone https://github.com/rafsun-jany-rafy/calorie-predictor-api.git  
cd calories-predictor-api  

---

### 2. Install Dependencies

pip install -r requirements.txt  

---

### 3. Run API

uvicorn app.main:app --reload  

---

### 4. Open Swagger UI

http://127.0.0.1:8000/docs  

---

## 🐳 Run with Docker

### Build Image

docker build -t calorie-api .

### Run Container

docker run -p 8000:8000 calorie-api  

---

## 📡 API Endpoints

### GET /

Response:
{
  "message": "Calories Prediction API is running"
}

---

### POST /predict

Request:
{
  "Gender": 0,
  "Age": 25,
  "Height": 175,
  "Weight": 70,
  "Duration": 30,
  "Heart_Rate": 110,
  "Body_Temp": 40
}

Response:
{
  "predicted_calories": 231.5
}

---

## 📊 Model Details

- Regression problem  
- Models tested: Random Forest, XGBoost, CatBoost  
- Best model: CatBoost  
- Evaluation: RMSE, R² Score  
- Saved using joblib  

---

## 🌐 Deployment

This project is deployed in Render[https://calorie-predictor-api.onrender.com/docs]

This project can be deployed later on:
  
- Railway  
- AWS EC2  
 

---

## 🚀 Future Improvements

- Add authentication (JWT)  
- Add logging system  
- Add CI/CD pipeline  
- Add frontend UI (React / Streamlit)  
- Add model monitoring  

---

## 👨‍💻 Author

Machine Learning Engineering project focused on production-ready deployment and real-world ML systems.

---

## 📜 License

This project is licensed under the MIT License.

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub.