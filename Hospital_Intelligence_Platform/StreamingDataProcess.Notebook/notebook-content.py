# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {}
# META }

# CELL ********************

import random as ran
import time

while True:
    data = []
    for i in range(0, 10, 1):
        row = []
        row.append(ran.randint(500, 5000))
        row.append(ran.randint(1, 10))
        row.append(ran.randint(1, 5))
        row.append(ran.randint(1, 100))
        row.append(ran.randint(100000, 999999))
        row.append(time.strftime("%Y%m%d-%H%M%S"))
        data.append(row)

    df2 = spark.createDataFrame(data, ['patient_id', 'bedrooms', 'min_heart_rate', 'max_heart_rate', 'timestamp'])
    timestamp_var = time.strftime("%Y%m%d-%H%M%S")
    
    

    time.sleep(10)
    

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
