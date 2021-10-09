from pyspark.sql import SparkSession 

spark = (
    SparkSession.build.appName("ExerciseSpark").getOrCreate()
)


enem = (
    spark
    .read
    .format("csv")
    .option("header", True)
    .option("inferSchema", True)
    .option("delimiter", ";")
    .load("s3://datalake-herbert-igti-edc/raw-data/enem/")
)

enem = (
    spark
    .write
    .mode("overwrite")
    .formar("parquet")
    .partitionBy("year")
    .save("s3://datalake-herbert-igti-edc/staging/enem")
)