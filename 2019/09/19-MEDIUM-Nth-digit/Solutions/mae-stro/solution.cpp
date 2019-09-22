#include <iostream>
#include <cmath>
#include <boost/math/special_functions/lambert_w.hpp>

// Implementation details in this paper: https://artemlos.net/docs/2014/01/MathExploration.pdf

using namespace std;

// Artem’s method - calculated the number of digits in interval [1,a]
constexpr long double artemG(long double a)
{
  return (a - 1LL) * pow(10LL, a) + ((pow(10LL, a - 1LL) - 1LL) / 9.0) * 8.0 * 10.0 + 9LL;
}

// Not defined for n = 1
long double inverseG(int n)
{
  const auto log5p2 = log(5.0L) + log(2.0L);
  const auto lambertFx = boost::math::lambert_w0((9.0L * n - 1) * log5p2 / (9 * pow(10.0L, 1.0L / 9.0L)));
  return (9.0L * lambertFx + log5p2) / (9.0L * log5p2);
}

void printDigit(int index)
{
  if (index == 1)
  {
    cout << "index: 1 output: 1" << endl;
    return;
  }

  auto a{inverseG(index)};
  int aCeil{static_cast<int>(ceil(a))};
  auto gOfACeil{artemG(aCeil)};
  auto gOfA{artemG(a)};

  // 4.3 from paper
  int p = pow(10.0L, aCeil) - 1.0L - floor((gOfACeil - gOfA) / aCeil);
  int r = fmod(gOfACeil - gOfA, aCeil);

  auto output{to_string(p)};
  cout << "index: " << index << " output: " << output[output.size() - 1 - r] << endl;
}

int main()
{
  for (int i = 1; i < 100; ++i)
    printDigit(i);

  // Example in paper
  printDigit(206788);
}