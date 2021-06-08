from Documents import documents, directories


def search_name(number_doc):
    """ функция, которая спросит номер документа и выведет имя человека, которому он принадлежит
    """
    for document in documents:
        documents_sorted = dict([(document['number'], document['name'])])
        for doc, name in documents_sorted.items():
            if number_doc == doc:
                print(f"Имя пользователя: {name}")
                return name
    print(f"Документ с номером '{number_doc}' отсутствует")
    return f'Error'


def find_shelf(doc_number):
    """функция, которая спросит номер документа и выведет номер полки, на которой он находится
    """
    for keys, values in directories.items():
        if doc_number in values:
            print(f"Номер полки: {keys}")
            return keys
    print(f"Полка с номером документа '{doc_number}' отсутствует")
    return f'Error'


def get_list():
    """ функция, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин"
    """
    result = " "
    for document in documents:
        result += f'\n{document["type"]} "{document["number"]}" "{document["name"]}"'
    print(result)
    return documents


def add_new_document():
    """ функция, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и
    номер полки, на котором он будет храниться."""
    doc_new = dict()
    doc_new['type'] = input('Введите тип документа: ')
    doc_new['number'] = input('Введите номер документа: ')
    doc_new['name'] = input('Введите имя и фамилию владельца документа: ')
    shelf = input("Введите номер полки для хранения информации: ")
    if shelf in directories.keys():
        directories[shelf].append(doc_new['number'])
        documents.append(doc_new)
        print(f"Документ с номером {doc_new['number']} добавлен на полку {shelf}")
        return directories[shelf], doc_new['number']
    else:
        print(f"Полка с номером {shelf} не существует")
        return f'Error'

def move_shelves():
    """функция, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую.
    """
    doc_number = input("Введите номер документа: ")
    doc_not_found = f"Документ с номером {doc_number} не найден"
    for keys, values in directories.items():
        if doc_number in values:
            shelf = input("Введите номер целевой полки: ")
            incorrect_shelf = f"Полка с номером {shelf} не существует"
            if shelf in directories.keys():
                directories[shelf].append(doc_number)
                doc_move = f"Документ {doc_number} перемещен на полку {shelf}"
                return doc_move
            return incorrect_shelf
    return doc_not_found
    # Документ перемещается на новую полку но со старой не получается убрать


def add_new_shelf(add_shelf):
    """функция, которая спросит номер новой полки и добавит ее в перечень.
    """
    #add_shelf = input("Введите номер новой полки: ")
    for _ in directories.keys():
        if add_shelf not in directories.keys():
            result = directories.setdefault(add_shelf, [])
            print(f'Полка с номером {add_shelf} добавлена в перечень')
            return directories
        print(f"Полка с номером {add_shelf} уже существует")
        return directories


def del_number_doc(doc_number):
    """ функция, которая спросит номер документа и удалит его из каталога и из перечня полок.
    """
    #doc_number = input("Введите номер документа: ")
    for document in documents:
        for keys, values in document.items():
            if document[keys] == doc_number:
                del document[keys]
                for number in directories:
                    if doc_number in directories[number]:
                        del directories[number]
                        print(f'Документ {doc_number} удален из каталога и из перечня полок')
                        return documents, directories
    print(f"Документа с номером {doc_number} не существует")
    return f'Error'
