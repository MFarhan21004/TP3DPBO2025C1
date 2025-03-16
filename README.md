# Janji
Saya Muhammad Farhan dengan NIM 2309323 mengerjakan Tugas Praktikum 3 dalam mata kuliah Desain dan Pemrograman Berorientasi Objek untuk keberkahanNya maka saya tidak melakukan kecurangan seperti yang telah dispesifikasikan. Aamiin.

# Diagram
![Image](https://github.com/user-attachments/assets/3ee48ad9-d015-4e06-9705-291bffd9a747)

# Desain Program
Diagram ini terdiri dari 5 kelas utama yang berhubungan satu sama lain:

### 1. Komponen (Super Class)

Kelas ini adalah kelas induk (parent class) yang memiliki atribut umum bagi semua komponen hardware, yaitu:

nama → Nama komponen (misalnya, "Core i7", "HyperX", dll.)

merek → Merek komponen (misalnya, "Intel", "Corsair", dll.)

Memiliki setter dan getter untuk mengakses dan mengubah data.

Kelas ini akan diwarisi oleh Cpu, Ram, dan Harddrive.

### 2. Cpu (Subclass dari Komponen)

Menambahkan atribut spesifik untuk CPU:

jumlahCore → Jumlah core pada CPU (misalnya, 8 core)

kecepatanGHz → Kecepatan clock CPU dalam GHz (misalnya, 3.4 GHz)

Memiliki setter dan getter.

### 3. Ram (Subclass dari Komponen)

Menambahkan atribut khusus RAM:

kapasitasGB → Kapasitas RAM dalam GB (misalnya, 16GB)

ddr → Jenis DDR RAM (misalnya, DDR4, DDR5)

Memiliki setter dan getter.

### 4. Harddrive (Subclass dari Komponen)

Menambahkan atribut untuk penyimpanan:

kapasitasGB → Kapasitas penyimpanan dalam GB (misalnya, 1024GB)

tipeDrive → Jenis hard drive (SSD atau HDD)

Memiliki setter dan getter.

### 5. Komputer

Kelas ini merepresentasikan sebuah komputer yang memiliki beberapa komponen:

nama → Nama komputer (misalnya, "PC Abdul")

cpu → Objek dari kelas Cpu (setiap komputer memiliki 1 CPU)

ramList → List (array) objek RAM (komputer bisa memiliki lebih dari 1 RAM)

harddrive → Objek dari kelas Harddrive (setiap komputer memiliki 1 Harddrive)

Memiliki setter dan getter.

# Hubungan Antar Kelas
### Inheritance (Pewarisan)

- Cpu, Ram, dan Harddrive mewarisi Komponen karena mereka memiliki atribut umum yang sama.

### Composite

- Komputer memiliki 1 CPU → Relasi 1 ke 1 dengan Cpu

- Komputer memiliki 1 Harddrive → Relasi 1 ke 1 dengan Harddrive

- Komputer memiliki banyak RAM → Relasi 1 ke banyak dengan Ram (ditunjukkan dengan ramList berupa array)

# Alur Program
1. Objek CPU, RAM, dan Harddrive dibuat terlebih dahulu.

2. Membuat objek komputer

3. Objek Komputer dibuat dengan memasukkan objek CPU, array RAM, dan objek Harddrive.

4. Menampilkan informasi dari setiap komputer dan menampilkan detail CPU, daftar RAM, dan Harddrive.
