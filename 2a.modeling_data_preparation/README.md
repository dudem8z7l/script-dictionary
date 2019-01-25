For optimal result, the order for performing these code will as followed:
1. Convert all categorical variables to 'categorical' type
2. Perform 'inverse_transform_cat_dict.py' to extract dictionary to transform and inverse transform categorical variables
3. Perform 'train_test_split_and_scaled_num_col.py' to perform train test split and scaled numerical columns
4. Perform 'convert_cat2num.py' to convert categorical variables to numerical variables using the result from the previous step
