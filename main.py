import unittest
from Personal_Dates import del_number_doc


# search_name, find_shelf, get_list, add_new_shelf
# add_new_document, move_shelves, ,


class TestUnittest(unittest.TestCase):
    def setUp(self):
        print("Method setup")

    #def test_search_name_true(self):
     #   self.assertEqual(search_name('2207 876234'), 'Василий Гупкин')
      #  self.assertEqual(search_name('11-2'), 'Геннадий Покемонов')
       # self.assertEqual(search_name('10006'), 'Аристарх Павлов')

    #def test_search_name_true_error(self):
     #   self.assertEqual(search_name('0'), "Error")
      #  self.assertEqual(search_name(' '), "Error")

    #def test_search_name_wrong(self):
     #   self.assertNotEqual(search_name('2207 876234'), "Аристарх Павлов")

    #def test_search_name_wrong_error(self):
     #   self.assertNotEqual(search_name('2207 876234'), "Error")

    #def test_find_shelf(self):
     #   self.assertEqual(find_shelf('2207 876234'), '1')
      #  self.assertEqual(find_shelf('11-2'), '1')
       # self.assertEqual(find_shelf('10006'), '2')

    #def test_find_shelf_wrong(self):
     #   self.assertEqual(find_shelf('100'), 'Error')

    #def test_get_list(self):
     #   self.assertTrue(get_list(), "result = 'documents'")

    #def test_add_new_document(self):
     #   self.assertEqual(add_new_document())

    #def test_move_shelves(self):
     #   self.assertEqual(move_shelves(), )

    #def test_add_new_shelf(self):
     #   self.assertTrue(add_new_shelf('8'), 'result = directories')

    #def test_add_new_shelf_(self):
     #   self.assertTrue(add_new_shelf('1'), 'result = directories')

    def test_del_number_doc(self):
        self.assertEqual(del_number_doc('11-2'), )
    def tearDown(self):
        print(f"Method tearDown\n")


if __name__ == '__main__':
    unittest.main()