import numpy as np
import csv

# def export_landmarks(results,action):
#     try:
#         keypoints=np.array([[res.x,res.y,res.z,res.v] for res in results.pose_landmarks.landmark]).flatten()
#         keypoints.insert(1,action)

#         with open('coords.csv',mode='a',newline='') as f:
#             csv_writer=csv.writer(f,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
#             csv_writer.writerow(keypoints)
#     except Exception as e:
#         pass
import pandas as pd

df=pd.read_csv('coords.csv')
print(df.head())