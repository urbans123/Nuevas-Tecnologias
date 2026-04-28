import pandas as pd

#Rutina para crear un archivo JSON desde python
def crear_json(data_frame):
   data_frame.to_json("archivo.json", orient="records", indent=4)

#Rutina para crear un archivo csv desde python
def crear_csv(data_frame):
    print(data_frame)
    data_frame.to_csv("archivo.csv", index=False)