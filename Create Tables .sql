use quiz_app
create table  users (
    id int primary key identity(1,1), 
    username varchar(255) unique not null,
    password varchar(255) not null
	
);


create table  subjects (
    id int primary key identity(1,1),
    subject_name varchar(255) unique not null
);

create table question_bank (
    question_id int primary key identity(1,1),
    subject_id int not null,
    question varchar(255) not null,
    option1 varchar(255) not null,
    option2 varchar(255) not null,
    option3 varchar(255) not null,
    option4 varchar(255) not null,
    correct_option int not null,
    foreign key (subject_id) references subjects (id) on delete cascade
);


