cd ../ooni-probe
sudo ./bin/ooniprobe --no-collector ../censorship_tests/tor_website_dns.py
mv report*.yamloo ../censorship_report_files
mv report*.pcap ../censorship_test_capure_pcap
