# indian-food-recognition-calorie-estimation
AI-powered Indian Food Recognition and Calorie Estimation using YOLOv8 and Flask
Overview

Developed an AI-powered system for detecting Indian food items and estimating their calorie content. The system uses YOLOv8 for food detection and a Flask-based API pipeline for calorie estimation.

Features
Detects 30+ Indian food categories
Real-time object detection using YOLOv8
Calorie estimation pipeline
Flask API integration
Trained on custom Indian food dataset
Supports restaurant and street-food items
Tech Stack
Python
YOLOv8
Flask
Roboflow
OpenCV
Pandas
Kaggle GPU (Tensor T4 × 2)
Dataset

Custom dataset prepared and annotated using Roboflow, containing Indian food items across categories such as:

Snacks
Main Course
Desserts
Project Workflow
Image Input
Food Detection using YOLOv8
Food Classification
Weight Estimation
Calorie Calculation
Result Display
Results
Successfully trained on 30+ food categories
Accurate food localization and classification
Automated calorie estimation pipeline
Future Scope
Nutritional analysis (Protein, Carbs, Fats)
Food freshness detection
Mobile application deployment
Depth estimation for improved portion-size calculation
