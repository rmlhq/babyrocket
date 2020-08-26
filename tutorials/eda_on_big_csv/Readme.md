### Pre-requisites

#### Data

You need atleast 50GB free disk space for this step 

Download csv files from [medicare website](https://www.cms.gov/OpenPayments/Explore-the-Data/Dataset-Downloads)


Download 2019 and 2018 medicare data. 
```
wget https://download.cms.gov/openpayments/PGYR19_P063020.ZIP
wget https://download.cms.gov/openpayments/PGYR18_P063020.ZIP
```

Unzip both the files.
```
unzip PGYR19_P063020.ZIP
unzip PGYR18_P063020.ZIP
```

Once unzipped, you will see the following csv files
```
-rwxr-xr-x 1 ubuntu ubuntu 829K Jun 13 17:35 OP_REMOVED_DELETED_PGYR2018_P06302020.csv
-rwxr-xr-x 1 ubuntu ubuntu 955K Jun 13 17:35 OP_DTL_OWNRSHP_PGYR2019_P06302020.csv
-rwxr-xr-x 1 ubuntu ubuntu 1.5M Jun 13 17:35 OP_DTL_OWNRSHP_PGYR2018_P06302020.csv
-rwxr-xr-x 1 ubuntu ubuntu 504M Jun 13 17:43 OP_DTL_RSRCH_PGYR2018_P06302020.csv
-rwxr-xr-x 1 ubuntu ubuntu 493M Jun 13 17:44 OP_DTL_RSRCH_PGYR2019_P06302020.csv
-rwxr-xr-x 1 ubuntu ubuntu 6.0G Jun 13 19:00 OP_DTL_GNRL_PGYR2018_P06302020.csv
-rwxr-xr-x 1 ubuntu ubuntu 5.7G Jun 13 19:08 OP_DTL_GNRL_PGYR2019_P06302020.csv
```


