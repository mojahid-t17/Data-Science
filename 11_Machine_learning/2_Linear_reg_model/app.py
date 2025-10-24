from flask import Flask, render_template, request, jsonify
import pandas as pd
import numpy as np
import joblib
from sklearn.preprocessing import StandardScaler
import warnings
warnings.filterwarnings('ignore')

app = Flask(__name__)

# Load the trained model
model = joblib.load('sddg_regressor_model.pkl')

# Load the original data to get the scaler parameters
df_original = pd.read_csv('regression_mobile_price.csv')

# Preprocessing function that replicates the notebook pipeline
def preprocess_data(input_data):
    """
    Preprocess input data following the same steps as in the notebook
    """
    # Create a DataFrame from input data
    df = pd.DataFrame([input_data])
    
    # Data cleaning and imputation (same as notebook)
    # Fill missing values with mode/mean
    df['OS'].fillna(df_original['OS'].mode()[0], inplace=True)
    df['display_type'].fillna(df_original['display_type'].mode()[0], inplace=True)
    df['SIM'].fillna(df_original['SIM'].mode()[0], inplace=True)
    df['battery'].fillna(df_original['battery'].mean(), inplace=True)
    df['internal_memory_GB'].fillna(df_original['internal_memory_GB'].mode()[0], inplace=True)
    
    # Fix typo in SIM column
    df['SIM'] = df['SIM'].replace('Sengle', 'Single')
    
    # Handle outliers using IQR method (same as notebook)
    numerical_cols = ['weight_g', 'display_resolution', 'display_size_ppi', 'memory_card', 
                     'internal_memory_GB', 'RAM_GB', 'primary_camera', 'secondary_camera', 'battery']
    
    for col in numerical_cols:
        if col in df.columns:
            Q1 = df_original[col].quantile(0.25)
            Q3 = df_original[col].quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
            
            # Check if value is outlier and replace with median
            if df[col].iloc[0] < lower_bound or df[col].iloc[0] > upper_bound:
                df[col] = df_original[col].median()
    
    # Categorical encoding (same mappings as notebook)
    sim_mapping = {'Dual': 1, 'Single': 0}
    display_type_mapping = {'IPS': 2, 'TFT': 1, 'Capacitive': 0, 'Super AMOLED': 4, 'AMOLED': 3}
    os_mapping = {'Marshmallow': 0, 'Lollipop': 1, 'KitKat': 2, 'Jelly Bean': 3, 'Ice Cream Sandwich': 4, 'Nougat': 5}
    cpu_mapping = {'Quad-core': 1, 'Octa-core': 3, 'Dual-core': 0, 'Hexa-core': 2}
    
    df['SIM'] = df['SIM'].map(sim_mapping)
    df['display_type'] = df['display_type'].map(display_type_mapping)
    df['OS'] = df['OS'].map(os_mapping)
    df['CPU'] = df['CPU'].map(cpu_mapping)
    
    # Remove target column if present
    if 'approx_price_EUR' in df.columns:
        df = df.drop('approx_price_EUR', axis=1)
    
    # Standard scaling
    scaler = StandardScaler()
    
    # Fit scaler on original training data (excluding target)
    X_original = df_original.drop('approx_price_EUR', axis=1)
    
    # Apply same preprocessing to original data
    X_original['OS'].fillna(X_original['OS'].mode()[0], inplace=True)
    X_original['display_type'].fillna(X_original['display_type'].mode()[0], inplace=True)
    X_original['SIM'].fillna(X_original['SIM'].mode()[0], inplace=True)
    X_original['battery'].fillna(X_original['battery'].mean(), inplace=True)
    X_original['internal_memory_GB'].fillna(X_original['internal_memory_GB'].mode()[0], inplace=True)
    X_original['SIM'] = X_original['SIM'].replace('Sengle', 'Single')
    
    # Apply outlier treatment to original data
    for col in numerical_cols:
        Q1 = X_original[col].quantile(0.25)
        Q3 = X_original[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        outliers = (X_original[col] < lower_bound) | (X_original[col] > upper_bound)
        median = X_original[col].median()
        X_original.loc[outliers, col] = median
    
    # Apply categorical encoding to original data
    X_original['SIM'] = X_original['SIM'].map(sim_mapping)
    X_original['display_type'] = X_original['display_type'].map(display_type_mapping)
    X_original['OS'] = X_original['OS'].map(os_mapping)
    X_original['CPU'] = X_original['CPU'].map(cpu_mapping)
    
    # Fit scaler on original data
    scaler.fit(X_original)
    
    # Transform input data
    df_scaled = scaler.transform(df)
    
    return df_scaled

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input data from form
        input_data = {
            'weight_g': float(request.form['weight_g']),
            'SIM': request.form['SIM'],
            'display_type': request.form['display_type'],
            'display_resolution': float(request.form['display_resolution']),
            'display_size_ppi': int(request.form['display_size_ppi']),
            'OS': request.form['OS'],
            'CPU': request.form['CPU'],
            'memory_card': int(request.form['memory_card']),
            'internal_memory_GB': float(request.form['internal_memory_GB']),
            'RAM_GB': float(request.form['RAM_GB']),
            'primary_camera': float(request.form['primary_camera']),
            'secondary_camera': float(request.form['secondary_camera']),
            'battery': float(request.form['battery'])
        }
        
        # Preprocess the data
        processed_data = preprocess_data(input_data)
        
        # Make prediction
        prediction = model.predict(processed_data)[0]
        
        # Return prediction result
        return jsonify({
            'success': True,
            'predicted_price': round(prediction, 2),
            'predicted_price_formatted': f"€{round(prediction, 2):,}"
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
