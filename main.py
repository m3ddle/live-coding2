example = "vfdsjsfaffffffffreitirrrrrert"

def longest_substring(string):

    substring_tracker = {}
    substring_length = 0
    index = 0
    subs_track = 0
    curent_char = ''
    while index < len(string):
        if index < len(string) - 1:
            
            if string[index + 1] == string[index]:
                current_char = string[index]
                subs_track += 1
                while current_char == string[index]:
                    substring_length += 1
                    index += 1
                    substring_tracker[subs_track] = substring_length
            else:
                index += 1
                substring_length = 0
        else:
            index += 1        
    indie = 0
    print(substring_tracker)
    for key in substring_tracker.values():
        if key > indie:
            indie = key
    return indie


if __name__ == "__main__":
    print(longest_substring(example))

