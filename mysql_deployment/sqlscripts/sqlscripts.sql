CREATE DATABASE mydb;


GRANT ALL PRIVILEGES ON mydb.* TO 'root'@'%';

USE mydb;

CREATE TABLE IF NOT EXISTS mytable(
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    phone VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL);


INSERT INTO mytable(username,phone,email)
VALUES
("Dusty","8825610826","dbeardsworth0@miibeian.gov.cn"),
("Eugine","9342910475","esavins1@weibo.com"),
("Bryce","7162187948","bmcgarrity2@multiply.com"),
("Hermann","5368937127","heskriet3@fema.gov"),
("Hortense","3568425529","hjoubert4@mac.com"),
("Ferguson","1611156727","fpryn5@networksolutions.com"),
("Eulalie","9313876974","ebrise6@yolasite.com"),
("Ashbey","2847609330","adarrington7@latimes.com"),
("Ragnar","9895384865","rphin8@qq.com"),
("Hewie","3648611482","hbaggot9@slideshare.net"),
("Rosie","6028290978","rvanichkina@goo.gl"),
("Russ","3568221729","rhitchensb@wisc.edu"),
("Isador","9221157674","ikeyworthc@google.co.uk"),
("Carlin","6492068688","cciccod@blog.com"),
("Peta","8621466929","pduckette@tuttocitta.it"),
("Collette","9761651109","cbrumf@sourceforge.net");


