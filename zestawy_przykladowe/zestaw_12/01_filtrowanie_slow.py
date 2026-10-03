import numbers


def process_words(words, condition, transform):
    return [transform(x) for x in words if condition(x)]

lista = ["python", "java", "C++", "JavaScript", "go", "Rust", "Kotlin", "PHP"]
words = lambda x: len(x) > 4
transform = lambda x: x.upper()

print(process_words(lista, words, transform))

words2 = lambda x: x[0].isupper()
transform2 = lambda x: len(x)

print(process_words(lista, words2, transform2))

words3 = lambda x: x.count("a")
transform3 = lambda x: x[::-1]

print(process_words(lista, words3, transform3))

