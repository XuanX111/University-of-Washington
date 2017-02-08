## include more features on the house prices assignment

import graphlab
graphlab.product_key.set_product_key('XXX')

#question 1 find the mean value of the house in the area 98039

zip_subset = sales[sales['zipcode']=='98039'] # defind a subset under sales
zip_subset.show() #show the data general information


price2 = zip_subset['price'].mean()
print price2 # which is 2160606.6

# filtering data
sqft_living2 = sales[(sales['sqft_living']>=2000) & (sales['sqft_living']<=4000)]
sqft_living2.count

print len(sqft_living2)

import numpy as N
[r,c] = N.shape(sales) #compute the row column number
print r,c

temp = len(sqft_living2)/float(r)
print temp   #percentage 0.43

# create regression analysis
advanced_features = ['bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'floors', 'zipcode', 'condition','grade', 'waterfront','view', 'sqft_above', 'sqft_basement','yr_built', 'yr_renovated','sqft_living15', 'sqft_lot15']
train_data2,test_data2 = sales.random_split(.8,seed=0)

advanced_features_model = graphlab.linear_regression.create(train_data2,target='price',features=advanced_features,validation_set=None)
my_features_model1 = graphlab.linear_regression.create(train_data2,target='price',features=my_features,validation_set=None)

print advanced_features_model.evaluate(test_data2)
print my_features_model1.evaluate(test_data2)

#{'max_error': 3557371.7401880627, 'rmse': 156853.93496525375}
#{'max_error': 3486584.509381705, 'rmse': 179542.4333126903}
# lower than 22689

print my_features_model.predict(house2)
