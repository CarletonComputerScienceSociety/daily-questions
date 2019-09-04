#include <algorithm>
#include <vector>

template <class T> auto move_zeros_to_end(std::vector<T> a) {
    std::sort(a.begin(), a.end(), [](const T& a, const T& b){return !b;});
    return a;
}

