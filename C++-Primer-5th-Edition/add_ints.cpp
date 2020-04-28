#include <iostream> // refers to a header
/*
 *try ILLEGAL nesting /**/
 *
 *
*/
int main() 
{
  int var1 = 0, var2 = 0;

  std::cout << "Enter two numbers: " << std::endl;
  std::cin >> var1 >> var2;

  std::cout << "The sum of " << var1 << " and " << var2
            << " is " << (var1 + var2) << std::endl;

  return 0;
}