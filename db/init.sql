
CREATE TABLE temperature (
	node VARCHAR(128),
	time DATE,
	temp INTEGER
);

CREATE TABLE tokens (
	token VARCHAR(128),
	node  VARCHAR(128),
	desc  VARCHAR(256)
);
