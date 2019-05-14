import unittest
import queue
import array

import session8_hw

class TestMembers(unittest.TestCase):

    def setUp(self):
        self.heap = [('V', 1), ('V', 3), ('V', 2)]

    def test_display(self):
        self.assertEqual(session8_hw.display(session8_hw.Members.Afghanistan),
                         "\nMember name: Afghanistan \n Member value: 93\n")

    def test_name_order_by_value(self):
        self.assertEqual(
            session8_hw.name_order_by_value(session8_hw.Members),
            "\nCountry Name ordered by Country Code:"
            "\nAfghanistan"
            "\nAlgeria"
            "\nAngola"
            "\nAlbania"
            "\nAndorra"
        )

    def test_get_value(self):
        self.assertEqual(
            session8_hw.get_values(session8_hw.Members),
            [93, 355, 213, 376, 244]
        )

    def test_common_words(self):
        lst = [
            'red', 'green', 'black', 'pink', 'black', 'white', 'black', 'eyes',
            'white', 'black', 'orange', 'pink', 'pink', 'red', 'red', 'white', 'orange',
            'white', "black", 'pink', 'green', 'green', 'pink', 'green', 'pink',
            'white', 'orange', "orange", 'red'
        ]
        self.assertEqual(
            session8_hw.common_words(lst),
            [('pink', 6), ('black', 5), ('white', 5), ('red', 4)]
        )

    def test_class_roll(self):
        self.assertEqual(
            session8_hw.class_roll(session8_hw.CLASSES),
            {'V': [1, 2], 'VI': [1, 2, 3], 'VII': [1]}
        )

    def test_count_words(self):
        self.assertEqual(
            session8_hw.count_words(session8_hw.CLASSES),
            {'VI': 3, 'V': 2, 'VII': 1}
        )

    def test_unique(self):
        self.assertEqual(
            session8_hw.iterate(session8_hw.Members),
            (
                "sAfghanistan     = 93"
                "Albania         = 355"
                "Algeria         = 213"
                "Andorra         = 376"
                "Angola          = 244"
            )
        )
    def test_revered(self):
        self.assertEqual(
            [{k:v} for k, v in session8_hw.reversed_dict(session8_hw.Members)],
            [{"Angola": 244},
             {"Andorra": 376},
             {"Algeria": 213},
             {"Albania": 355},
             {"Afghanistan": 93}]
        )

    def test_sequence_dict(self):
        self.assertEqual(
            session8_hw.sequence_dict(session8_hw.SEQ),
            [('v', [1, 3]), ('vi', [2, 4]), ('vii', [1])]
        )

    def test_compere_lst(self):
        self.assertFalse(session8_hw.compere_list(
            [20, 10, 30, 10, 20, 30],
            [30, 20, 10, 30, 20, 50]
        ))

    def test_create_array(self):
        self.assertTrue(isinstance(
            session8_hw.create_array([1, 2, 3, 4]),
            array.array
        ))

    def test_array_size(self):
        self.assertEqual(
            session8_hw.array_size([1, 2, 3, 4]),
            (4, 4)
        )

    def test_array_buffer(self):
        memeory, size = session8_hw.array_buffer([1, 2, 3, 4])
        self.assertEqual(size, 4)

    def test_array_length(self):
        self.assertEqual(
            session8_hw.array_length([1, 2, 3, 4]),
            4
        )

    def test_insert_sorted(self):
        self.assertEqual(session8_hw.insert_sorted(
            [25, 45, 36, 47, 69, 48, 68, 78, 14, 36]),
            [14, 25, 36, 36, 45, 47, 48, 68, 69, 78]
        )

    def test_heap_push(self):
        session8_hw.heap_push(self.heap, ('V', 6))
        self.assertEqual(self.heap, [('V', 1), ('V', 3), ('V', 2), ('V', 6)])

    def test_heap_smallest(self):
        smallest, pop_smallest = session8_hw.heap_smallest(self.heap)
        self.assertEqual(smallest, ('V', 1))
        self.assertEqual(self.heap,[('V', 2), ('V', 3)])

    def test_heap_pop_push(self):
        session8_hw.heap_pop_push(self.heap, ('V', 6))
        self.assertEqual(self.heap, [('V', 2), ('V', 3), ('V', 6)])


    def test_heapsort(self):
        lst = [70, 20, 50, 40, 30, 60, 10, 80, 90, 100]
        self.assertEqual(session8_hw.heapsort(lst), [10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

    def test_h_23(self):
        lst = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
        self.assertEqual(session8_hw.h_23(lst), ([100, 90], [10, 20, 30]))

    def test_left_insert_point(self):
        self.assertEqual(session8_hw.left_insert_point([1, 2, 3, 4], 2), 1)

    def test_right_insert_point(self):
        self.assertEqual(session8_hw.right_insert_point([1, 2, 3, 4], 2), 2)

    def test_create_queue(self):
        self.assertEqual(session8_hw.create_queue(4), ([0, 1, 2, 3], 4))

    def test_empty_queue(self):
        que = queue.Queue()
        self.assertTrue(session8_hw.empty_queue(que))

    def test_fifo(self):
        fifo = session8_hw.fifo_queue(4)
        self.assertEqual([fifo.get() for i in range(fifo.qsize())], [0, 1, 2, 3])

    def test_lifo(self):
        lifo = session8_hw.lifo_queue(4)
        self.assertEqual([lifo.get() for i in range(lifo.qsize())], [3, 2, 1, 0])


if __name__ == "__main__":
    unittest.main()
