for i in {1..50}; do echo -n "Run # $i :: "; 
curl -w 'Return code: %{http_code}; Bytes Received: %{size_download}; 
Response Time: %{time_total}\n' http://172.20.0.2:80 -m 2 -o /dev/null -s; 
done|tee /dev/tty|awk '{ sum+= $NF; n++ } END { if (n > 0) print "Average Response time =",sum / n; }'