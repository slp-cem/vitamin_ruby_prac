create table post (
  title  text,
  main   text,
  id     integer
);

create table comment (
  viewer  text,
  content text,
  post_id integer
);