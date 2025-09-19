from pyspark.sql import SparkSession
import argparse

def main(input_path, output_path):
    spark = SparkSession.builder.appName("HotelReservationsETL").getOrCreate()

    df = spark.read.csv(input_path, header=True, inferSchema=True)
    df.write.mode("overwrite").parquet(output_path)

    spark.stop()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    main(args.input, args.output)
