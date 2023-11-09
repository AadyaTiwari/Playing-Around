import speedtest as st
server = st.Speedtest()
server.get_best_server

down = server.download()
down = down/1000000

print(f"Download Speed is {down} Mbps")

up = server.upload()
up = up/1000000
print(f"Upload speed is {up} Mbps")

ping = server.results.ping
print(f"Ping Speed is {ping}")