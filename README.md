# Runtime Checker
Runtime checker (for EpiGastroDRG purposes only)

This is a simple **Streamlit web app** that helps you estimate how long your `nf-core/methylseq` or `nf-core/rnaseq` analysis might take when running on the RCSI's HPC cluster managed by SLURM. It is designed to assist in planning and communicating expected runtimes, especially useful when submitting long jobs or coordinating reserved cluster time.

# Features
- Check rnaseq or methylseq (nf-core pipelines)
- Select aligner (bismark, bwameth, hisat2, star)
- Input sample count, avg. FASTQ file size, CPU and memory requested
- Obtain a rough estimate (~15-20% error margin) for Runtime per sample, Total job runtime and Warnings for long runtimes (>24hs).

# Requirements
- Just have Python and Streamlit installed:
```bash
pip install streamlit
```

# Running the App
1. Save the script to a file, e.g., `runtime_estimator.py`
2. Run with:

```bash
streamlit run runtime_estimator.py
```

## How to Use

### 1. **Select the pipeline**
Choose between:
- `methylseq` (e.g., for bisulfite-treated samples)
- `rnaseq` (for expression studies)

### 2. **Pick the aligner**
Depending on the pipeline, choose an aligner:
- `methylseq`: `bismark` or `bwameth`
- `rnaseq`: `star` or `hisat2`

### 3. **Input your sample details**
- **Number of Samples**: Total number of samples (not FASTQ files). For **paired-end**, still count each as **one sample**.
- **Average FASTQ File Size (GB)**: Combined size of R1 + R2 if paired-end. E.g., if R1 and R2 are ~400 MB each, input `0.8` GB.

### 4. **Enter SLURM Job Parameters**
- **Requested CPUs**: e.g., `15` (value used with `--cpus-per-task`)
- **Memory (GB)**: Total memory allocated to the job

## 📌 Notes and Assumptions
- Estimates are derived from real-world job runtimes on RCSI's HPC cluster
- Assumes up to 4 samples can be processed in parallel using 15–16 cores
- Results can vary slightly based on:
  - I/O performance
  - Temporary cluster load
  - Pipeline version and configuration

## 🧑‍💻 Author
Developed by [Alejandra Rodríguez](https://github.com/AlejRSosa) for the RCSI Epigenomics & Gastrointestinal Disease Research Group.

## 📜 License
MIT License
