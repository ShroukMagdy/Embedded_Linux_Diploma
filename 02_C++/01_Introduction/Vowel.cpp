#include <iostream>
#include <string>

int main()
{
    const std::string vowels = "aeiou";
    char letter;
    std::cout<<"Enter charater : ";
    std::cin>>letter;
    
    if(vowels.find(letter)<vowels.length())
    {
        std::cout<<"It is a vowel";
    }
    else
    {
        std::cout<<"It is Not a vowel";
    }
    
    return 0;
}
