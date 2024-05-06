from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StructField, IntegerType, LongType

schema = StructType([
    StructField('patient_id', IntegerType()),
    StructField('heart_rate', IntegerType()),
    StructField('blood_pressure', IntegerType()),
    StructField('timestamp', LongType())
])

spark = SparkSession.builder \
    .appName("HealthcareDataProcessor") \
    .getOrCreate()

df = spark \
    .readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "kafka:9092") \
    .option("subscribe", "healthcare") \
    .load()

healthcare_df = df.select(from_json(col("value").cast("string"), schema).alias("data")).select("data.*")

filtered_df = healthcare_df.filter(healthcare_df.heart_rate > 70)

query = filtered_df.writeStream \
    .outputMode("append") \
    .format("console") \
    .start()

query.awaitTermination()
