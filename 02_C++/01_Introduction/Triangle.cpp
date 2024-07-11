#include <iostream>
#include <cmath>

int main()
{
    int side1,side2,side3;
    std::cout <<"side1 : ";
    std::cin >>side1;
    side1=pow(side1,2);
    std::cout <<"side2 : ";
    std::cin >>side2;
    side2=pow(side2,2);
    std::cout <<"side3 : ";
    std::cin >>side3;
    side3=pow(side3,2);
    
    if((side1+side2 == side3)|(side1+side3 == side2)|(side2+side3 == side1))
    {
        std::cout << "Right Angle triangle";
    }
    else
    {
        std::cout << "Not Right Angle triangle";
    }
    
    return 0;
}