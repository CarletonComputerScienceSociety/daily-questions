#include <iostream>
#include <vector>

int arr[] = { 1, 4, 2, 7, 10, 8 };

void main()
{
	std::vector<int> vec;
	size_t size = (sizeof(arr) / sizeof(arr[0]));

	for (size_t i = 0; i < size; i++) {
		vec.push_back(arr[i]);
	}

	while (!(vec.size() == 1)) {
		if (vec[1] > vec[0])
			vec.erase(vec.begin());
		else
			vec.erase(vec.begin() + 1);
	}

	int largestNumber = vec[0];
	std::cout << largestNumber;
}