from pyspark.sql import SparkSession
from pyspark.sql.functions import expr, col, explode
import json

# Spark 세션 생성
spark = SparkSession.builder.getOrCreate()

# json 데이터 읽기
path_json = '/users/kimdohoon/Desktop/TESTFOLDER/39_Tinfo.json'
with open (path_json, 'r') as file:
    data_json = json.load(file)


# 데이터프레임 생성
data_rdd = spark.sparkContext.parallelize(data_json["data"])
df = data_rdd.flatMap(lambda sublist: sublist) \
             .select(expr("team").alias("team"), expr("venue").alias("venue"))

df.show()