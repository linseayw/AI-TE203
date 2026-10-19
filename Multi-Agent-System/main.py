#!/usr/bin/env python3
import os
import sys

from praval import agent, chat, broadcast, start_agents, get_reef


# ---------------------------------------------------------------
# Konfigurasi
# ---------------------------------------------------------------
MODEL_NAME = "gemini-2.0-flash"   # model gratis & cepat
TOPIC = "sejarah kopi di Indonesia"
OUTPUT_FILE = "hasil_tugas.txt"


# ---------------------------------------------------------------
# Agen 1: Researcher
# ---------------------------------------------------------------
@agent("researcher", responds_to=["research_request"])
def researcher(spore):
    """Meneliti topik, menghasilkan 3 fakta, lalu menyiarkan ke Writer."""
    topic = spore.knowledge.get("topic", "unknown")
    print(f"\n[Researcher] Mulai meneliti: {topic}")

    result = chat(
        f"Berikan 3 fakta menarik dan akurat tentang: {topic}. "
        f"Gunakan format daftar bernomor.",
        provider="gemini",
        model=MODEL_NAME,
    )
    print(f"[Researcher] Fakta yang ditemukan:\n{result}")

    broadcast({
        "type": "research_complete",
        "topic": topic,
        "findings": result,
    })
    return {"status": "research_complete"}


# ---------------------------------------------------------------
# Agen 2: Writer
# ---------------------------------------------------------------
@agent("writer", responds_to=["research_complete"])
def writer(spore):
    """Menerima fakta riset, menulis paragraf, simpan ke file."""
    findings = spore.knowledge.get("findings", "")
    topic = spore.knowledge.get("topic", "unknown")
    print(f"\n[Writer] Menerima hasil riset tentang: {topic}")

    article = chat(
        f"Tulis satu paragraf ringkas (80-120 kata) dan menarik tentang {topic} "
        f"berdasarkan fakta berikut:\n{findings}",
        provider="gemini",
        model=MODEL_NAME,
    )

    print(f"\n[Writer] Artikel yang dihasilkan:\n{'-' * 40}")
    print(article)
    print("-" * 40)

    try:
        with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
            f.write(f"Topik: {topic}\n\n")
            f.write(f"=== Fakta Riset ===\n{findings}\n\n")
            f.write(f"=== Artikel Final ===\n{article}\n")
        print(f"\n[Writer] Hasil disimpan ke: {OUTPUT_FILE}")
    except OSError as e:
        print(f"\n[Writer] Gagal menyimpan file: {e}")

    return {"article": article}


# ---------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------
def main():
    if not os.getenv("GEMINI_API_KEY"):
        print("Error: GEMINI_API_KEY belum di-set.")
        print("  Windows PowerShell : $env:GEMINI_API_KEY=\"api-key-kamu\"")
        print("  macOS / Linux      : export GEMINI_API_KEY=\"api-key-kamu\"")
        sys.exit(1)

    print("=" * 55)
    print(" Sistem Multi-Agent Tugas Mata Kuliah (Gemini Gratis)")
    print("=" * 55)
    print(f" Model  : {MODEL_NAME}")
    print(f" Topik  : {TOPIC}")

    start_agents(
        researcher,
        writer,
        initial_data={
            "type": "research_request",
            "topic": TOPIC,
        },
    )

    get_reef().wait_for_completion()
    get_reef().shutdown()
    print("\n[Sistem] Semua agen selesai diproses.")


if __name__ == "__main__":
    main()
