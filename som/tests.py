#!/usr/bin/python
# encoding=utf-8
import pytest
from interpreter import *
from synthesizer import *
from effects_processor import *

#teste para o interpretador
def test_interpreter():
	print 'Testa se a pauta não tiver notas'
	assert len(generate_pairs('The Simpsons:d=4,o=5,b=160:')) == 0
	print 'Testa se a pauta tiver uma nota'
	assert len(generate_pairs('The Simpsons:d=4,o=5,b=160:c.6')) == 1
	print 'Testa se a pauta tiver seis notas'
	assert len(generate_pairs('The Simpsons:d=4,o=5,b=160:c.6,e6,f#6,8a6,g.6,e6')) == 6

#teste para o sintetizador
def test_synthesizer():
	print 'Testa se a lista estiver vazia'
	assert len(generate_sounds([],'888888888')) == 0
	print 'Testa se a lista tiver um par'
	assert len(generate_sounds([{'freq': 1046, 'time': 0.5625}],'888888888')) == 1
	print 'Testa se a lista tiver seis pares'
	assert len(generate_sounds([{'freq': 1046, 'time': 0.5625}, {'freq': 1318, 'time': 0.375}, {'freq': 1480, 'time': 0.375}, {'freq': 1760, 'time': 0.1875}, {'freq': 1568, 'time': 0.5625}, {'freq': 1318, 'time': 0.375}],'888888888')) == 6

#teste para o cálculo do módulo no processador de efeitos
def test_module():
	print 'Testa o módulo de -5'
	assert module(-5) == 5
	print 'Testa o módulo de 0'
	assert module(0) == 0
	print 'Testa o módulo de 1'
	assert module(1) == 1
	print 'Testa o módulo de 5'
	assert module(5) == 5

#teste para o efeito nulo
def test_effect_none():
	assert effect_none([],[]) == []
	assert effect_none([],[{'freq': 440, 'samples':[20,30,-10,0]},{'freq': 600, 'samples':[800, 10, 47]}]) == [20,30,-10,0,800,10,47]
	assert effect_none([200],[{'freq': 440, 'samples':[]},{'freq': 600, 'samples':[800, 47]}]) == [200,800,47]
