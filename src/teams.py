from pyspark.sql import SparkSession
from pyspark.sql.functions import expr, explode
import json

import pandas as pd

# spark session 빌드
spark = SparkSession.builder.getOrCreate()

# json 데이터 읽기
path_json = '/users/kimdohoon/Desktop/TESTFOLDER/39_Tinfo.json'
with open (path_json, 'r') as file:
    data_json = json.load(file)

# 리스트 내부의 리스트를 합치는 pandas 로직
combined_data = []
for sublist in data_json["data"]:
    combined_data.extend(sublist)

# JSON 데이터를 Spark DataFrame으로 변환
df = spark.createDataFrame(combined_data)
df.printSchema()

# df_specification = dataframe.select( *col , explode(col( col=dict )).alias( name1 , name2 , .. ))
df_team = df.select(explode("team").alias("code", "country", "founded", "team_id", "logo", "name", "national"))
df_team.show()

df_venue = df.select(explode("venue").alias("venue_address", "venue_capacity", "venue_location", "venue_id", "venue_image", "venue_name", "venue_surface"))
df_venue.show()

df_specification = df.withColumn("team_code", expr()) \
                     .withColumn("team_country", expr()) \
                     .withColumn("team_founded", expr()) \
                     .withColumn("team_id", expr()) \
                     .withColumn("team_logo", expr()) \
                     .withColumn("team_name", expr()) \
                     .withColumn("team_national", expr()) \
                     .withColumn("address", expr()) \
                     .withColumn("capacity", expr()) \
                     .withColumn("location", expr()) \
                     .withColumn("id", expr()) \
                     .withColumn("image", expr()) \
                     .withColumn("name", expr()) \
                     .withColumn("surface", expr())
