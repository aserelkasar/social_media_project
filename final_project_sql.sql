 create database data_network;
 
 use data_network;
 
 create table _user(
 username varchar(255) primary key,
 user_password varchar(255) not null,
 user_role int not null,
 user_first_name varchar(255) not null,
 user_last_name varchar(255) not null
 );
 
create table _post(
post_id int primary key auto_increment,
post_name varchar(255) not null,
post_content varchar(255) not null,
post_username varchar(255) not null
);

create table _comment(
comment_id int primary key auto_increment,
comment_content varchar(255) NOT NULL,
id_of_post int not null,
comment_username varchar(255) not null
);

alter table _post add constraint foreign key (post_username) references _user(username);
alter table _comment add constraint foreign key (id_of_post) references _post(post_id);
alter table _comment add constraint foreign key (comment_username) references _user(username);