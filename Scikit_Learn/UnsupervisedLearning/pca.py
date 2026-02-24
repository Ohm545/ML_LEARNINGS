import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

data = {
    'Age': [25, 30, 35, 40, 45, 50],
    'Income': [30000, 40000, 50000, 60000, 70000, 80000],
    'Spending': [70, 60, 50, 40, 30, 20],  
    'Savings': [1000, 5000, 8000, 10000, 15000, 20000]
}

df = pd.DataFrame(data)

# Step 1: Standardize the data
scaler = StandardScaler()
scaled_data = scaler.fit_transform(df)

# Step 2: Apply PCA (reduce to 2 principal components)
pca = PCA(n_components=2)
pca_result = pca.fit_transform(scaled_data)

# Print transformed data
print("PCA Result:")
print(pca_result)

# Check how much variance is explained
print("\nExplained Variance Ratio:")
print(pca.explained_variance_ratio_)

# See component directions
print("\nPrincipal Components:")
print(pca.components_)