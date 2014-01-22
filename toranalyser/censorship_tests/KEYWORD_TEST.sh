cd ../ooni-probe
sudo ./bin/ooniprobe --no-collector ../censorship_tests/keyword_test.py -f test_inputs/keyword_filtering_file.txt
mv report*.yamloo ../censorship_report_files
mv report*.pcap ../censorship_test_capure_pcap
