from pyspark.sql import SparkSession

spark = SparkSession  \
	.builder  \
	.appName("StructuredSocketRead")  \
	.getOrCreate()
	
lines = spark  \
	.readStream  \
	.format("socket")  \
	.option("host","localhost")  \
	.option("port",12345)  \
	.load()
	
query = lines  \
	.writeStream  \
	.outputMode("append")  \
	.format("console")  \
        .option("truncate", "False")  \
	.start()
	
query.awaitTermination()
