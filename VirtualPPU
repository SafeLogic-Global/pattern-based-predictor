"""
================================================================================
PROJECT: PHOTONIC PROCESSING UNIT (PPU) - VIRTUAL CHIP EMULATOR & BRIDGE
================================================================================
Status:  Version 1.2 (Functional Emulator with Visual Output)
Urheber: 0009-0003-9088-2341
Lizenz:  Apache License 2.0

EIN VIRTUELLER CHIP MUSS DREI DINGE KÖNNEN (ÜBER DAS ÜBERSETZEN HINAUS):

1. INTERFERENZ-SIMULATION: 
   Er muss zwei Lichtmuster nehmen und sie „übereinanderlegen“.
2. SENSOR-LOGIK: 
   Er muss simulieren, wie der CMOS-Sensor die Helligkeit an den 9 Punkten misst.
3. ZUSTANDS-ÜBERWACHUNG: 
   Er muss erkennen, wenn ein Muster „ungültig“ ist.
================================================================================
"""

class VirtualPPU:
    def __init__(self):
        self.grid_state = 0b000000000
        
    def simulate_interference(self, pattern_a, pattern_b):
        self.grid_state = pattern_a | pattern_b
        return self.grid_state

    def visualize_grid(self):
        """Erzeugt eine visuelle Darstellung des 3x3 Gitters in der Konsole."""
        grid_visual = "\n   AKTUELLER CHIP-ZUSTAND (3x3):\n"
        grid_visual += "   +---+---+---+\n"
        
        # Wir gehen die 9 Bits durch und zeichnen das Gitter
        binary_str = bin(self.grid_state)[2:].zfill(9)[::-1]
        for i in range(0, 9, 3):
            row = binary_str[i:i+3]
            grid_visual += "   | " + " | ".join(['*' if b == '1' else ' ' for b in row]) + " |\n"
            grid_visual += "   +---+---+---+\n"
        return grid_visual

class GPAPatternCompiler:
    def compile_to_laser_pattern(self, number):
        if 1 <= number <= 9:
            return 1 << (number - 1)
        return 0

def run_emulator_demo():
    print("--- PPU VIRTUAL CHIP VISUALIZER ---")
    compiler = GPAPatternCompiler()
    ppu = VirtualPPU()
    
    # Rechnung: 1 + 5 + 9 (Diagonal)
    vals = [1, 5, 9]
    combined_pattern = 0
    
    for v in vals:
        combined_pattern = ppu.simulate_interference(combined_pattern, compiler.compile_to_laser_pattern(v))
    
    # Ausgabe der Grafik
    print(ppu.visualize_grid())
    print(f"Ergebnis-Muster: {bin(combined_pattern)}")
    print("Die '*' Symbole stellen die aktiven Lichtpunkte im Chip dar.")

if __name__ == "__main__":
    run_emulator_demo()
