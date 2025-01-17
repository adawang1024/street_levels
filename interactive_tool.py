import joblib

# Load the model from disk
dt_model = joblib.load('dt_model.joblib')

def predict_stress(inputs):
    # Predicting stress level based on the user inputs
    prediction = dt_model.predict([inputs])
    return prediction[0]

def main():
    print("Welcome to the Stress Level Predictor!")
    try:
        # Asking for user input for each feature
        study_hours = float(input("Enter your daily study hours: "))
        sleep_hours = float(input("Enter your daily sleep hours: "))
        social_hours = float(input("Enter your daily social hours: "))
        physical_activity_hours = float(input("Enter your daily physical activity hours: "))
        gpa = float(input("Enter your GPA: "))
        
        # Combine all feature inputs into a list
        inputs = [study_hours, sleep_hours, social_hours, physical_activity_hours, gpa]

        # Predicting stress level based on the inputs
        stress_level = predict_stress(inputs)
        print(f"Predicted stress level: {stress_level}")

    except ValueError:
        print("Please enter valid numbers for all inputs.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
