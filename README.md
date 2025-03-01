# Apparel-Recommendation-based-on-Content-Based-Clustering-System

## **1. Introduction**
Recommender systems play a crucial role in enhancing user experience on e-commerce platforms by suggesting relevant products. This project focuses on building a **Content-Based Clustering Recommendation System** that groups similar products using **Pairwise Cosine Distances**.

The system will analyze product features such as:
- **Title of the product**
- **Brand of the product**
- **Color of the product**
- **Type of the product**
- **Image of the apparel**

Using this information, it will recommend similar products to a given input product.

---
## **2. Problem Statement**
The objective is to build a **recommendation engine** that suggests similar products on e-commerce platforms such as Amazon, Myntra, and Flipkart. Given a large dataset of **1,80,000 products**, we aim to identify similar products using **content-based filtering** and **clustering techniques**.

---
## **3. Methodology**
The project consists of several steps:

### **3.1 Data Preprocessing**
- Cleaning the dataset to remove missing values.
- Converting categorical features into numerical representations.
- Extracting text-based features using **TF-IDF (Term Frequency-Inverse Document Frequency)**.
- Extracting image features using **Convolutional Neural Networks (CNNs)**.

### **3.2 Feature Extraction**
We extract the following feature types:
1. **Text Features**: Using **TF-IDF Vectorization** for product titles and descriptions.
2. **Numerical Features**: Encoding categorical data such as brand, color, and product type.
3. **Image Features**: Using a **pretrained CNN model (ResNet-50)** to extract embeddings from apparel images.

### **3.3 Similarity Computation**
To find similar products, we compute the **Pairwise Cosine Similarity** between product feature vectors.

#### **Cosine Similarity Formula:**
\[
\text{Similarity}(A, B) = \frac{A \cdot B}{||A|| ||B||}
\]
Where:
- **A and B** are the feature vectors of two products.
- **Numerator** represents the dot product of the vectors.
- **Denominator** is the product of their magnitudes.

### **3.4 Clustering Similar Products**
We use **K-Means Clustering** to group similar items together. Steps involved:
1. Compute **cosine similarity** between all product vectors.
2. Apply **K-Means clustering** to group similar items.
3. Assign a cluster label to each product.
4. Given an input product, find its cluster and recommend other products within the same cluster.

### **3.5 Building the Recommendation Engine**
The final step involves creating a function that:
1. Accepts a **product ID** as input.
2. Finds the cluster to which it belongs.
3. Suggests **top-N similar products** from the same cluster.
4. Displays a heatmap to show feature similarity.

---
## **4. Technologies Used**
- **Python** (pandas, numpy, scikit-learn, matplotlib, seaborn)
- **NLP Techniques** (TF-IDF, Cosine Similarity)
- **Machine Learning Algorithms** (K-Means Clustering)
- **Deep Learning** (CNNs for image feature extraction)

---
## **5. Comparison with Other Recommendation Methods**

| **Method** | **Description** | **Advantages** | **Disadvantages** |
|------------|----------------|----------------|--------------------|
| **Collaborative Filtering** | Uses user interactions (ratings, views) | No need for detailed product info | Cold start problem for new products |
| **Content-Based Filtering** | Uses product attributes (title, brand, color, etc.) | Works well for new products | Requires feature engineering |
| **Hybrid Filtering** | Combines collaborative & content-based filtering | More accurate | Computationally expensive |
| **Clustering-Based (Our Approach)** | Groups similar products based on content | Efficient for large datasets | Needs good feature extraction |

---
## **6. Conclusion**
This **Content-Based Clustering Recommendation System** efficiently finds and suggests similar products using **Cosine Similarity & K-Means Clustering**. The system is scalable and works well for large datasets. Future improvements can include:
- Enhancing the **image similarity** using **Siamese Networks**.
- Implementing a **hybrid approach** combining collaborative filtering.
- Deploying the model as an API for real-world applications.

---
## **7. References**
- https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html
- https://www.tensorflow.org/tutorials/images/cnn

---
## **8. How to Run the Project**
1. Install dependencies:
   ```sh
   pip install numpy pandas scikit-learn tensorflow matplotlib seaborn
   ```
2. Load the dataset and preprocess it.
3. Run the `recommendation_engine.py` script to get recommendations.
4. View results in the heatmap visualization.

---
### **Contributors**
- **Abhishek Sharma**

