cd ../ooni-probe
sudo ./bin/ooniprobe --no-collector ../censorship_tests/bridge_tcp.py
mv report*.yamloo ../censorship_report_files
mv report*.pcap ../censorship_test_capure_pcap
