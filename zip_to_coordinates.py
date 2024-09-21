import redivis

user = redivis.user("stanfordphs")
dataset = user.dataset("us_zip_codes_to_longitude_and_latitude:d5sz:v1_1")
table = dataset.table("us_zip_codes_to_longitude_and_latitude:j864")

# Load table as a dataframe
df = table.to_pandas_dataframe(max_results=100)
df.head()
