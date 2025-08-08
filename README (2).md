# E‑Commerce Prediction

A data‑driven web app that leverages Linear Regression to forecast customer spending and sales trends by analyzing features like session time, pages viewed, and purchase history.

##  Project Overview

Predict customer spending patterns and sales trends using machine learning, enabling businesses to optimize marketing efforts and improve decision-making.

##  Repository Structure

```
├── Ecommerce Customers.csv     # Dataset
├── model_training.ipynb        # Data preprocessing, exploratory analysis, model training and validation
├── linear_model.joblib         # Trained Linear Regression model
├── app.py                      # Flask (or Streamlit) web application for live predictions
├── templates/                  # Front-end templates for the app
└── static/                     # Static assets (CSS, JS, images)
```

##  Features

- **Data Preprocessing**: Cleaning and preparing raw data for modeling.
- **Exploratory Data Analysis (EDA)**: Visual insights into spending patterns.
- **Model Training**: Training and tuning a Linear Regression model.
- **Evaluation**: Performance metrics like RMSE and R².
- **Interactive Web App**: Launch a UI to input new data and receive spending predictions in real time.

##  Installation & Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/Srinithimahalakshmi/Ecommerce_prediction.git
   cd Ecommerce_prediction
   ```

2. **Create a virtual environment & install dependencies**

   ```bash
   python3 -m venv venv
   source venv/bin/activate     # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Run model training (optional)**

   ```bash
   jupyter notebook model_training.ipynb
   ```

4. **Start the web application**

   ```bash
   python app.py
   ```

5. Open your browser and go to `http://localhost:5000` (or according to your app framework).

##  Usage

1. Enter customer session details like session duration, page views, etc.
2. Submit the form to receive a predicted spending value.
3. Use these insights to drive marketing strategies and business planning.

##  Dependencies

- Python 3.x
- pandas, numpy
- scikit-learn
- joblib
- Flask or Streamlit (depending on your front-end framework)
- Jupyter (for exploration and development)

##  License

Distributed under the MIT License — see the [LICENSE](LICENSE) file for full details.

##  Contact

Created by [Srinithimahalakshmi](https://github.com/Srinithimahalakshmi). Feel free to open issues or pull requests for improvements.
