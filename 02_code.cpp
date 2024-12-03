#include <algorithm>
#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>

bool valid_differences(const std::vector<int>& differences) {
    const bool all_positive = std::ranges::all_of(differences, [](const int difference){return difference > 0;});
    const bool all_negative = std::ranges::all_of(differences, [](const int difference){return difference < 0;});
    const bool all_in_range = std::ranges::all_of(differences, [](const int difference){return abs(difference) < 4;});

    return (all_positive || all_negative) && all_in_range;
}

int main() {
    const std::string filename = "02_input.txt";

    std::ifstream file(filename, std::ios::in);
    if (!file.is_open()) {
        std::cerr << "Failed to open the file." << std::endl;
        return 1;
    }

    std::string line;
    int num_safe_lines_part_1 = 0;
    int num_safe_lines_part_2 = 0;

    while (std::getline(file, line)) {
        std::istringstream stream(line);
        std::vector<int> numbers;
        std::vector<int> differences;

        int number;
        while(stream >> number) {
            if (!numbers.empty()) {
                differences.push_back(number - numbers.back());
            }
            numbers.push_back(number);
        }

        if (valid_differences(differences)){
            num_safe_lines_part_1++;
            num_safe_lines_part_2++;
        } else {
            for (int i = 0; i < numbers.size(); i++) {
                std::vector<int> sub_numbers;
                std::vector<int> sub_differences;
                std::cout << std::endl;
                for (int j = 0; j < numbers.size(); j++) {
                    if (j != i) {
                        sub_numbers.push_back(numbers[j]);
                    }
                }
                for (int j = 0; j < sub_numbers.size() - 1; j++) {
                    sub_differences.push_back(sub_numbers[j+1] - sub_numbers[j]);
                }

                if (valid_differences(sub_differences)) {
                    num_safe_lines_part_2++;
                    break;
                }
            }
        }
    }
    file.close();

    std::cout << "First part:" << num_safe_lines_part_1 << std::endl;
    std::cout << "Second part:" << num_safe_lines_part_2 << std::endl;

    return 0;
}
