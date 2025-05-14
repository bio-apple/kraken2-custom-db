import os,re,sys
import argparse
import subprocess

docker="krakendb:latest"

def download_fa(species_list_file, outdir):
    os.makedirs(outdir, exist_ok=True)
    with open(species_list_file, "r") as infile, open(f"{outdir}/download_genome.sh", "w") as shell:
        for line in infile:
            line = line.strip()
            if line:
                shell.write(f"docker run --rm -v {os.path.abspath(outdir)}:/outdir {docker} /opt/conda/bin/datasets download genome taxon {line} --filename /outdir/{line}.zip\n")
    subprocess.check_call(f'sh {outdir}/download_genome.sh',shell=True)

cmd=(f'docker run --rm -v {os.getcwd()}:/ref/ docker sh -c \'export PATH=/opt/conda/bin/:$PATH && '
     f'kraken2-build --db /ref/ --download-taxonomy && kraken2-build --add-to-library /ref/%s_library.fna --db /database/ --threads 48\'')