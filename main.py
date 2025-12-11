import sys
from stats import get_num_words, sort_on, make_dict_list
file_path = sys.argv
if len(file_path)<2:
      print("Usage: python3 main.py <path_to_book>")
      sys.exit(1)

else:
      book_path = file_path[1]
      print("============ BOOKBOT ============", f"\nAnalyzing book found at {book_path}...",
            "\n----------- Word Count ----------", f"\nFound {get_num_words(book_path)} total words", 
            "\n--------- Character Count -------"
            )

#print(f"Found {get_num_words(file_path)} total words")
      sorted_dict = sorted(make_dict_list(book_path), reverse=True, key=sort_on, )
      for item in sorted_dict: # removes special char and spaces
            if item["char"].isalpha():
                  print(item["char"]+":", item["num"])

      print("============= END ===============")
      