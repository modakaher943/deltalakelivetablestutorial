# Databricks notebook source
df = spark.read.table("dltprasad.source.orders")
df.display()

# COMMAND ----------


