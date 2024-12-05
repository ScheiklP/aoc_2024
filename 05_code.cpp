#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>

bool check_subset_for_violation(const std::vector<int> &numbers, const std::vector<int> &rules) {
    for (const int number : numbers) {
        for (const int rule : rules) {
            if (number == rule) {
                return true;
            }
        }
    }
    return false;
}


bool update_is_valid(const std::vector<std::pair<int, int>> &rules, const std::vector<int> &update) {
    bool is_valid = true;

    for (int i = 0; i < update.size(); i++) {
        const int number = update[i];

        std::vector<int> left_of_number(update.begin(), update.begin() + i);
        std::vector<int> right_of_number(
            std::next(
                update.begin(),
                std::min(static_cast<std::size_t>(i + 1), update.size())
                ),
            update.end());

        std::vector<int> left_rules;
        std::vector<int> right_rules;
        for (auto [fst, snd] : rules) {
            if (snd == number) {
                left_rules.push_back(fst);
            } else if (fst == number) {
                right_rules.push_back(snd);
            }
        }

        const bool left_violation = check_subset_for_violation(left_of_number, right_rules);
        const bool right_violation = check_subset_for_violation(right_of_number, left_rules);

        if (left_violation || right_violation) is_valid = false;
    }
    return is_valid;
}

int main() {

    const std::string filename = "05_input.txt";
    std::ifstream file(filename, std::ios::in);

    if (!file.is_open()) {
        std::cerr << "Error opening file " << filename << std::endl;
        return 1;
    }

    std::vector<std::pair<int, int>> rules;
    std::vector<std::vector<int>> updates;

    std::string line;
    while (std::getline(file, line)) {
        if (line.contains('|')) {

            std::size_t separator = line.find('|');
            int left_number = std::stoi(line.substr(0, separator));
            int right_number = std::stoi(line.substr(separator + 1));
            rules.emplace_back(left_number, right_number);

        } else if (line.contains(',')) {
            std::vector<int> numbers;
            std::string s_number;
            std::stringstream ss(line);
            while (std::getline(ss, s_number, ',')) {
                numbers.emplace_back(std::stoi(s_number));
            }
            updates.push_back(numbers);
        }
    }

    std::vector<std::vector<int>> invalid_updates;
    int first_part_sum = 0;
    for (std::vector<int> update : updates) {
        if (update_is_valid(rules, update)) {
            int middle_index = static_cast<int>(update.size() / 2);
            first_part_sum += update[middle_index];
        } else {
            invalid_updates.push_back(std::move(update));
        }
    }
    std::cout << "First part: " << first_part_sum << std::endl;

    int second_part_sum = 0;
    for (std::vector<int> invalid_update : invalid_updates) {
        std::vector<int> corrected_update;
        corrected_update.reserve(invalid_update.size());

        while (!invalid_update.empty()) {
            int test_number = invalid_update.back();
            invalid_update.pop_back();

            for (int i = 0; i < corrected_update.size() + 1; i++) {
                std::vector<int> tmp_update = corrected_update;
                tmp_update.insert(tmp_update.begin() + i, test_number);
                if (update_is_valid(rules, tmp_update)) {
                    corrected_update = tmp_update;
                    break;
                }
            }
        }

        int middle_index = static_cast<int>(corrected_update.size() / 2);
        second_part_sum += corrected_update[middle_index];
    }

    std::cout << "Second part: " << second_part_sum << std::endl;

    return 0;
}