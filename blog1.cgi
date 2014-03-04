#!/usr/local/bin/ruby
# -*- coding: utf-8 -*-

require 'cgi'
require 'pg'

conn = PGconn.connect(dbname: 'blogsystem', user: 'postgres')

result = conn.exec("select * from post;")
value = result.getvalue(0,0)

cgi = CGI.new
title = cgi["title"]
STDERR.puts "#{}"
unless title.empty?
  text = cgi["main"]
  STDERR.puts "params:#{cgi.params.inspect}"
  STDERR.puts "#{title}"
  find = conn.exec("select id from post;")
  i = find.to_a.last["id"].to_i + 1
  STDERR.puts "i:#{i}"
  STDERR.puts "insert into post values ( '#{title}', '#{text}', #{i} );"
  conn.exec("insert into post values ( '#{title}', '#{text}', #{i} );")
end
  
puts cgi.header("charset" => "utf-8")
print <<EOM
<html>
<head>
  <title>簡易ブログ</title>
</head>
<body>
  <h1>ブログ的なあれ</h1>
  <hr>
EOM

result = conn.exec("select * from post;")

result.each  do |record|
  print <<EOM
    <h2>#{record["title"]}</h2>
    <h3>#{record["main"]}</h3>
    <hr>
EOM
end

com_rec = conn.exec("select * from comment")
com_rec.each do |com_rec|
    print <<EOM
  <table border="1">
    <caption>コメント</caption>
    <tr>
      <th>投稿者</th>
      <td>#{com_rec["viewer"]}</td>
    </tr>
    <tr>
      <th></th>
      <td>#{com_rec["content"]}</td>
    </tr>
  </table>
  <form method="post" action="blog1.cgi">
  <p>ユーザ名</p>
  <p><input type="text" name="name"></p>
  <p>コメント</p>
  <p><textarea name="comment" cols="50" rows="5"></textarea></p>
  <p><input type="submit" value="投稿"></p>
  </form>
  <hr>
EOM
end
print <<EOM
</body>
  
</html>
EOM
