software requirement  
```
php 7+
python 3+
```
Pyton package  
```
Faker, urllib
```
how to run this application  
* using xampp or lamp servive server to run php and mysql
* create database table
```
CREATE TABLE `registered_users` (
  `email` varchar(100) NOT NULL,
  `fullname` varchar(100) NOT NULL,
  `address` varchar(500) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
COMMIT;
```
* run python script
```
python pybot_register.py
```
* or go to this url and continous to register  
```
localhost/yourfoldername
```