echo "*********************************************************"
echo "This will try to install the dependencies for the project"
echo "*********************************************************"
sudo apt-get install python-setuptools
sudo apt-get install python-dev
sudo easy_install pip
sudo apt-get install git
cd ooni-probe
sudo ./setup-dependencies.sh 
sudo apt-get install git-core python python-pip python-dev build-essential tor tor-geoipdb tcpdump python-geoip python-docutils python-ipaddr python-scapy python-pyrex libdumbnet python-dumbnet python-libpcap python-pypcap pcapy python-dnspython python-virtualenv virtualenvwrapper
sudo pip install virtualenv
wget https://libdnet.googlecode.com/files/libdnet-1.12.tgz
tar xzf libdnet-1.12.tgz
cd libdnet-1.12
./configure  && make
cd python/
sudo python setup.py install
cd ../../ && rm -rf libdnet-1.12*
sudo apt-get install libpcap-dev
git clone https://github.com/hellais/pypcap
cd pypcap/
sudo pip install pyrex
sudo python setup.py install
cd ../ && rm -rf pypcap
sudo pip install twisted pyyaml pypcap scapy  txsocksx pygeoip parsley docutils ipaddr Pyrex
sudo pip install pyCrypto
sudo pip install BeautifulSoup
sudo pip install paramiko
sudo python setup.py install
cd ../
sudo cp ooniprobe.conf ~/.ooni
cd ~/.ooni
sudo mkdir data
cd -
sudo cp -r ooni-probe/data/* ~/.ooni/


