#include <bits/stdc++.h>
#include "Cpu.cpp"
#include "Ram.cpp"
#include "Harddrive.cpp"
#include "Komputer.cpp"

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    // Membuat beberapa objek CPU
    Cpu cpu1(10, 4.2, "Intel", "Core i9");
    Cpu cpu2(6, 3.7, "AMD", "Ryzen 5 5600X");
    Cpu cpu3(12, 3.9, "Intel", "Xeon W-2295");

    // Membuat beberapa objek RAM
    Ram ram1(16, "DDR4", "Kingston", "HyperX Fury");
    Ram ram2(8, "DDR3", "Crucial", "Ballistix");
    Ram ram3(32, "DDR5", "Corsair", "Dominator Platinum");
    Ram ram4(16, "DDR5", "G.Skill", "Trident Z");
    Ram ram5(8, "DDR4", "ADATA", "XPG");
    Ram ram6(32, "DDR5", "Samsung", "EVO RAM");

    // Membuat beberapa objek Harddrive
    Harddrive hdd1(512, "SSD", "Western Digital", "Black SN850");
    Harddrive hdd2(1000, "HDD", "Toshiba", "X300");
    Harddrive hdd3(2000, "SSD", "Samsung", "970 EVO Plus");

    // Membuat array of object Komputer
    Komputer komputerArray[3] = {
        Komputer("PC Rizki", cpu1, {ram1, ram2}, hdd1),
        Komputer("PC Siti", cpu2, {ram3}, hdd2),
        Komputer("PC Tono", cpu3, {ram4, ram5}, hdd3)
    };

    // Menambahkan RAM tambahan ke masing-masing komputer
    komputerArray[0].addRam(Ram(8, "DDR4", "G.Skill", "Ripjaws V"));
    komputerArray[1].addRam(Ram(16, "DDR5", "Kingston", "Fury Beast"));
    komputerArray[2].addRam(Ram(32, "DDR5", "Corsair", "Vengeance RGB"));

    // Menampilkan informasi komputer
    for (int i = 0; i < 3; i++) {
        cout << "======================================\n";
        cout << "Informasi Komputer " << i + 1 << ":" << endl;
        cout << "Nama      : " << komputerArray[i].getNama() << endl;
        cout << "Cpu       : " << komputerArray[i].getCpu().getMerk() << ' ' 
             << komputerArray[i].getCpu().getNama() << " (" 
             << komputerArray[i].getCpu().getJumlahCore() << " Core) " 
             << "~" << komputerArray[i].getCpu().getKecepatanGHz() << "GHz" << endl;

        for (Ram& ram : komputerArray[i].getRamList()) {
            cout << "Ram       : ";
            cout << ram.getMerk() << ' ' << ram.getNama() << " (" 
                 << ram.getKapasitasGB() << " GB) " 
                 << ram.getDdr() << endl;
        }

        cout << "Harddrive : " << komputerArray[i].getHarddrive().getTipeDrive() << ' ' 
             << komputerArray[i].getHarddrive().getMerk() << ' ' 
             << komputerArray[i].getHarddrive().getNama() << " (" 
             << komputerArray[i].getHarddrive().getKapasitasGB() << " GB) " << endl;
    }

    return 0;
}
