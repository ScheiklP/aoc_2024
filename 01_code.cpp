#include <algorithm>
#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <unordered_map>


int main() {
    const std::string filename = "01_input.txt";

    std::ifstream file(filename, std::ios::in);
    if (!file.is_open()) {
        std::cerr << "Failed to open the file." << std::endl;
        return 1;
    }

    std::size_t line_count = std::count(
        std::istreambuf_iterator<char>(file),
        std::istreambuf_iterator<char>(),
        '\n'
    );
    file.close();

    std::vector<int> first_list;
    std::vector<int> second_list;

    first_list.reserve(line_count);
    second_list.reserve(line_count);

    file.open(filename, std::ios::in);
    if (!file.is_open()) {
        std::cerr << "Failed to open the file." << std::endl;
        return 1;
    }

    std::string line;
    while (std::getline(file, line)) {
        std::istringstream stream(line); // Create a stream for the line

        int first_number;
        int second_number;

        stream >> first_number;
        stream >> second_number;
        first_list.push_back(first_number);
        second_list.push_back(second_number);
    }
    file.close();

    std::ranges::sort(first_list);
    std::ranges::sort(second_list);

    std::unordered_map<int, int> second_list_map;

    int total_distance = 0;
    for (int i = 0; i < line_count; i++) {
        second_list_map[second_list[i]]++;
        int distance = std::abs(first_list[i] - second_list[i]);
        total_distance += distance;
    }

    int total_score = 0;
    for (int num : first_list) {
        total_score += num * second_list_map[num];
    }

    std::cout << "First part: " << total_distance << std::endl;
    std::cout << "Second part: " << total_score << std::endl;

    return 0;
}
