import streamlit as st
import pandas as pd
import joblib
import warnings
warnings.filterwarnings("ignore")

# Load the model and preprocessor
model = joblib.load("finalized model/model.joblib")   
preprocessor = joblib.load("finalized model/preprocessor.joblib")

def main():
    st.title('IBM Anti-Launder Prediction')
    st.markdown("Please fill the details below for the Prediction")

    # Create a form for input
    with st.form("IBM Anti-Launder Prediction"):
        Day = st.selectbox('Day of Transaction', ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'])
        From_Bank = st.text_input('Enter from bank id', value="12345")
        Account_from_bank = st.text_input("Enter account from bank", value="54321")
        To_Bank = st.text_input('Enter to bank id', value="67890")
        Account_to_bank = st.text_input("Enter account to bank", value="09876")
        Amount_Received = st.slider('Amount Received', 1.0, 1000000.0, step=0.1, value=10.0)
        Receiving_Currency = st.selectbox('Receiving Currency', ['US Dollar','Euro','Yuan','Shekel','Canadian Dollar','UK Pound','Ruble','Australian Dollar',   
                                                                 'Yen','Mexican Peso','Swiss Franc','Rupee','Bitcoin','Brazil Real','Saudi Riyal','Others'])
        Amount_Paid = st.slider('Amount Paid', 1.0, 1000000.0, step=0.1, value=10.0)
        Payment_Currency  = st.selectbox('Payment Currency', ['US Dollar','Euro','Yuan','Shekel','Canadian Dollar','UK Pound','Ruble','Australian Dollar',   
                                                              'Yen','Mexican Peso','Swiss Franc','Rupee','Bitcoin','Brazil Real','Saudi Riyal','Others'])
        Payment_Format = st.selectbox('Payment Format', ['Cheque', 'Credit Card', 'ACH','Cash','Reinvestment','Wire','Bitcoin'])

        submit_button = st.form_submit_button("Submit")

    if submit_button:
        try:
            input_data = pd.DataFrame({
                'From Bank': [From_Bank], 
                'Account': [Account_from_bank],
                'To Bank': [To_Bank],
                'Account.1': [Account_to_bank], 
                'Amount Received': [Amount_Received],
                'Receiving Currency': [Receiving_Currency], 
                'Amount Paid': [Amount_Paid],
                'Payment Currency': [Payment_Currency], 
                'Payment Format': [Payment_Format],
                'Day': [Day] 
            })

            # Preprocess the input data
            X_transformed = preprocessor.transform(input_data)

            # Make the prediction
            prediction = model.predict(X_transformed)[0]

            result_text = "Is Laundering" if prediction == 1 else "Is Not Laundering"
            st.write(f"Predicted Result: {result_text}")

        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()