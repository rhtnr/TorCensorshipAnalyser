cd ../ooni-probe
sudo ./bin/ooniprobe --no-collector ooni/nettests/blocking/http_requests.py -u http://torproject.org
sudo ./bin/ooniprobe --no-collector ooni/nettests/blocking/http_requests.py -u http://bridges.torproject.org
mv report*.yamloo ../censorship_report_files
mv report*.pcap ../censorship_test_capure_pcap
