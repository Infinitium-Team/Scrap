import basic
import os

while True:
	text = input(f'{os.getenv("USER") or os.getenv("USERNAME")}@Scrap > ')
	if text.strip() == "": continue
	result, error = basic.run('<stdin>', text)

	if error:
		print(error.as_string())
	elif result:
		if len(result.elements) == 1:
			print(repr(result.elements[0]))
		else:
			print(repr(result))