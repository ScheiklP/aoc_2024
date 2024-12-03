#include <algorithm>
#include <iostream>
#include <fstream>
#include <string>
#include <regex>
#include <sstream>
#include <vector>

int main() {
    const std::string filename = "03_input.txt";

    std::ifstream file(filename, std::ios::in);
    if (!file.is_open()) {
        std::cerr << "Failed to open the file." << std::endl;
        return 1;
    }

    std::string content;
    std::string line;
    while (std::getline(file, line)) {
        content += line;
    }

    std::regex pattern(R"((don't\(\))|(do\(\))|mul\((\d{1,3}),(\d{1,3})\))");
    std::vector<std::tuple<bool, bool, std::string, std::string>> results;

    int total_sum_1 = 0;
    int total_sum_2 = 0;

    auto words_begin = std::sregex_iterator(content.begin(), content.end(), pattern);
    auto words_end = std::sregex_iterator();

    for (std::regex_iterator i = words_begin; i != words_end; ++i) {
        std::smatch match = *i;
        bool disable = !match[1].str().empty();
        bool enable = !match[2].str().empty();
        std::string a = match[3].str();
        std::string b = match[4].str();
        results.emplace_back(disable, enable, a, b);
    }

    bool is_enabled = true;

    for (const auto& [disable_flag, enable_flag, a, b] : results) {
        if (!a.empty() && !b.empty()) {
            int product = std::stoi(a) * std::stoi(b);
            total_sum_1 += product;
            if (is_enabled) total_sum_2 += product;
        }
        if (disable_flag) is_enabled = false;
        if (enable_flag) is_enabled = true;
    }

    file.close();

    std::cout << "First part:" << total_sum_1 << std::endl;
    std::cout << "Second part:" << total_sum_2 << std::endl;

    return 0;
}
