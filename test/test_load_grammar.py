import pytest
from parso.grammar import load_grammar
from parso import grammar


def test_load_inexisting_grammar():
    # This version shouldn't be out for a while, but if we ever do, wow!
    with pytest.raises(NotImplementedError):
        load_grammar('15.8')
    # The same is true for very old grammars (even though this is probably not
    # going to be an issue.
    with pytest.raises(NotImplementedError):
        load_grammar('1.5')


@pytest.mark.parametrize(('string', 'result'), [
    ('2', 27), ('3', 36), ('1.1', 11), ('1.1.1', 11), ('300.1.31', 3001)
])
def test_parse_version(string, result):
    assert grammar._parse_version(string) == result


@pytest.mark.parametrize('string', ['1.', 'a', '#', '1.3.4.5', '1.12'])
def test_invalid_grammar_version(string):
    with pytest.raises(ValueError):
        load_grammar(string)


def test_grammar_int_version():
    with pytest.raises(TypeError):
        load_grammar(3.2)