# Importing wikipediaapi and textwrap
#pip3 install wikipedia-api to install the library
import wikipediaapi
import textwrap

# this initializes the Wikipedia API object
wiki = wikipediaapi.Wikipedia('en')

# this section you put the topic to search for on Wikipedia
topic = input('Type in a topic you want to search on wikipedia: ')

# fetches the Wikipedia page 
page = wiki.page(topic)

# this code allows us to check if the page exists
if page.exists():
    # prints the full summary of the topic. 
    # if we use [:] it prints the first x amount of characters you want. 
    summary = page.summary
    # a width of 80 characters per line
    wrapped_summary = textwrap.fill(summary, width=80)
    print(wrapped_summary)

    # prints the table of contents
    print("\nTable of Contents:")
    toc = page.sections
    for section in toc:
        print(f"{'*' * (section.level - 1)} {section.title}")

    # the user chooses a section to read
    choice = input("\nEnter the number of the section you want to read (type 'q' to quit): ")

    # this coding prompts the user in a loop, until the user chooses to quit, q
    while choice != 'q':
        # Validating the user's choice
        try:
            choice = int(choice)
            section = toc[choice-1]
        except:
            print("Invalid choice.")

        # prints the contents of the selected section
        contents = section.text
        wrapped_contents = textwrap.fill(contents, width=80)
        print(wrapped_contents)

        # prompting the user to choose another section to read
        choice = input("\nEnter the number of another section you want to read (or 'q' to quit): ")

else:
    print(f"The page for '{topic}' does not exist on Wikipedia.")
