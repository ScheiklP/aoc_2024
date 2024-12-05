#include <iostream>
#include <fstream>
#include <vector>
#include <array>
#include <unordered_set>

bool valid_location(const int i, const int j, const std::size_t num_lines, const std::size_t num_chars) {
    const bool i_valid = 0 <= i && i < num_lines;
    const bool j_valid = 0 <= j && j < num_chars;

    return i_valid && j_valid;
}

int look_for_mas(
        const int i,
        const int j,
        const std::size_t num_lines,
        const std::size_t num_chars,
        const std::vector<std::string> &text
        ) {
    // Create indices to check for M, A, and S characters
    std::array<std::array<std::pair<int, int>,3>,8> search_directions;
    int step = 0;
    for (int a = -1; a <= 1; a++) {
        for (int b = -1; b <= 1; b++) {
            if (a == b && b == 0) continue;
            const std::array directions = {
                std::make_pair(i+a, j+b), // M
                std::make_pair(i+a*2, j+b*2), // A
                std::make_pair(i+a*3, j+b*3), // S
            };
            search_directions[step] = directions;
            step++;
        }
    }

    // Check the indices
    int xmas_counter = 0;
    constexpr std::array target_chars = {'M', 'A', 'S'};
    for (std::array<std::pair<int, int>, 3> direction : search_directions) {
        bool not_xmas = false;
        int target_char_counter = 0;
        for (auto [loc_i, loc_j] : direction) {
            if (valid_location(loc_i, loc_j, num_lines, num_chars)) {
                if (text[loc_i][loc_j] != target_chars[target_char_counter]) not_xmas = true;
            } else not_xmas = true;
            target_char_counter++;
        }
        if (!not_xmas) xmas_counter++;
    }

    return xmas_counter;
}

int look_for_xed_mas(
        const int i,
        const int j,
        const std::size_t num_lines,
        const std::size_t num_chars,
        const std::vector<std::string> &text
    ) {

    // Look on the diagonals at the A location
    const std::array<std::array<std::pair<int, int>,2>,2> diagonals = {{
        {{ {i - 1, j - 1}, {i + 1, j + 1}, }},
        {{ {i - 1, j + 1}, {i + 1, j - 1}, }},
    }};

    // Check both diagonals, if their chars are exactly M and S
    bool invalid = false;
    for (std::array<std::pair<int, int>, 2> diagonal : diagonals) {
        std::unordered_set<char> chars;
        const std::unordered_set target_chars = {'M', 'S'};

        for (auto [loc_i, loc_j] : diagonal) {
            if (valid_location(loc_i, loc_j, num_lines, num_chars)) chars.insert(text[loc_i][loc_j]);
        }
        if (chars != target_chars) invalid = true;
    }

    // If the location has a xed MAS, return 1
    return invalid ? 0 : 1;
}

int main() {
    const std::string filename = "04_input.txt";

    std::ifstream file(filename, std::ios::in);
    if (!file.is_open()) {
        std::cerr << "Failed to open the file." << std::endl;
        return 1;
    }

    std::size_t num_lines = 0;
    std::size_t num_chars = 0;
    std::vector<std::string> text;
    std::string line;
    while (std::getline(file, line)) {
        text.push_back(line);
        num_lines++;
    }
    file.close();
    num_chars = text[0].size();

    // First Part
    std::vector<std::pair<int, int>> possible_start_locations;
    for (int i = 0; i < num_lines; i++) {
        for (int j = 0; j < num_chars; j++) {
            if (text[i][j] == 'X') possible_start_locations.emplace_back(i, j);
        }
    }

    int total_hits = 0;
    for (auto [i, j] : possible_start_locations) {
        total_hits += look_for_mas(i, j, num_lines, num_chars, text);
    }

    std::cout << "First part: " << total_hits << std::endl;

    // Second Part
    std::vector<std::pair<int, int>> possible_start_locations_part2;
    for (int i = 0; i < num_lines; i++) {
        for (int j = 0; j < num_chars; j++) {
            if (text[i][j] == 'A') possible_start_locations_part2.emplace_back(i, j);
        }
    }

    int total_hits_part2 = 0;
    for (auto [i, j] : possible_start_locations_part2) {
        total_hits_part2 += look_for_xed_mas(i, j, num_lines, num_chars, text);
    }

    std::cout << "Second part: " << total_hits_part2 << std::endl;

    return 0;
}
