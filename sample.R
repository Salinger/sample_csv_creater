start_time <- proc.time()
library("dplyr")
df <- read.csv(
    "/Users/tatsuya/Dropbox/Programing/mcmd/data/sample/payment_sample.csv"
    )
result <- group_by(df,user_id) %.%
    summarise(
        payment_avg=sum(payment)
        )
end_time <- proc.time() - start_time
print(end_time)
