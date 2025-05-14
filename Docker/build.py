import os,re,sys
import argparse
import subprocess

docker="krakendb:latest"

def download_fa(taxid,outdir,prefix):


cmd=(f'docker run -v {os.getcwd()}:/ref/ docker sh -c \'export PATH=/opt/conda/bin/:$PATH && '
     f'kraken2-build --db /ref/ --download-taxonomy && kraken2-build --add-to-library /ref/%s_library.fna --db /database/ --threads 48\'')