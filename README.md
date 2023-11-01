# Scrap

Welcome to Scrap, an unconventional programming language that created with 3 hours, it combines Python's functionality with a twist of bizarre syntax. If you're wondering, "wtf is this bro?" you're in the right place! Let's dive into the peculiar world of Scrap.

## Introduction

Scrap is a unique programming language that challenges traditional Python syntax. Its unusual constructs might leave you scratching your head, but fear not; understanding this language is an adventure in itself!

## Syntax

Scrap syntax is a fusion of Python and absurdity. Here are the key elements:

- **Define Function:** `define function_name(parameters) -> expression` defines a function. Yes, it starts with "define" and uses "->" for the return statement.
- **Loops:** Scrap replaces Python's "for" loops with `foreach i = start to end then` for loop iterations.
- **Conditional:** The traditional "if" statement is absent; Scrap relies on implicit conditions within loops and functions.
- **Print:** Output to the console is achieved using `printT()`, a quirky cousin of Python's `print()` function.
- **List Manipulation:** Scrap introduces its unique `append()` function for list operations.

## Example Usage

```
define oopify(prefix) -> prefix + "oop"

define join(elements, separator)
	declare result = ""
	declare len = len(elements)

	foreach i = 0 TO len then
		declare result = result + elements/i
		if i != len - 1 then declare result = result + separator
	END

	return result
END

define map(elements, definec)
	declare new_elements = []

	foreach i = 0 TO len(elements) then
		append(new_elements, func(elements/i))
	END

	return new_elements
END

printT("Greetings universe!")

foreach i = 0 TO 5 then
	printT(join(map(["l", "sp"], oopify), ", "))
END
```
This code snippet demonstrates the usage of Scrap functions. It prefixes the elements of the list ["l", "sp"] with "oop", then joins them with a comma and prints the result.

In Scrap, be prepared for the unexpected! Happy coding, or should I say, happy Scraping? 😄

# ⚠️ MIT License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/Infinitium-Team/Scrap/blob/main/LICENSE) file for details.
