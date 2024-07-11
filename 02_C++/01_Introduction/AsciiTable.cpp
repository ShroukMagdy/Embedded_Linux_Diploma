#include <iostream>
#include <iomanip>

int main()
{
    std::cout << "ASCII Code Table" << std::endl;
    std::cout << "*---------*---------*" << std::endl;
    for (unsigned char i = 0;i<=255;i++)
    {
        std::cout << "|"<< std::setw(5) << i << std::setw(5) << "|"<< std::setw(5) << static_cast<int>(i) << std::setw(5)<< "|" << std::endl;
    }
    std::cout << "*---------*---------*" << std::endl;

    return 0;
}