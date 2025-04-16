import streamlit as st
import math

def estimate_runtime(pipeline, samples, fastq_size_gb, cpus, memory_gb, aligner):
    # Base time estimates per sample (in minutes) under optimal conditions (on 16 cores)
    base_times = {
        "methylseq": {
            "bismark": 90,  # average per sample
            "bwameth": 70
        },
        "rnaseq": {
            "star": 50,
            "hisat2": 40
        }
    }

    baseline_cpu = 16
    baseline_memory = 64  # in GB

    time_per_sample = base_times[pipeline][aligner]
    cpu_factor = baseline_cpu / cpus if cpus > 0 else 1
    mem_factor = max(1.0, baseline_memory / memory_gb)
    size_factor = 1.0 + (fastq_size_gb - 3) * 0.1  

    estimated_time_per_sample = time_per_sample * cpu_factor * mem_factor * size_factor
    total_runtime = estimated_time_per_sample * samples / (cpus / 4)  # assume 4 samples in parallel for 16 CPUs

    return estimated_time_per_sample, total_runtime

st.title("nf-core Pipeline Runtime Estimator")

pipeline = st.selectbox("Pipeline", ["methylseq", "rnaseq"])

aligner_options = {"methylseq": ["bismark", "bwameth"], "rnaseq": ["star", "hisat2"]}
aligner = st.selectbox("Aligner", aligner_options[pipeline])

samples = st.number_input("Number of Samples", min_value=1, step=1)
fastq_size = st.number_input("Average FASTQ File Size per Sample (GB)", min_value=0.1, value=3.0)
cpus = st.number_input("Requested CPUs", min_value=1, value=15)
memory = st.number_input("Requested Memory (GB)", min_value=1, value=120)

if st.button("Estimate Runtime"):
    per_sample, total = estimate_runtime(pipeline, samples, fastq_size, cpus, memory, aligner)

    st.success(f"\nEstimated runtime per sample: {per_sample:.1f} minutes")
    hours, minutes = divmod(total, 60)
    st.info(f"\nEstimated total job runtime: {int(hours)} hours and {int(minutes)} minutes")

    if total > 24 * 60:
        st.warning("Consider running in batches or increasing CPU resources to reduce walltime.")

st.markdown("---")
st.caption("Estimates assume moderate I/O, average pipeline load, and good node availability.")
