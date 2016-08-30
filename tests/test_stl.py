from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from os import path
import unittest

from steno3d.parsers import ParseError
import steno3d
import steno3d_stl

class TestStl(unittest.TestCase):

    def setUp(self):
        stl_dir = path.split(path.realpath(steno3d_stl.__file__))[0]
        self.assets = stl_dir.split(path.sep)[:-1] + ['assets']

    def test_ascii(self):
        ascii_file = path.sep.join(self.assets + ['ascii.stl'])
        parser = steno3d.parsers.stl(ascii_file)
        projs = parser.parse()
        assert len(projs) == 1
        proj, = projs
        assert len(proj.resources) == 1
        assert isinstance(proj.resources[0], steno3d.Surface)
        assert proj.resources[0].mesh.nN == 4
        assert proj.resources[0].mesh.nC == 4

        parser = steno3d.parsers.AllParsers(ascii_file)
        projs = parser.parse()
        assert len(projs) == 1
        proj, = projs
        assert len(proj.resources) == 1
        assert isinstance(proj.resources[0], steno3d.Surface)
        assert proj.resources[0].mesh.nN == 4
        assert proj.resources[0].mesh.nC == 4

        proj = steno3d.Project()
        parser.parse(proj)
        assert len(proj.resources) == 1

    def test_ascii_error(self):
        self.assertRaises(ParseError, lambda: steno3d.parsers.stl('junk.stl'))
        self.assertRaises(ParseError, lambda: steno3d.parsers.stl(5))

        bad_files = [
            'ascii_bad0.stl',
            'ascii_bad1.stl',
            'ascii_bad2.stl',
        ]
        for f in bad_files:
            stlfile = path.sep.join(self.assets + [f])
            self.assertRaises(ParseError,
                              lambda: steno3d.parsers.stl(stlfile).parse())

    def test_binary(self):
        bin_file = path.sep.join(self.assets + ['beethoven.stl'])
        parser = steno3d.parsers.stl(bin_file)
        projs = parser.parse()
        assert len(projs) == 1
        proj, = projs
        assert len(proj.resources) == 1
        assert isinstance(proj.resources[0], steno3d.Surface)
        assert proj.resources[0].mesh.nC == 5028


if __name__ == '__main__':
    unittest.main()


