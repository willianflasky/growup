#/bin/sh
apikey="4W7Be819ba7bf63e7c8cd8fe92101112d7"
mobile=$1
text="报警信息$2,报警内容$3【VIP】"
echo "get user info:"

curl --data "apikey=$apikey" "https://sms.yunpian.com/v1/user/get.json"
echo "\nsend sms:"
#curl --data "apikey=$apikey&mobile=$mobile&text=$text" "http://yunpian.com/v1/sms/send.json"
curl --data "apikey=$apikey&mobile=$mobile&text=$text" "https://sms.yunpian.com/v1/sms/send.json"
