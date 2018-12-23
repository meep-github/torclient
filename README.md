# torclient-lib
A Simple, Lightweight and Easy To Use, TOR Proxy Library For Python

If you haven't already, you can install a TOR proxy server on linux with the command:
   
    apt-get install tor
    #check installation command for other distros of linux :)

Then edit the file /etc/tor/torrc until you find the line:
    
    "#ControlPort 9051"
    Take away the comment # and edit to:
    "ControlPort 9051"
    
Next, set your password. This can be done by running the command:

    $ tor --hash-password "my super secret password"
      
      16:YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY
     
Copy the 16:YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY output and again, edit /etc/tor/torrc and find the line:

    #HashedControlPassword 16:XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX (this is the default password)
    Take away the comment # and edit to:
    'HashedControlPassword 16:YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY (my super secret password)
    
Save, and run:

    $ service tor start

And thats it.


    
How To Install:

Download the zip file or clone the repo with:

    $ git clone http://github.com/noctua-github/torclient-lib

After, run the setup.py installation script with the install argument:

    $ python setup.py install
    
This will install the dependencies. If not, run:
 
    $ pip install -r requirements.txt
    
Then all the requirements and the library itself should be ready to use
For more information on how to use it, check out the example.py script.

How to use:

First, create a configuration to control your proxy server via the script:

    import torclient
    my_proxy_config = torclient.ControlConfig()
    my_proxy_config.SetControlPort(9051) #default tor control port
    my_proxy_config.SetAuthentication("my super secret password")
    my_proxy_config.SetAddress("127.0.0.1") #Make sure you set this
    my_proxy_config.Apply() #apply settings
    
When you're finished, you can check your config with:

    my_proxy_config.ShowConfig()
    
    '{"Control Port": 9051, "Authentication": "my super secret password"}'
    
Next, setup the proxy connections:

    proxy_session = torclient.InitProxy()
    proxy_socket  = proxy_session.ProxySocket("localhost", 9050, False) #localhost = server, 9050 = port, False = not global proxy sockets (more info in example.py)
    
    #Renew the proxy session/get new IP!
    
    torclient.RenewProxy() #90% chance it will break the socket pipe
    
    #If torclient.RenewProxy() doesn't work, try:
    torclient.ForceRenewProxy() 
    #It may cause timeouts though

Now, you can use 'proxy_socket' just like a normal socket object, and it goes through the proxy! You can also set up a non-proxy socket along side it!:

    import socket
    proxy_socket = proxy_sesison.InitProxy("localhost", 9050, False) # as we declared before
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # normal socket without proxy!
    
    #'proxy_socket' now is literally a socket object!
    
    proxy_socket.connect(("google.com", 80)) #connects through proxy
    s.connect(("google.com", 80)) #connects through normal
    
    proxy_socket.close()
    s.close()

