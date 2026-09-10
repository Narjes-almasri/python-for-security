# regular expression module for pattern matching
# Technique 3: extract a pattern (an IP address) with re.search()
import re
line = "2026-02-10 08:04:59 WARNING Connection retry to 172.16.0.9" 
ip = re.search(r"\d+\.\d+\.\d+\.\d+",line)
print ("ip = ", ip)