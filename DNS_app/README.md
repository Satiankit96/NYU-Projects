Docker image: https://hub.docker.com/repository/docker/ankitsati096/user-server
$ docker build -t ankitsati096/user-server:latest .
Sending build context to Docker daemon  10.24kB
Step 1/8 : FROM python:3.9
 ---> e2d7fd224b9c
Step 2/8 : RUN apt-get update   && apt-get clean   && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
 ---> Using cache
 ---> 4d1b3e38e705
Step 3/8 : RUN groupadd -g 799 nyu &&     useradd -r -u 999 -g nyu nyu
 ---> Using cache
 ---> c1770a5e67b3
Step 4/8 : WORKDIR /app
 ---> Using cache
 ---> cc583be82e08
Step 5/8 : RUN pip install Flask
 ---> Using cache
 ---> c9731b823fc1
Step 6/8 : USER nyu
 ---> Using cache
 ---> 6bbc9fc4952f
Step 7/8 : COPY --chown=nyu:nyu . .
 ---> 13eb564bea77
Step 8/8 : CMD [ "python", "./user_server.py" ]
 ---> Running in 18ddef678d85
Removing intermediate container 18ddef678d85
 ---> 71eb56846a08
Successfully built 71eb56846a08
Successfully tagged ankitsati096/user-server:latest
(base) ~/ankit_sati_assignment/dns_app/user_server$ docker run -p 8080:8080 ankitsati096/user-server
 * Serving Flask app 'user_server' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
[11:22:19 PM]  * Running on all addresses.
   WARNING: This is a development server. Do not use it in a production deployment.
[11:22:19 PM]  * Running on http://172.17.0.3:8080/ (Press CTRL+C to quit)
[11:22:19 PM]  * Restarting with stat
[11:22:19 PM]  * Debugger is active!
[11:22:19 PM]  * Debugger PIN: 118-351-383


$ docker push ankitsati096/user-server
Using default tag: latest
The push refers to repository [docker.io/ankitsati096/user-server]
ee00e2cd5c4e: Pushed 
45623b179400: Mounted from ankitsati096/fibonacci-server 
29ab41e8e8d4: Mounted from ankitsati096/fibonacci-server 
25c0ee8241be: Mounted from ankitsati096/fibonacci-server 
b360058cc67d: Mounted from ankitsati096/fibonacci-server 
febe96d6107f: Mounted from ankitsati096/fibonacci-server 
7b656b8058c4: Mounted from ankitsati096/fibonacci-server 
02a38a00d553: Mounted from ankitsati096/fibonacci-server 
7fcd2600f5ad: Mounted from ankitsati096/fibonacci-server 
8f56c3340629: Mounted from ankitsati096/fibonacci-server 
ba6e5ff31f23: Mounted from ankitsati096/fibonacci-server 
9f9f651e9303: Mounted from ankitsati096/fibonacci-server 
0b3c02b5d746: Mounted from ankitsati096/fibonacci-server 
62a747bf1719: Mounted from ankitsati096/fibonacci-server 
latest: digest: sha256:809d505dac2d3e1b3d59192d1773d4b71a263b4a892e7c93bdca301f59d3ee3b size: 3259




