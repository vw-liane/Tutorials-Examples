# include <iostream>

int main ()
{
  int sum = 0, num = 0;
  // while exists another number from standard-input
  //    stores in <num>
  while (std::cin >> num)  // keeps going until <end-of-file>
  {                        //   or invalid input (not an int)
         //  <istream> invalid state will cause false condition 
    sum += num;
  }
  std::cout << "Sum is: " << sum << std::endl;

  // unknown initial value
  int unitialized;
  std::cout << "\nSurprise value!\n" << unitialized << std::endl;
  return 0;
}