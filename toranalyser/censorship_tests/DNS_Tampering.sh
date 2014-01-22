cd ../ooni-probe
sudo ./bin/ooniprobe ooni/nettests/blocking/dnsconsistency.py -T test_inputs/dns_tamper_test_resolvers.txt -f test_inputs/http_host_file.txt
mv report*dns*.yamloo ../censorship_report_files
mv report*dns*.pcap ../censorship_test_capure_pcap

