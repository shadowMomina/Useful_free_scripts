# -------------------------------
# Text Case Converter Tool (Final Loop Version)
# -------------------------------
# Features:
# 1. Keeps running until the user chooses to exit.
# 2. First shows the action menu, then asks for the text.
# 3. Supports: Uppercase, Lowercase, Title Case, Sentence Case,
#    and Heading styles (H1, H2, H3).
# -------------------------------

def sentence_case(text):
    """Convert text into sentence case"""
    text = text.strip()
    if len(text) == 0:
        return text
    return text[0].upper() + text[1:].lower()

def heading_case(text, level=1):
    """Convert text into heading style (H1, H2, etc.)"""
    return f"{'#' * level} {text.title()}"

def main():
    print("\n--- Text Case Converter Tool ---\n")
    
    while True:  # Infinite loop until user exits
        # Show options first
        print("\nChoose a conversion option:")
        print("1. UPPERCASE")
        print("2. lowercase")
        print("3. Title Case")
        print("4. Sentence case")
        print("5. Heading (H1)")
        print("6. Heading (H2)")
        print("7. Heading (H3)")
        print("8. Exit Program")
        
        choice = input("\nEnter your choice (1-8): ")
        
        if choice == "8":
            print("\n✅ Exiting program. Goodbye!\n")
            break  # End loop only when user selects exit
        
        # Now ask for text input
        text = input("\nPaste your text (up to 100 words):\n\n")
        
        # Limit input to 100 words
        words = text.split()
        if len(words) > 100:
            print("\n⚠️ Limit exceeded! Only the first 100 words will be used.\n")
            text = " ".join(words[:100])
        
        print("\n--- Converted Text ---")
        
        if choice == "1":
            print(text.upper())
        elif choice == "2":
            print(text.lower())
        elif choice == "3":
            print(text.title())
        elif choice == "4":
            print(sentence_case(text))
        elif choice == "5":
            print(heading_case(text, 1))
        elif choice == "6":
            print(heading_case(text, 2))
        elif choice == "7":
            print(heading_case(text, 3))
        else:
            print("❌ Invalid choice! Please try again.")
        
        print("\n-----------------------\n")

# Run the program
if __name__ == "__main__":
    main()
