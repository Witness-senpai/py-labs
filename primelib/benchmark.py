import cProfile
import primesGenerator

cProfile.run("primesGenerator.test()", sort="tottime")
