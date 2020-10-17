import music21
from audio-to-midi
score = music21.converter.parse('StarWars60.wav')
key = score.analyze('key')
print(key.tonic.name, key.mode)