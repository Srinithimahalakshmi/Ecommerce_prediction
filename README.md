
#  E-commerce Spending Predictor (Linear Regression)

##  Overview
This project predicts customer spending and sales trends using **Linear Regression**, based on features like session duration, pages viewed, and purchase history. The pipeline includes data preprocessing, exploratory analysis, model training, evaluation, and a simple web interface for prediction.

---

##  Table of Contents
- [⚙️ Installation](#-installation)  
- [🚀 Usage](#-usage)  
- [📁 Project Structure](#-project-structure)  
- [📊 Results](#-results)  
- [🤝 Contributing](#-contributing)  
- [📬 Contact](#-contact)  

---

##  Installation
```bash
git clone https://github.com/Srinithimahalakshmi/Ecommerce_prediction.git
cd Ecommerce_prediction

python3 -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
pip install -r requirements.txt
````

---

## Usage

### 1. Train & Evaluate the Model

Open the notebook for a step-by-step journey through data processing and model building:

```bash
jupyter notebook model_training.ipynb
```

Train and save the model using provided scripts or within the notebook workflow.

### 2. Launch the Web App

Start the interactive interface for real-time predictions:

```bash
python app.py
```

Navigate to **[http://127.0.0.1:5000](http://127.0.0.1:5000)**, enter session details, and view estimated customer spending predictions!

---

## Project Structure

```
Ecommerce_prediction/
├── Ecommerce Customers.csv       # Raw customer session data
├── model_training.ipynb          # Notebook for analysis and model training
├── linear_model.joblib           # Saved Linear Regression model
├── app.py                        # Flask app for prediction interface
├── templates/
│   └── index.html                # HTML template
├── static/
│   └── [CSS & JS assets]         # Web interface resources
├── requirements.txt              # Project dependencies
└── README.md                     # This documentation
```

---

## Results

* **Model Performance**: Include metrics like R², MAE, MSE, and RMSE here.
* Visual outputs such as **scatter plots**, **residual plots**, or **feature importance** (if available) should be embedded or linked within the notebook/results folder for better context.

---

## Contributing

Contributions are welcome! Ways you can help:

* Improve preprocessing or feature engineering
* Explore alternative regression models (e.g., Ridge, Lasso, XGBoost)
* Add more visualization for performance insights
* Enhance the web UI with input validation or responsive design

**To contribute:**

1. Fork this repository
2. Branch off: `git checkout -b feature/YourFeature`
3. Commit changes: `git commit -m "Add feature XYZ"`
4. Push & create a Pull Request

---

## Contact

👤 **Maintainer**: Srinithi Mahalakshmi
📧 **Email**: [srinithiarumugam2003@gmail.com](mailto:srinithiarumugam2003@gmail.com)
🔗 **GitHub**: [Srinithimahalakshmi](https://github.com/Srinithimahalakshmi)

---

⭐ *If you find this project valuable, a star on GitHub would mean a lot!*
