# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "49a0b936-d027-4966-adb6-5d9d3f416535",
# META       "default_lakehouse_name": "hospital_lakehouse",
# META       "default_lakehouse_workspace_id": "8edd74b2-e6e6-4847-94a1-e96434b2ea84",
# META       "known_lakehouses": [
# META         {
# META           "id": "49a0b936-d027-4966-adb6-5d9d3f416535"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

df = spark.read.option('header',True).csv('abfss://8edd74b2-e6e6-4847-94a1-e96434b2ea84@onelake.dfs.fabric.microsoft.com/49a0b936-d027-4966-adb6-5d9d3f416535/Files/bronze/patient/2026-38-03/2026-01-03.csv')

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df.show()

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df.write.mode("overwrite").format("delta").saveAsTable("bronze_patients")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
