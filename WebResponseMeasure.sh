for i in {1..50}; do echo -n "Run # $i :: "; 
curl -w 'Return code: %{http_code}; Bytes Received: %{size_download}; 
 time_namelookup:  %{time_namelookup}s\n
 time_connect:  %{time_connect}s\n
 time_appconnect:  %{time_appconnect}s\n
 time_pretransfer:  %{time_pretransfer}s\n
 time_redirect:  %{time_redirect}s\n
 time_starttransfer:  %{time_starttransfer}s\n
 ----------\n
 time_total:  %{time_total}s\n
Response Time: %{time_total}\n' http://172.20.0.2:80 -m 2 -o /dev/null -s; 
done|tee /dev/tty|awk '{ sum+= $NF; n++ } END { if (n > 0) print "Average Response time =",sum / n; }'