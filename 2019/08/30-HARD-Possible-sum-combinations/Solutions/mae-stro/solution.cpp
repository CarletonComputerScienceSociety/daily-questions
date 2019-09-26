#include <string>
#include <iostream>
#include <vector>
using namespace std;

// build a binary tree v.size() deep
// each leaf in tree represents a combination
// left child means its parent node is not part of combination
// right child means its parent node is part of the combination
void print_combinations(
    vector<int> const &data, // all elements
    size_t const target,     // The goal to sum too
    string state = "",       // Current state (list of all parents values)
    size_t const depth = 0,  // depth in tree, max is size of data
    size_t sum = 0)
{
  if (depth >= data.size())
    return;
  if (sum == target)
  {
    for (auto &&c : state)
      cout << c << " ";
    cout << "\n";
  }
  else if (sum > target)
    return;
  print_combinations(data, target, state, depth + 1, sum);
  state += to_string(data[depth]);
  print_combinations(data, target, state, depth + 1, sum + data[depth]);
}

int main()
{
  vector<int> v{1, 2, 3, 5, 7};
  int const sum{8};
  print_combinations(v, sum);
}