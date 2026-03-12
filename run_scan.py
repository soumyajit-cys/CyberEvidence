from modules.evidence_collector import collect_files
from modules.file_forensics import analyze_file
from modules.metadata_extractor import extract_metadata
from modules.log_analyzer import analyze_logs
from modules.network_analyzer import analyze_pcap
from reports.report_generator import generate_report

print("Starting Digital Forensics Investigation")

files = collect_files()

print("Files collected:",len(files))

for f in files:

    analyze_file(f)
    extract_metadata(f)

print("File and metadata analysis completed")

analyze_logs()
print("Log analysis completed")

analyze_pcap()
print("Network analysis completed")

generate_report()

print("Investigation report generated")