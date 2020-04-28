#include <iostream> // refers to a header

int main() 
{
  // WHILE LOOP
  int sum = 0, num = 1;
  while (num <= 10)
  {
    sum += num;  // assign (sum+num) to sum
    ++num;       // increments num
  }
  std::cout << "First Loop:" << std::endl
            << "Sum of 1 to 10 inclusive is "
            << sum << "." << std::endl;

  // FOR LOOP
  int sum2 = 0;
  for (int num = 1; num <= 10; ++num)
  {
    sum2 += num;
  }  
  std::cout << "\nSecond Loop:" << std::endl
            << "Sum of 1 to 10 inclusive is "
            << sum2 << "." << std::endl;
  return 0;
}