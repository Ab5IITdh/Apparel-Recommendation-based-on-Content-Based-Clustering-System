import pandas as pd

data = pd.read_json('C:\\Users\\Abhishek Sharma\\Apparel Reccomadation System\\sample_for_amazon_30k_data.ldjson', lines =True) 

print('Number of data points : ', data.shape[0])
print() 
print('Number of features/variables:', data.shape[1]) 

data.columns # prints column-names or feature-names.

data = data[['asin', 'brand', 'colour', 'image_urls__small', 'product_name', 'rating', 'sales_price', 'product_details__k_v_pairs']] 

print('Number of data points : ', data.shape[0])
print()
print('Number of features:', data.shape[1])
print() 
data.head() # prints the top rows in the table.

print(data['product_details__k_v_pairs'].describe()) 
print(data['product_name'].describe()) 
# names of different product types
print(data['product_name'].unique()) 

from collections import Counter

# find the 10 most frequent product_type_names.
product_type_count = Counter(list(data['product_name']))
product_type_count.most_common(10) 

print(data['brand'].describe())
# find the 10 most frequent brand.
brand_count = Counter(list(data['brand']))
brand_count.most_common(10)

print(data['colour'].describe())
# find the 10 most frequent color.
color_count = Counter(list(data['colour']))
color_count.most_common(10) 

print(data['sales_price'].describe()) 
price_count = Counter(list(data['sales_price']))
price_count.most_common(10) 


print(data['product_name'].describe()) 

data.isnull().sum() 
