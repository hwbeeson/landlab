#! /usr/bin/env python

import unittest
import numpy as np
from numpy.testing import assert_array_equal

from landlab.field.grouped import ModelDataFields


class TestModelDataFields(unittest.TestCase):
    def test_init(self):
        fields = ModelDataFields()
        self.assertSetEqual(set(), fields.groups)

    def test_add_group(self):
        fields = ModelDataFields()
        fields.add_group('nodes', 12)
        self.assertSetEqual(set(['nodes']), fields.groups)

    def test_add_existing_group(self):
        fields = ModelDataFields()
        fields.add_group('nodes', 12)
        with self.assertRaises(ValueError):
            fields.add_group('nodes', 24)

    def test_add_multiple_groups(self):
        fields = ModelDataFields()
        fields.add_group('nodes', 12)
        fields.add_group('cells', 2)
        fields.add_group('faces', 7)
        fields.add_group('links', 7)
        self.assertSetEqual(set(['nodes', 'cells', 'faces', 'links']),
                            fields.groups)

    def test_ones(self):
        fields = ModelDataFields()
        fields.add_group('nodes', 12)
        fields.add_group('cells', 2)

        value_array = fields.ones('nodes')
        assert_array_equal(np.ones(12.), value_array)

        value_array = fields.ones('cells')
        assert_array_equal(np.ones(2.), value_array)

    def test_add_ones(self):
        fields = ModelDataFields()
        fields.add_group('nodes', 12)
        fields.add_group('cells', 2)

        fields.add_ones('nodes', 'z')
        assert_array_equal(np.ones(12.), fields['nodes']['z'])
        assert_array_equal(np.ones(12.), fields.field_values('nodes', 'z'))

        fields.add_ones('cells', 'z')
        assert_array_equal(np.ones(2.), fields['cells']['z'])
        assert_array_equal(np.ones(2.), fields.field_values('cells', 'z'))
