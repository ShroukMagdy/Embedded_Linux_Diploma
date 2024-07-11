#include <iostream>
#include <bitset>

int main()
{
    //binary representation
    int num;
    std::cout << "Enter a decimal number : ";
    std::cin >> num;
    std::bitset<8> Binarynum(num);
    std::cout << "Binary representation "<<Binarynum<<std::endl;
    
    //decimal representation
    std::cout << "Enter a binary number : ";
    std::cin >> Binarynum;
    std::cout << "Decimal representation "<<Binarynum.to_ulong()<<std::endl;
    
    return 0;
}