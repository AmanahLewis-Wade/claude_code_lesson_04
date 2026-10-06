from pyspark.sql import SparkSession
spark = SparkSession.builder.getOrCreate()

import pandas as pd


d = [{'name': 'apple', 'price': 0.50}]
df=spark.createDataFrame(d)
df.show()