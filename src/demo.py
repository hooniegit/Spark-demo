from pyspark.sql import SparkSession

# Spark Session Build
spark = SparkSession.builder.getOrCreate()
print("spark session built successfully")