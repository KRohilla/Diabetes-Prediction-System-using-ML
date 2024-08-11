# Diabetes-Prediction-System-using-ML
Basic machine learning model deployment using the Streamlit library <br>

<strong> Overview</strong> <br>
Diabetes prediction using machine learning involves developing a model that predicts whether an individual has diabetes 
based on various health-related features. This process typically uses a dataset with features such as the number of pregnancies, glucose levels, blood pressure, skin thickness, insulin levels, BMI, diabetes pedigree function, and age.

<br><strong> Steps Involved</strong> <br>
<strong> Data Collection and Preprocessing</strong> <br>
The first step is gathering relevant data, commonly from datasets like the Pima Indians Diabetes Database. 
Data preprocessing involves handling any missing values, normalizing the data, and splitting it into training and testing sets.

<br><strong> Feature Selection</strong> <br>
Selecting the most relevant features from the dataset is crucial for improving the model's accuracy. This can <br>
The features used in the prediction model include: <br>
Pregnancies: Number of pregnancies. <br>
Glucose: Plasma glucose concentration. <br>
Blood Pressure: Diastolic blood pressure (mm Hg). <br>
Skin Thickness: Triceps skinfold thickness (mm). <br>
Insulin: 2-Hour serum insulin (mu U/ml). <br>
BMI: Body mass index (weight in kg/(height in m)^2). <br>
Diabetes Pedigree Function: Likelihood of diabetes based on family history. <br>
Age: Age of the patient. <br>

<strong></strong>Model Selection and Training</strong>  <br>
Various machine learning models, such as Logistic Regression, Decision Trees, Random Forest, or Support Vector Machines, can be used. The chosen model is trained on the training data and validated on the testing data to ensure it performs well.

<br><strong> Model Evaluation</strong> <br>
The model's effectiveness is assessed using metrics like accuracy, precision, recall, and F1-score. Cross-validation techniques can further ensure the model's robustness.

<br><strong> Saving the Model</strong> <br>
Once trained, the model can be saved using a serialization technique like pickle. This allows the model to be stored and reused without needing to retrain it each time.

<br><strong> Deployment Using Streamlit</strong> <br>
The saved model can be deployed as a web application using the Streamlit library. Streamlit provides an easy way to create an interactive interface where users can input features and get predictions. This makes the model accessible to a broader audience.
