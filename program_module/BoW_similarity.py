from sklearn.feature_extraction.text import CountVectorizer
bow_title_vectorizer = CountVectorizer()
bow_title_features = CountVectorizer().fit_transform(data['product_name'])
bow_title_features.get_shape()

def bag_of_words_model(doc_id, num_results):
    # doc_id: apparel's id in given corpus
    
    # pairwise_dist will store the distance from given input apparel to all remaining apparels
    # the metric we used here is cosine, the cosine distance is mesured as K(X, Y) = <X, Y> / (||X||*||Y||)
    # http://scikit-learn.org/stable/modules/metrics.html#cosine-similarity
    pairwise_dist = pairwise_distances(bow_title_features, bow_title_features[doc_id], metric='cosine', n_jobs=-1)
    
    # np.argsort will return `num_results` indices of the smallest distances
    indices = np.argsort(pairwise_dist.flatten())[0:num_results]
    #pdists will store the smallest distances
    pdists  = np.sort(pairwise_dist.flatten())[0:num_results]
    # np.argsort returns the indices of the smallest distances in ascending order.
    # The sort() method sorts the list ascending by default.

    #data frame indices of the 9 smallest distace's
    df_indices = list(data.index[indices])
    
    #displaying the results.
    for i in range(0, len(indices)):
        # we will pass 1. doc_id, 2. title1, 3. title2, 4. url, 5. model
        get_result(indices[i], data['product_name'].loc[df_indices[0]], 
                   data['product_name'].loc[df_indices[i]], 
                   data['image_urls__small'].loc[df_indices[i]], 'bag_of_words')
        
        print('ASIN :',data['asin'].loc[df_indices[i]])
        print ('Brand:', data['brand'].loc[df_indices[i]])
        print ('Title:', data['product_name'].loc[df_indices[i]])
        print ('Euclidean similarity with the query image :', pdists[i])
        print('='*80)


#call the bag-of-words model for a product to get similar products.
bag_of_words_model(12, 20) # change the index if you want to.
# In the output heat map each value represents the count value 
# of the label word, the color represents the intersection 
# with inputs title.
# 12 is the index of the "Query title"
#try 931  

















