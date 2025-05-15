# 🛍️ Customer Analytics & Machine Learning Design System for E-commerce (Olist Dataset)

This project is an end-to-end data science and engineering solution using the [Olist Brazilian E-commerce Dataset](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce). It includes machine learning tasks and design a full pipeline from raw data ingestion to machine learning models and system deployment.

---

## 📂 Datasets 

Data source:
- [Olist Brazilian E-commerce Dataset](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)
- [Seller Marketing Funnel by Olist](https://www.kaggle.com/datasets/olistbr/marketing-funnel-olist)


Data Schema:

![Alt text](/image/data_schema.png)
---

## 🧪 Machine Learning Tasks

### 1. 💰 Customer Segmentation based on Life Time Value 
- **Goal**: Customer Segmenation based on user Life Time Value (LTV)
- **Features**: historical recency (last active), frequency, and revenue
- **Model**: KMeans
- **Metrics**: 

### 2. 💰 Customer Lifetime Value Prediction
- **Goal**: Estimate future total value a customer will bring
- **Features**: historical purchase amount, frequency, user recency
- **Model**: KNN, Logistic Regression, Random Forest, Gradient Boosting, XGBoost
- **Metrics**: 

---
## 🧱 Machine Learning Design System

![Alt text](/image/architecture_overview.png)
---
## 🔧 Tech Stack

- **Languages**: Python 3.x
- **ML Frameworks**: scikit-learn
- **Data Processing**: pandas, numpy
- **Visualization**: seaborn, matplotlib, plotly
- **Database**: Postgres
- **Pipeline & Scheduling**: Airflow / Spark
- **Environment**: Docker

---

## ⚙️ How to Run

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/ecommerce-customer-analytics.git
cd ecommerce-customer-analytics






