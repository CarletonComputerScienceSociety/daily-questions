#include <iostream>
#include <vector>

int arr[] = { 0, 1, 0, 3, 12 };

void main()
{
	std::vector<int> vec;

	for (int i : arr) {
		vec.push_back(i);
	}

	for (int i = 0; i < vec.size(); i++) {
		if (vec[i] == 0) {
			vec.erase(vec.begin() + i);
			vec.push_back(0);
		}
	}

	for (int i : vec) {
		std::cout << i;
	}
}