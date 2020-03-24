Internet Technology Project 1
Ryan Mulhall & Raymond Lin
rem208 rl512

1. We implemented our recursive client by sending the hostnames and then receiving the responses from the RS program. Then it sends the unresolved hostnames to the TS and receives it's response. For the DNS table, both the RS and TS implement a dictionary loaded from the text file with the hostname as a key and stored the IP and flag as a tuple.

2. One aspect of our program is that it does not store the hostnames in RESOLVED.txt in the same order as the hostname file. It resolves the hostnames correctly, but first writes the RS responses to the file and then writes the TS responses.

3. The main problem that was faced was getting the data to be sent and received at the correct points in time so that at no point was there any program waiting on a socket that wasn't sending/receiving data. The other difficulty was with testing as there were three files to debug which caused some difficulty.

4. We learned how to use multiple sockets and dictionaries in python.
