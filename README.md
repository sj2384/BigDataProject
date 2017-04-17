To generate the first table regarding details of each column. You need to run the script in ./code/column_investigation/

For example, in order to get BORO_NM.out, on dumbo you run
hjs -D mapreduce.job.reduces=1 -files <dumbo_directory> -mapper <dumbo_directory>/map_BORO_NM.py -reducer <dumbo_directory>/reduce_BORO_NM.py -input <hdfs_directory>/NYPD_Complaint_Data_Historic.csv -output <hdfs_directory>/BORO_NM.out
Then you use getmerge  and scp command to transfer output file from hdfs and dumbo to your local directory.

To generate most of graphs in the summary, you run weitao.ipynb which takes the output files from previous steps to generate graphs.

There are also some graphs generated from different sources:

