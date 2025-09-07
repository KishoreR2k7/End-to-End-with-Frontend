# 🌍 Life Expectancy Prediction  

This project provides an **end-to-end solution** for predicting life expectancy using **Random Forest Regression**. It includes data preprocessing, model training, evaluation, and a secure frontend with **Gradio-based login authentication** for users to interact with the model.  

## ✨ Key Features  
- 📊 **Regression Model** – Random Forest Regression for accurate predictions  
- 🔄 **Preprocessing Pipeline** – Missing value handling, scaling, encoding  
- 📈 **Evaluation Metrics** – R², RMSE, MAE  
- 💻 **Interactive Web App** – Built with Gradio, includes login page  
- 🔐 **User Authentication** – Secure access with username & password  

## 🔑 Demo Login Credentials  
- **Username:** `user`  
- **Password:** `123456`  

## 🌐 Live Application  


👉)  ## https://huggingface.co/spaces/KishoreR123/End-to-End1



## 📸 Screenshots  
### Login Page  


<img width="1919" height="777" alt="image" src="https://github.com/user-attachments/assets/6aebccab-e56f-4ae8-8c68-e959689f8f0b" />



### Prediction Page 


<img width="1883" height="906" alt="image" src="https://github.com/user-attachments/assets/320d9f06-f8f6-4ccc-9bad-136de7186c62" />


## 🛠️ Tech Stack  
- **Python** – Data preprocessing & modeling  
- **Scikit-learn** – Random Forest Regression  
- **Pandas / NumPy** – Data handling  
- **Gradio** – Web application & frontend  
- **Pickle / Joblib** – Model serialization  

## 📂 Project Structure  
├── data/ # Dataset
├── notebooks/ # Exploratory data analysis
├── model/ # Trained model + preprocessing pipeline
├── app/ # Gradio frontend (with login)
├── requirements.txt # Dependencies
├── README.md # Documentation

bash
Copy code

## ⚙️ Installation & Usage  
1. **Clone the repository**  
   ```bash
   git clone https://github.com/yourusername/life-expectancy-prediction.git
   cd life-expectancy-prediction
Install dependencies

bash
Copy code
pip install -r requirements.txt
Run the app

bash
Copy code
python app/app.py
Then open the local URL provided by Gradio.

📊 Model Performance
R² Score: 0.92

RMSE: 1.87

MAE: 1.25

yaml
Copy code
