from pyspark.sql import SparkSession

if __name__ == '__main__':
    spark = SparkSession.builder.appName("ExerciseSpark").getOrCreate()

    input_path = spark.read.csv('')
