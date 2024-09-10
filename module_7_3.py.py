import string

class WordsFinder:
    def __init__(self, *file_names):
        # Сохраняем имена файлов в кортеже
        self.file_names = file_names

    def __repr__(self):
        return f"WordsFinder(file_names={self.file_names})"

    def get_all_words(self):
        all_words = {}  # Словарь для хранения имен файлов и их слов
        for file_name in self.file_names:
            try:
                with open(file_name, 'r', encoding='utf-8') as file:
                    # Читаем файл построчно
                    words = []
                    for line in file:
                        # Приводим строку к нижнему регистру
                        line = line.lower()
                        # Избавляемся от пунктуации
                        line = line.translate(str.maketrans('', '', string.punctuation.replace('-', '')))
                        # Разбиваем строку на слова
                        words.extend(line.split())
                    # Сохраняем список слов в словаре
                    all_words[file_name] = words
            except FileNotFoundError:
                all_words[file_name] = []  # Если файл не найден, добавляем пустой список
        return all_words

    def find(self, word):
        results = {}
        word_lower = word.lower()  # Приводим искомое слово к нижнему регистру
        all_words = self.get_all_words()  # Получаем все слова из файлов
        for file_name, words in all_words.items():
            if word_lower in words:
                results[file_name] = words.index(word_lower)  # Позиция первого вхождения слова
        return results

    def count(self, word):
        results = {}
        word_lower = word.lower()  # Приводим искомое слово к нижнему регистру
        all_words = self.get_all_words()  # Получаем все слова из файлов
        for file_name, words in all_words.items():
            count = words.count(word_lower)  # Подсчитываем количество вхождений слова
            if count > 0:
                results[file_name] = count
        return results

# Пример использования
finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # Позиция слова 'TEXT'
print(finder2.count('teXT'))  # Количество слов 'teXT' в тексте