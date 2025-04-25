# Collaborative_Filtering_System-
## 📌 Project Description

Collaborative Filtering is a widely-used recommendation technique that relies on user-item interaction data. This project includes:

- User-Based Collaborative Filtering
- Item-Based Collaborative Filtering
- Model Evaluation with RMSE, Precision@K, and Recall@K
- Generating Top-N Recommendations
- Visualizations (optional)

The dataset used is the **MovieLens 100K**, containing 100,000 ratings from 943 users on 1,682 movies.

🚀 Usage Instructions
▶️ Run in Jupyter Notebook
Navigate to the notebooks/ folder and open the notebooks in order:

01_data_preprocessing.ipynb: Load and clean the dataset

02_user_based_cf.ipynb: Implement user-based CF

03_item_based_cf.ipynb: Implement item-based CF

04_evaluation_and_visualization.ipynb: Evaluate and visualize results

📁 Project Structure

collaborative-filtering-recommender/
├── README.md
├── requirements.txt
├── data/
│   ├── u.data
│   ├── u.item
│   └── u.user
├── notebooks/
│   ├── 01_data_preprocessing.ipynb
│   ├── 02_user_based_cf.ipynb
│   ├── 03_item_based_cf.ipynb
│   └── 04_evaluation_and_visualization.ipynb
├── results/
│   ├── top_n_recommendations.csv
│   └── evaluation_metrics.json
├── src/
│   ├── __init__.py
│   ├── data_loader.py
│   ├── recommender.py
│   └── evaluation.py

