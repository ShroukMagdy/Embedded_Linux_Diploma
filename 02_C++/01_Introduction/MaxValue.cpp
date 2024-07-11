#include <iostream>
#include <algorithm>

int main()
{
    int num1,num2,num3,max;
    std::cout <<"num1 : ";
    std::cin >>num1;
    std::cout <<"num2 : ";
    std::cin >>num2;
    std::cout <<"num3 : ";
    std::cin >>num3;
    
    max = std::max(num1,num2);
    max = std::max(max,num3);
    
    std::cout << "Max. no. is "<<max;

    return 0;
}