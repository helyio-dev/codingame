#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_LEVEL 10
#define MAX_TITLE_LENGTH 50
#define MAX_ENTRIES 30
#define MAX_LINE_LENGTH 50

typedef struct {
    int level;
    char title[MAX_TITLE_LENGTH];
    int page;
} Entry;

int parse_input(int length_of_line, int N, Entry *entries) {
    char line[MAX_LINE_LENGTH + MAX_TITLE_LENGTH];
    int i;
    for (i = 0; i < N; i++) {
        if (fgets(line, sizeof(line), stdin) == NULL) return 0;
        
        char *ptr = line;
        int level = 0;
        while (*ptr == '>') {
            level++;
            ptr++;
        }
        entries[i].level = level;

        char *title_start = ptr;
        char *space_ptr = strrchr(title_start, ' ');
        if (space_ptr == NULL) return 0;

        *space_ptr = '\0';
        strcpy(entries[i].title, title_start);

        if (sscanf(space_ptr + 1, "%d", &entries[i].page) != 1) return 0;
    }
    return 1;
}

void print_toc(int length_of_line, int N, const Entry *entries) {
    int section_numbers[MAX_LEVEL] = {0};
    int i;
    for (i = 0; i < N; i++) {
        int current_level = entries[i].level;

        section_numbers[current_level]++;
        
        int j;
        for (j = current_level + 1; j < MAX_LEVEL; j++) {
            section_numbers[j] = 0;
        }

        int indent_size = current_level * 4;
        for (j = 0; j < indent_size; j++) {
            printf(" ");
        }

        char num_str[20] = "";
        
        int number_to_print;
        if (current_level == 0) {
             number_to_print = section_numbers[0];
        } else {
             number_to_print = section_numbers[current_level];
        }

        snprintf(num_str, sizeof(num_str), "%d", number_to_print);
        
        printf("%s %s", num_str, entries[i].title);

        int page_len = snprintf(NULL, 0, "%d", entries[i].page);
        
        int current_content_length = indent_size + strlen(num_str) + 1 + strlen(entries[i].title) + page_len;

        int num_dots = length_of_line - current_content_length;
        if (num_dots < 0) num_dots = 0; 

        for (j = 0; j < num_dots; j++) {
            printf(".");
        }

        printf("%d\n", entries[i].page);
    }
}

int main() {
    int length_of_line;
    int N;

    if (scanf("%d", &length_of_line) != 1) return 1;
    if (scanf("%d", &N) != 1) return 1;

    int c;
    while ((c = getchar()) != '\n' && c != EOF); 

    Entry entries[MAX_ENTRIES];
    
    if (!parse_input(length_of_line, N, entries)) return 1;

    print_toc(length_of_line, N, entries);

    return 0;
}