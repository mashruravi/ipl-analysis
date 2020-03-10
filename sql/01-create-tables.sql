/* Drop tables if they exist */
DROP TABLE teams;

CREATE TABLE teams(
    team_id varchar(4),
    team_name varchar(64)
);
