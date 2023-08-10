'''
json 파일을 파싱하여 dataframe을 생성하는 파일 예제
'''

from pyspark.sql import SparkSession
from pyspark.sql.functions import expr, explode

# spark session 빌드
spark = SparkSession.builder.getOrCreate()

# parquet 파일 읽기
PARQUET_PATH = 'file:/Users/kimdohoon/git/Spotify-Playground/spotify-API/Airflow/sample_hooniegit/datas/parquets/playlists/Hot Hits Korea/items/*'

# dataframe 생성 및 가공
dataframe = spark.read.parquet(PARQUET_PATH)
df_specification = dataframe.withColumn("album_type", expr("track.album.album_type")) \
                                   .withColumn("album_images", expr("track.album.images")) \
                                   .withColumn("album_name", expr("track.album.name")) \
                                   .withColumn("album_artists", expr("track.album.artists.name")) \
                                   .withColumn("popularity", expr("track.popularity")) \
                                   .withColumn("track_name", expr("track.name")) \
                                   .select("album_type", "album_images", "album_name", "album_artists", "popularity", "track_name")

# dataframe 확인
df_specification.show()