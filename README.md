#simpleDNS
Uses a root and top level server programs (rs.py and ts.py) each with their own DNS table stored in text files and implemented through a dictionary. The client can then connect to these servers in order to resolve it's own list of hostnames with their appropriate IP addresses, and then stores the results in RESOLVED.txt.

#loadBalancingDNS
Uses a load balancing DNS server which then connects to two other DNS servers in order to resolve IP's
