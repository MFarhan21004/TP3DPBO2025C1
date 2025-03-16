#pragma once
#include <iostream>
#include <string>
#include "Komponen.cpp"


using namespace std;


class Cpu : public Komponen
{
private:
    int jumlahCore;
    float kecepatanGHz;
public:
    Cpu()
    {


    }


    Cpu(int jumlahCore, float kecepatanGHz, string merk, string nama) : Komponen(merk, nama)
    {
        this->jumlahCore = jumlahCore;
        this->kecepatanGHz = kecepatanGHz;
    }


    void setJumlahCore(int jumlahCore)
    {
        this->jumlahCore = jumlahCore;
    }


    void setKecepatanGHz(float kecepatanGHz)
    {
        this->kecepatanGHz = kecepatanGHz;
    }


    int getJumlahCore()
    {
        return this->jumlahCore;
    }


    float getKecepatanGHz()
    {
        return this->kecepatanGHz;
    }


    ~Cpu()
    {


    }
};
