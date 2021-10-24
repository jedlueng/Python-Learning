import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics


#### Supervised learning
# Learning from existing data, to predict unknowns in the future


# # Inputs
# height = [170, 165, 125, 180, 65]
# ages = [65, 55,44,34,55]

# # Outputs
# bmi = [23,24,21,26,27]

### Regression: Continous Outputs
### Classification: 1, 0

################################


# 1. read data and inspect
data = pd.read_csv('StudentsPerformance.csv')


# Given a math score, what is the likely reading score?
# Linear Regression -> Ordinary least Squares


#### 2. Split data into X and y

# Reshaping data into a vertical column
X = data['math score'].values.reshape(-1, 1)
y = data['reading score'].values.reshape(-1, 1)


### 3. Split into Training and Testing

X_train, X_test, y_train, y_test = train_test_split(X,
                                                    y,
                                                    test_size=0.2,
                                                    random_state=1)


# print('Training Data', X_train.shape)
# print('Testing Data', X_test.shape)
# print(X_train[:10])


# Learning Math
# Teacher has 50 sums with answers


# Training
# Give you 40 questions and answers and ask to study!

# Testing
# 10 sums with no answers..
# Teacher compares your answers with correct answers and checks your score


### 4. Pass training data to the regressor


# Set up a blank regressor
linreg = LinearRegression()
linreg.fit(X_train, y_train)


print('Coefficient: ', linreg.coef_)
print('Intercept: ', linreg.intercept_)

# Minimise the squared residuals between truth values and the prediction

scores = [10, 5, 100, 12, 65]
preds =  [11, 5, 100, 13, 63]
diff =   [1,  0,  0,   1,  2] # Residuals/Deltas/Differences

# for s in scores:
#   print(s, linreg.predict([[s]]))

### 5. Evaluate by testing performance with the test data


# heres the remaining 20% of data.... make some guesses!
predictions = linreg.predict(X_test)


accuracy = metrics.mean_absolute_error(y_test, predictions)
print(accuracy)


#### Research Linear Regression:
#### Logistic Regression, Ridge/Lasso Regression



