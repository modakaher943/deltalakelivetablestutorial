
# import dlt

# #Create Streaming table 
# @dlt.table(
#     name = "first_stream_table"
# )

# def first_stream_table():
#     df = spark.readStream.table("dltprasad.source.orders")
#     return df

# #create materialized view

# @dlt.table(
#     name= "first_mat_view"
# )
# def first_mat_view():
#     df = spark.read.table("dltprasad.source.orders")
#     return df

# #create batch view
# @dlt.view(
#     name= "first_batch_view"
# )
# def first_batch_view():
#     df = spark.readStream.table("dltprasad.source.orders")
#     return df

# #create streaming view
# @dlt.view(
#     name= "first_stream_view"
# )
# def first_stream_view():
#     df = spark.readStream.table("dltprasad.source.orders")
#     return df




