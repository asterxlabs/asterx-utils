import os

from asterx_utils.file.writer import FileWriter


TEST_OUT_DIR = 'GG'


def test_init():
    fw = FileWriter('test.txt', batch_size=100)

    assert fw.filename == 'test.txt'
    assert fw.batch_size == 100


def test_generate_fd():
    fw = FileWriter('test.txt', batch_size=100)
    fd = fw.generate_fd()

    assert fw.filename == 'test.txt'
    assert fw.batch_size == 100
    assert fd.write

    fw = FileWriter('dir_test.txt', directory=TEST_OUT_DIR)
    fd = fw.generate_fd()

    assert fd.name == os.path.join(TEST_OUT_DIR, 'dir_test.txt')

    fd = fw.generate_fd('wp.txt')

    assert fd.name == os.path.join(TEST_OUT_DIR, 'wp.txt')


