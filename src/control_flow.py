from src.hamming import HammingDistance
from src.jaccard import JaccardSimilarity
from src.tanimoto import TSimilarity
from src.input_output import extract_data, write_output


def run():
    """Runs the string comparison process."""

    print("📥 Extracting input data...")
    data = extract_data()
    print(f"✅ {len(data)} string pairs loaded.")

    print("⚙️ Initializing similarity metrics...")
    hamming = HammingDistance()
    jaccard = JaccardSimilarity()
    tanimoto = TSimilarity()
    print("✅ Hamming, Jaccard and Tanimoto initialized.")

    results = []

    print("🔄 Calculating similarities...")

    for s1, s2 in data:
        h = hamming.calculate(s1, s2)
        j = jaccard.calculate(s1, s2)
        t = tanimoto.calculate(s1, s2)

        results.append((s1, s2, h, j, t))

    print("💾 Writing results to output.csv...")
    write_output(results)

    print("🎉 Output generated successfully!")