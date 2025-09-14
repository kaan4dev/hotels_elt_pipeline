from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("HotelReservations").getOrCreate()

df = spark.read.csv("hotel_bookings.csv", header=True, inferSchema=True)

df.show(5)

print(df.columns)