#!/usr/local/bin/ruby
# -*- coding: utf-8 -*-

require 'cgi'

cgi = CGI.new

puts cgi.header("charset" => "utf-8")
print <<EOM
<html>
  <head>
    <title>簡易ブログ投稿ページ</title>
  </head>
  <body>
    <h1>記事を投稿する</h1>
    <hr>
    <form method="post" action="blog1.cgi">
    <p>タイトル</p>
    <p><input type="text" name="title"></p>
    <p>本文</p>
    <textarea name="main" cols="50" rows="10"></textarea>
    <p><input type="submit" value="投稿"></p>
    </form>
  </body>
</html>
EOM
