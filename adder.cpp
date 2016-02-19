// Example program
#include <iostream>
#include <string>

int main()
{
    unsigned long long number = 1;
    unsigned long long total = 0;
    unsigned long long end = 1000000000; // 1 Billion
        
    while(number <= end)
    {
        total += number;
        ++number;
    };
                           
    std::cout << "Total: " << total << std::endl;
    return 0;
}

