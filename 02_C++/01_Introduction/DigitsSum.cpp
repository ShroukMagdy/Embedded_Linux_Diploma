#include <iostream>
#include <string>

int main()
{
    int num,sum;
    std::cout << "Enter an integer : ";
    std::cin >> num;

    std::string numStr = std::to_string(num);

    for(char digitChar : numStr)
    {
        int digit = digitChar - '0';
        sum += digit;
    }
    std::cout << "Sum of digits of "<<num<<" is : "<<sum<<std::endl;
    
    return 0;
}