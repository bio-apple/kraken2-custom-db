FROM ubuntu:latest
RUN apt-get update && apt-get install -y --no-install-recommends  libcurl4-openssl-dev \
    build-essential wget curl ca-certificates bzip2 gnupg git libssl-dev libffi-dev libz-dev libbz2-dev && rm -rf /var/lib/apt/lists/* && \
    mkdir -p /ref/ /script/ /raw_data/ /outdir/ && \
    wget -q -O /miniforge.sh https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Linux-x86_64.sh && \
    bash /miniforge.sh -b -p /opt/conda && rm /miniforge.sh && \
    /opt/conda/bin/conda install --channel conda-forge --channel bioconda --channel defaults kraken2 krakentools krona bracken taxonkit bioawk && \
    curl -sSL https://ftp.ncbi.nlm.nih.gov/pub/datasets/command-line/v2/linux-amd64/datasets -o /opt/conda/bin/datasets && chmod +x /opt/conda/bin/datasets