# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 10:52:09 2024

@author: USER
"""

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import ttkbootstrap as ttkb
import joblib
import numpy as np

# Loading the models
model_1hr = joblib.load('model_1h.pkl')  
model_3hr = joblib.load('model_3h.pkl') 
scaler = joblib.load('scaler.pkl')

def predict_rainfall():
    try:
        # Geting input from the user for all 5 required features
        rfh = float(entry_rfh.get())
        r1h_avg = float(entry_r1h_avg.get())
        r3h_avg = float(entry_r3h_avg.get())
        r1q = float(entry_r1q.get())
        r3q = float(entry_r3q.get())

        # Creating and array with the 5 features
        input_data = np.array([[rfh, r1h_avg, r3h_avg, r1q, r3q]])

        # Scale the input data using scaler model
        input_data_scaled = scaler.transform(input_data)

        if model_var.get() == '1_hour':
            # Predict rainfall for 1-hour
            prediction = model_1hr.predict(input_data_scaled)[0]
            messagebox.showinfo("Prediction", f"Predicted 1-month Rainfall Amount is: {prediction:.2f} ")
        else:
            # Predict rainfall for 3-hour
            prediction = model_3hr.predict(input_data_scaled)[0]
            messagebox.showinfo("Prediction", f"Predicted 3-month Rainfall Amount is: {prediction:.2f} ")
            
    except ValueError as ve:
        messagebox.showerror("Error", str(ve))
    except Exception as e:
        messagebox.showerror("Error", "Please enter valid inputs.")

# main window
root = ttkb.Window(themename="solar")
root.title("Rainfall Prediction Model")
root.geometry("1500x700")

# Create and place the widgets
frame = ttkb.Frame(root, padding="10 10 10 10")
frame.pack(fill=tk.BOTH, expand=True)

# Title
label_title = ttkb.Label(frame, text="Rainfall Prediction Model", font=('Arial', 25, 'bold'))
label_title.grid(row=0, column=0, columnspan=5, pady=20)

# Input Fields for Rainfall in mm, rolling aggregation average
label_rfh = ttkb.Label(frame, text="10 day rainfall [mm]:", font=('Arial', 14))
label_rfh.grid(row=2, column=0, pady=10, padx=10)

entry_rfh = ttkb.Entry(frame)
entry_rfh.grid(row=2, column=1, pady=10, padx=10)

label_3hr = ttkb.Label(frame, text="1-month rolling aggregation average:", font=('Arial', 14))
label_3hr.grid(row=2, column=2, pady=10, padx=10)

entry_r3h_avg = ttkb.Entry(frame)
entry_r3h_avg.grid(row=2, column=3, pady=10, padx=10)

label_r1h_avg = ttkb.Label(frame, text="3-month rolling aggregation average: ", font=('Arial', 14))
label_r1h_avg.grid(row=3, column=0, pady=10, padx=10)

entry_r1h_avg = ttkb.Entry(frame)
entry_r1h_avg.grid(row=3, column=1, pady=10, padx=10)

# Labels and Entry Fields for rainfall anomaly [%]
label_r3q = ttkb.Label(frame, text="rainfall 1-month anomally [mm]:", font=('Arial', 14))
label_r3q.grid(row=3, column=2, pady=10, padx=10)

entry_r3q = ttkb.Entry(frame)
entry_r3q.grid(row=3, column=3, pady=10, padx=10)

label_r1q_rainfall = ttkb.Label(frame, text="rainfall 3-month anomally [mm]", font=('Arial', 14))
label_r1q_rainfall.grid(row=4, column=0, pady=10, padx=10)

entry_r1q = ttkb.Entry(frame)
entry_r1q.grid(row=4, column=1, pady=10, padx=10)

# Model Selection Radio Buttons
label_model = ttkb.Label(frame, text="Select Model:", font=('Arial', 14))
label_model.grid(row=5, column=0, pady=20, padx=10)

model_var = tk.StringVar(value='1_hour')
radio_1hr = ttkb.Radiobutton(frame, text='1 month Model', variable=model_var, value='1_hour')
radio_1hr.grid(row=5, column=1, pady=10, padx=10)

radio_3hr = ttkb.Radiobutton(frame, text='3 month Model', variable=model_var, value='3_hour')
radio_3hr.grid(row=5, column=2, pady=10, padx=10)

# Predict Button
button_predict = ttkb.Button(frame, text="Predict Rainfall", command=predict_rainfall, bootstyle="success")
button_predict.grid(row=6, column=0, columnspan=4, pady=20)

# Start the main loop
root.mainloop()


