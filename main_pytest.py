from Personal_Dates import search_name, find_shelf


class TestPytest:

    def setup(self):
        print('method setup')

    def test_search_name(self):
        assert search_name('2207 876234') == 'Василий Гупкин'

    def test_search_name_wrong(self):
        assert search_name('2207') == 'Error'

    def test_find_shelf_wrong(self):
        assert find_shelf('10006') == 1

    def test_find_shelf(self):
        assert find_shelf('11-2') == 1

    def test_add_new_document(monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: "Mark")
        i = input("What is your name?")
        assert i == "Mark"

    def teardown(self):
        print('method teardown')
