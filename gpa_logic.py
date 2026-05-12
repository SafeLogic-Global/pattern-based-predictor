import math

# --- TEIL 1: DIE GEOMETRISCHE GITTER-LOGIK ---
def erstelle_gitter_muster(wert):
    """Erstellt die 3x3 Bitmaske für einen Wert."""
    # Werte der Felder: 1, 2, 4 (oben), 8, 16, 32 (mitte), 64, 128, 256 (unten)
    bit_werte = [1, 2, 4, 8, 16, 32, 64, 128, 256]
    return ["[X]" if int(wert) & v else "[ ]" for v in bit_werte]

def zeige_finanz_gitter(euro_wert):
    """Stellt den Betrag visuell in zwei 3x3 Blöcken dar."""
    euro = int(euro_wert)
    # Cent-Bereich exakt berechnen
    cent = int(round((euro_wert - euro) * 100))
    
    g_euro = erstelle_gitter_muster(euro)
    g_cent = erstelle_gitter_muster(cent)
    
    print(f"\n--- GPA SICHERHEITS-MODUS: {euro_wert:.2f} € ---")
    print("  [ EURO-BLOCK ]       [ CENT-BLOCK ]")
    for i in range(0, 9, 3):
        e_reihe = " ".join(g_euro[i:i+3])
        c_reihe = " ".join(g_cent[i:i+3])
        print(f"   {e_reihe}             {c_reihe}")
    print("-" * 40)

# --- TEIL 2: DER HYBRID-PREDICTOR ---
def sichere_transaktion(betrag_a, betrag_b, operation="+"):
    """
    Prüft auf Fließkommafehler und schaltet bei Bedarf 
    auf das geometrische Gitter um.
    """
    if operation == "+":
        # Normale Hardware-Rechnung
        ergebnis_standard = betrag_a + betrag_b
        # Exakte Ganzzahl-Prüfung (Simuliert die Gitter-Präzision)
        ergebnis_exakt = (int(round(betrag_a * 100)) + int(round(betrag_b * 100))) / 100
    
    elif operation == "*":
        ergebnis_standard = betrag_a * betrag_b
        ergebnis_exakt = (int(round(betrag_a * 100)) * betrag_b) / 100

    # PREDICTOR CHECK
    if not math.isclose(ergebnis_standard, ergebnis_exakt, rel_tol=1e-15):
        print(f"⚠️  ALARM: Numerischer Fehler bei Standard-CPU erkannt!")
        print(f"CPU-Wert: {ergebnis_standard} vs. Exakt: {ergebnis_exakt}")
        zeige_finanz_gitter(ergebnis_exakt)
        return ergebnis_exakt
    else:
        print(f"✅ Transaktion stabil: {ergebnis_standard:.2f} €")
        return ergebnis_standard

# --- TEIL 3: DEMO-SZENARIO (TRADING) ---
if __name__ == "__main__":
    print("=== GPA SYSTEM START (Geometric Pattern Arithmetic) ===")
    
    # Beispiel 1: Die klassische 0.1 + 0.2 Falle
    print("\nSzenario 1: Kleine Währungsbeträge addieren...")
    sichere_transaktion(0.10, 0.20)
    
    # Beispiel 2: Zins-Berechnung
    print("\nSzenario 2: Zinsberechnung (Multiplikation)...")
    sichere_transaktion(100.00, 0.025, operation="*") # 2.5% von 100€

    # Beispiel 3: Stabile Rechnung
    print("\nSzenario 3: Einfache stabile Transaktion...")
    sichere_transaktion(50.00, 25.00)
    
    print("\n=== SYSTEMBEREIT FÜR WEITERE BERECHNUNGEN ===")
