curl https://www.post.japanpost.jp/zipcode/dl/kogaki/zip/ken_all.zip -o data/ken_all.zip
unzip -o data/ken_all.zip -d data
rm data/ken_all.zip

curl http://mobile.shinsv.mydns.jp/jinmei/ime-import.zip -o data/ime-import.zip
unzip -o data/ime-import.zip -d data
rm data/ime-import.zip